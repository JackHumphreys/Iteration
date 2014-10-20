#N factorial
n = int(input("Please enter n: "))
num1 = 1
num2 = 1
while num1 != n:
    num1 = num1 + 1
    num2 = num1 * num2
print(num2)
