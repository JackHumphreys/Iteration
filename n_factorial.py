#N factorial
n = int(input("Please enter n: "))
if n > 0:
    num1 = 1
    num2 = 1
    while num1 != n:
        num1 = num1 + 1
        num2 = num1 * num2
    print("{0} factorial is: {1}".format(n,num2))
else:
    print("This number is not valid. Try again.")
