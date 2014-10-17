#Rogue Value
new_num = 0
prev_num = 0
while new_num >= 0:
    if new_num >= prev_num:
        new_num = int(input("Please input a number of a series:"))
    new_num = (new_num+prev_num)
print(new_num)

