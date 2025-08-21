numbers =[11,20,31,40,51,60,71,80,91,100]
even = list(filter(lambda x: x%2 ==0 and x > 50, numbers))
print('numbers greater than 50 and are even;', even)



def even1(x):
    print('the output is:', x%2 )
    return x % 2 ==0 and x > 50
print(even1(100))
