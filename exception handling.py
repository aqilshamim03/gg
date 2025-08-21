try:
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))
    result = num1 / num2
    print("Result:", result)
except ZeroDivisionError as e:
    print(" You cannot divide by zero!", e)
except ValueError :
    print(" Please enter only numbers!")




try:
    a = [1, 2, 3]
    print(a[5])   # Index out of range
except Exception as e:
    print("Error occurred:", e)
