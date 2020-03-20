# Python Refresher
# Variables, Strings, Int and Print
age = 22
name = "Nick"
name2 = 'Matt'
todayIsCold = False

print(f'Hello, my name is {name} and I am {age} years old.')

# IF statements and comments
# a comment in code
""" A comment in
multiple
lines"""
if age != 15:
    print("You're older than 18")
    print("This is another line")
else:
    print("You're younger than  18")

# Functions


def hello(name='Sean', age=0):
    print("Hello {} you are {} years old".format(name, age))
    return "Hello {} you are {} years old".format(name, age)


sentence = hello()
print(sentence)

# Lists
dognames = ['Fido', 'Sean', 'Sally', 'Mark', 202, True, False, 2.78]
dognames.insert(0, 'Jane')
dognames[1] = 'Jason'
del(dognames[2])
print(len(dognames))
print(dognames[3])

# Loops
dognames = ['Fido', 'Sean', 'Sally', 'Mark']

for dog in dognames:
    print(dog)

for x in range(1, 100):
    print(x)

age = 0
while age < 18:
    print(age)
    age += 1

# Dictionaries
dogs = {
    "Fido": 8,
    "Sally": 17,
    "Sean": 2
}
print(dogs['Sean'])

del(dogs['Sean'])
print(dogs)

dogs['Sarah'] = 6
dogs['Fido'] = False
print(dogs)

# Classes


class Dog:
    info = "Dogs are cool!"

    def bark(self, str):
        print("BARK!", str)


mydog = Dog()
mydog.bark('asdasfdsad')

mydog.name = "Fido"
mydog.age = "Age"

print(mydog.name)
print(mydog.age)

mydog.info = "Hey there!"
print(mydog.info)


class Cat:
    def __init__(self, name='', age=0, furcolor=''):
        self.name = name
        self.age = age
        self.furcolor = furcolor

    def meow(self, str):
        print('meow!', str)


mycat = Cat("Lula", 13, "Brown")
mycat2 = Cat()
print(mycat.age)
print(mycat2.age)
