a = input("Enter a comma-separated list of integers: ")
int_tuple = tuple(map(int, a.split(',')))

total_sum = sum(int_tuple)
print("Sum of the integers:", total_sum)