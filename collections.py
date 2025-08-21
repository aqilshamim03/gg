fruits = ["apple", "banana", "cherry"]
fruits.append("mango")       
fruits.remove("banana")
print("List:", fruits)

colors = ("red", "green", "blue")
print("Tuple:", colors)


numbers = {1, 2, 3, 3, 2}
numbers.add(4)
numbers.discard(1)
print("Set:", numbers)

person = {"name": "John", "age": 25, "city": "New York"}
person["age"] = 26
person["job"] = "Engineer"
del person["city"]
print("Dictionary:", person)


print("Iterating over List:")
for fruit in fruits:
    print(fruit)

print("Iterating over Tuple:")
for color in colors:
    print(color)

print("Iterating over Set:")
for number in numbers:
    print(number)

print("Iterating over Dictionary:")
for key, value in person.items():
    print(f"{key}: {value}")
