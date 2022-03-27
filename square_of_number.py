lower_range = int(input("Please write the lower range"))
upper_range = int(input("Please write the upper range"))
square_list = []
square = 0
for x in range(lower_range,upper_range+1):
    square_number = x*x
    square_list.append(square_number)
for x in square_list:
    square+=x
print(square)
print(square_list)
