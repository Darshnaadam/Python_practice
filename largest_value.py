largest_value = 1
print('Before',largest_value)
for the_num in [9,41,12,3,74,15]:
    if the_num > largest_value:
        largest_value = the_num
    print(largest_value,the_num)
print("After",largest_value)