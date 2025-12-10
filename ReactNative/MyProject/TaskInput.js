import React,{useState} from "react";
import { StyleSheet, TextInput, View, Button, Modal } from "react-native";

const TaskInput = (props) => {
  const [task, setTask] = useState("");
 
   function taskInputHandler(enteredTask) {
     console.log(enteredTask);
     setTask(enteredTask);
   }
 function addTask() {
    props.onAddTask(task);
    setTask("");
 }
  return (
    <Modal visible={props.visible}>
    <View style={styles.inputContainer}>
      <TextInput
        style={styles.textInput}
        placeholder="Inserisci task"
        onChangeText={taskInputHandler}
        value={task}
      />
      <Button
        title="Aggiungi"
        onPress={addTask}
        disabled={task === ""}
      ></Button>
      <Button
        title="Annulla"
        onPress={props.onCancel}
        
      ></Button>
    </View>
    </Modal>
  );
};

const styles = StyleSheet.create({
  textInput: {
    borderWidth: 1,
    borderColor: "#cccccc",
    width: "70%",
    padding: 8,
  },
  inputContainer: {
    flex: 1,
    flexDirection: "row",
    justifyContent: "space-between",
    alignItems: "center",
    marginBottom: 24,
    borderBottomWidth: 1,
    borderColor: "#cccccc",
  },
});
export default TaskInput;