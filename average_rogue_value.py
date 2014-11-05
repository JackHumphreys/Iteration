count = 0
total = 0
num = int(input("Please enter a number of a series: "))

while num >= 0:
        total = num + total
        count = count + 1
        num = int(input("Please enter a number of a series: "))

if count == 0:
        print("Goodbye")
else:
        average = total/count
        print("The average value is {0}".format(average))
