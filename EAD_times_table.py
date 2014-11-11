integer = int(input("Please enter a integer: "))
for count in range(1,13):
    answer = (integer*count)
    print("{0:>2} * {1} = {2:>3}".format(count,integer,answer))
