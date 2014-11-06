#Not complete
#5 values per line

squares = int(input("Please enter the amount of square numbers you want: "))
rows = squares//5
count = 1
while squares <= 5: 
    for count in range(1,6):
        print("{0:>2}".format(count*count),end=" ")
        count = count+1
