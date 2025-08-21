def happy_birthday():
    print('Happy birthday to you')
    print('you have become old!')
    print('Happy birthday to you')
happy_birthday()

def happy_birthday1(name):
    print(f'Happy birthday to {name}! ')      #fstring to assign variable while calling function
    print('you became old')
happy_birthday1('Nasir')
happy_birthday1('Aqil')

#now adding with 2 parameters
def happy_birthday2(name,age):                     #position of paramters do matter 
    print(f'Happy birthday to you {name}!')
    print(f'you are {age} years old !')
happy_birthday2('Nasir',49)



def create_name(first,last):
    first = first.capitalize()
    last = last.capitalize()
    return first + ' ' + last
full_name = create_name('bro','code')
print(full_name)