const TASKS_URL = "https://todoapp-875ed-default-rtdb.europe-west1.firebasedatabase.app/task";

async function handleResponse(response) {
  if (!response.ok) {
    const errorText = response.text();
    throw new Error("Fire base error:" + response.status + " " + errorText);
  }
  return response.json();
}

export async function fetchTasks() {
  try {
    const response = await fetch(TASKS_URL + ".json");
    const data = await handleResponse(response);
    // console.log("data",data)
    if (!data) {
      return [];
    }
    const tasks = Object.keys(data).map((id) => {
      console.log(id);
      return {
        id,

        ...data[id],
      };
    });
    console.log("tasks", tasks);
    return tasks;
    //   return Object.entries(data).map(([id, value]) => ({
    //   id,
    //   text: value.text,
    //   done: Boolean(value.done),
    // }));
  } catch (err) {
    console.error("ERRORE fecthTasks:" + err);
  }
}

export async function addTask(taskText) {
  try {
    const newTask = { text: taskText, done: false };
    const response = await fetch(TASKS_URL + ".json", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(newTask),
    });
    return await response.json();
  } catch (err) {
    console.log("Errore:", err);
    return null;
  }
}

export async function doneTask(task) {
  const response = await fetch(TASKS_URL + task.id + ".json", {
    method: "PATCH",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ done: !task.done }),
  });

  await handleResponse(response);
}
import React from "react";
import { Text, View ,StyleSheet, Pressable} from "react-native";

const TaskItem = ({taskItem,onDelete}) => {
  return (
    <View style={styles.taskItem}>
    <Pressable 
    android_ripple={{ color: '#210644' }} 
    onPress={()=>onDelete(taskItem)}
    style={({ pressed }) => pressed && styles.pressedItem}

    >
   
      <Text style={styles.taskText}>{taskItem.text}</Text>

    </Pressable>
    </View>
  );
};

export default TaskItem;

const styles = StyleSheet.create({
  taskItem: {
    margin: 8,
    borderRadius: 6,
    backgroundColor: "#5e0acc",
  },
  pressedItem:{
    opacity:0.5
  },
  taskText: {
    color: "#fff", 
    padding: 8,
  },
});