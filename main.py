# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


f = open('24.txt').read()
s = f.split()
a, e, ii, o, u, y = 0, 0, 0, 0, 0, 0
for i in range(2,6):
    if i*"A" in s:
        a+=1

    if i*"E" in f:
        e= e+1

    if i*"I" in f:
        ii = i +1

    if i*"O" in f:
        o= o + 1

    if i*"U" in f:
        u = u + 1

    if i*"Y" in f:
        y = y + 1
    break
summ =  y +o +e + ii  + a +e
print(summ)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
