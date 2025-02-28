users = ("")
i = 0

if not users:
    print("We need to find some users!")

else:
    while users[i] != "Admin":
      print(f"Hello {users[i]}!")
      i = i + 1
    print("Hello admin, would you like to see a status report?")