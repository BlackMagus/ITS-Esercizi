def make_shirt(size:str, message:str):
    if size == "L":
        message = "I Love Python"
    print(f"è stata prodotta una T-Shirt di taglia {size} e con la scritta: {message}")


make_shirt("M", "Sei un Grande!")
make_shirt("L", "Daje!!!")

