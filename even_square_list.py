def even_square_list(numbers):
    even_squares = []

    for num in numbers:
        if num % 2 == 0:
            even_squares.append(num ** 2)

    return even_squares

user_input = input("Enter list of integers seperated by spaces: ")
input_list = [int(x) for x in user_input.split()]

result = even_square_list(input_list)
print("Squares of even numbers: ", result)