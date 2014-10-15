#Backwards Print Program
string = input("Please enter a word: ")
length = len(string)
for count in length:
    print(string[length - count - 1])
