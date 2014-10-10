#Secret password exercise
#Jack Humphreys

password = ""
while password != "secret":
    password = input("Please enter you password: ")
    if password == "secret":
        print("Correct password")
    else:
        print("Incorrect password - retry")
