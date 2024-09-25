import os

current_dir = os.getcwd()

for i in range(4,26):
    subfolder = f'{current_dir}\{i}'
    open(f'{subfolder}\{i}-2018-2.py', 'x')