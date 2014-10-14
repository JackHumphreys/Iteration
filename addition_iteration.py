# program to prompt for 8 numbers and report the total to the user

total = 0
for count in range(1,10):
    num = int(input("Please enter number {0} of your sequence".format(count)))
    total = total + num
print("The total is: {0}".format(total))


