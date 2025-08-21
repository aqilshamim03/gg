fruits = ["apple", "banana", "cherry", "mango"]

fruits[1], fruits[2] = fruits[2], fruits[1]    ## Swap positions of elements (banana and cherry)

print(fruits)  


#lists are mutable so they can be directly changed, but tuples are immutable they cannot be changed so they have to be converted into list then we can change there positions

numbers = (10, 20, 30)

# Convert to list
temp_list = list(numbers)

# Swap
temp_list[0], temp_list[2] = temp_list[2], temp_list[0]

# Convert back to tuple
numbers = tuple(temp_list)

print(numbers)
