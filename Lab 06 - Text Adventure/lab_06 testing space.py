"""14. Advanced Looping problems"""
# problem 1
print("problem 1")
for i in range(10):
    print("*", end=" ")
print()

# problem 2
print("problem 2")
for i in range(35):
    print("*", end=" ")
    if i == 9 or i == 14:
        print()
print()

# problem 3
print("problem 3")
for i in range(8):
    for i in range(10):
        print("*", end=" ")
    print()
print()

# problem 4
print("problem 4")
for i in range(10):
    for i in range(5):
        print("*", end=" ")
    print()
print()

# problem 5
print("problem 5")
for i in range(5):
    for i in range(20):
        print("*", end=" ")
    print()
print()

# problem 6
print("problem 6")
for i in range(10):
    for j in range(10):
        print(j, end=" ")
    print()
print()

# problem 7
print("problem 7")
for i in range(10):
    for j in range(10):
        print(i, end=" ")
    print()
print()

# problem 8
print("problem 8")
for i in range(10):
    for j in range(i+1):
       print(j, end=" ")
    print()
print()

# problem 9
print("problem 9")
for i in range(10):
    for k in range(i):
        print(" ", end=" ")
    for j in range(10-i):
        print(j, end=" ")
    print()
print()

# problem 10
print("problem 10")
for i in range(9):
    for j in range(9):
        product = (i + 1)*(j + 1)
        if product < 10:
            print(end=" ")
        print(product, end=" ")

    print()
print()

# problem 11
print("problem 11")
for i in range(1,10):
    for j in range(10-i):
        print("  ", end="")
    for j in range(1,i+1):
        print(j, end=" ")
    for j in range(1,i):
        print(i-j, end=" ")
    print()

"""15. Introduction to lists"""

# use () to define a tuple, use [] to define a list
# use type(thing) to return the type of data that "thing" is

x = (2,3,4,5)
print("x = ", x, "and is of type:", type(x))
x = [2,3,4,5]
print("x = ", x, "and is of type:", type(x))

# this creates a list:
x = [10, 20, 30]
# this returns the 0th position item in that list (0 index for python)
print(x[0])
# using negative numbers returns the value from the "back" of the array
print(x[-1])
# use the index position to reassign a particular element of an array
print(x)
x[0] = 22
print("I just reassigned the first value of the array to be 22.")
print(x)
# note that tuples cannot be changed once they're created; pycharm throws an error if you try

# create an empty list by just typing brackets:
# my_list = []

# have python do something for each element in the list, using a "for-each" loop:
my_list = [101, 20, 10, 50, 60, "spoon", "fork", "knife"]
for item in my_list:
    print(item)
# note that lists can contain mixed things, or even other lists

# have python do something for only a certain number of elements in my list:
for index in range(3):
    print(my_list[index])

# to find the length of a list, use len(my_list)
len(my_list)

# use an index variable to directly access (and potentially modify) the elements of a list:
for index in range(len(my_list)):
    print(my_list[index])

# if I want the position and the value, use enumerate:
print("here is this bit")
for index, value in enumerate(my_list):
    print(index, value)

# use .append to add to a list:
my_list_2 = [2,4,5,6]
print(my_list_2)
my_list_2.append(9)
print(my_list_2)

# build a list from scratch with user input!
# my_list_3 = []
# for i in range(5):
#     user_input = input( "Enter an integer: ")
#     user_input = int(user_input)
#     my_list_3.append(user_input)
#     print(my_list_3)

# to create an array with a specific length, n, you can do something like this:
# my_list = [0] * n
# my_list = [0] * 100

# let's sum up the values in an array:
my_list = [5, 76, 8, 5, 3, 3, 56, 5, 23]
list_total = 0
for index in range(len(my_list)):
    list_total += my_list[index]
print(my_list)
print(list_total)

# or do that same thing with a for loop to iterate the array:
my_list = [1, 2, 3, 5, 6, 7, 11]
list_total = 0
for item in my_list:
    list_total += item
print(my_list)
print(list_total)

# note that you need to use the index type of for loop to change the values, though:
my_list = [1, 2, 3, 10]
print("here's a list")
print(my_list)
print("now let's double each value")
for index in range(len(my_list)):
    my_list[index] = my_list[index] * 2 # double the value of all entries in my list
print(my_list)

# Slicing Strings
x = "This is a sample string"
#x = "0123456789"

print("x=", x)

# Accessing the first character ("T")
print("x[0]=", x[0])

# Accessing the second character ("h")
print("x[1]=", x[1])

# Accessing from the right side ("g")
print("x[-1]=", x[-1])

# Access 0-5 ("This ")
print("x[:6]=", x[:6])
# Access 6 to the end ("is a sample string")
print("x[6:]=", x[6:])
# Access 6-8
print("x[6:9]=", x[6:9])

a = "Hi"
b = "There"
c = "!"
print(a + b)
print(a + b + c)
print(3 * a)
print(a * 3)
print((a * 2) + (b * 2))

a = "Hi There"
print(len(a))

b = [3, 4, 5, 6, 76, 4, 3, 3]
print(len(b))

months = "JanFebMarAprMayJunJulAugSepOctNovDec"
n = int(input("Enter a month number: "))
print(months[3 * n - 3:3 * n])

plain_text = "This is a test. ABC abc"

for c in plain_text:
    print(c, end=" ")