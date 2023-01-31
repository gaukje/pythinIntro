# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
x = 5
y = 10
print(x + y)

# single line comment

"""  membership operators:
'x in y', 'x not in y' """

age = 18
if age > 18:
    print('ikke ok')
elif age == 18:
    print('kanskje')
else:
    print("ok")

count = 1
"""
while count < 10:
    print('the count is:', count)

    count = count + 1

    print("normal block")

"""

for c in 'Python':
    print('character: ', c)
"""
for num in range(10):
    print(num)

for num in range(2, 8):
    print(num)
"""

for num in range(1, 10, 2):
    print(num)

# list:

fruits = ['apple', 'banana', 'mango']


num = [1, 2, 3, 4]

mixed = ['apple', 2, 3, 4]

for f in fruits:
    print(f)

print(fruits[1])
