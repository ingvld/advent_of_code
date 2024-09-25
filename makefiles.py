import os

for i in range(2023,2024):
    yeardir = str(i)
    for n in range(2, 26):
        daypath = yeardir + '/' + str(n)
        os.mkdir(daypath)
        open(f'{daypath}/{n}-1.py', 'x')
        open(f'{daypath}/{n}-2.py', 'x')
        open(f'{daypath}/{n}-test.txt', 'x')
        open(f'{daypath}/{n}-input.txt', 'x')
