# Function to check the name
def check_name(MyName):
    if MyName == "Vlad":
        return "Sup Vlad"
    if MyName != "Vlad":
        return f"Lier,  your name is not {MyName}, it's Vlad."
# what happens when correct name
print(check_name("Vlad"))
# what happens when incorrect name
print(check_name("Jack"))