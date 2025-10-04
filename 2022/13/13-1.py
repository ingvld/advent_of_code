from sys import argv
import re

with open(argv[1]) as f:
    lines = f.readlines()

total=0
current_pair=1

def get_nums(packet):
    ls = []
    level = 0
    for r in re.findall(r"(\[|\d+)",packet[1:]):
        current = ls
        for i in range(level):
            current = current[-1]
        match r:
            case "[":
                current.append([])
            case "]":
                level -= 1
            case _:
                current.append(int(r))
    return ls
        
        

for i in range(0,len(lines),3):
    p1,p2=lines[i:i+2]
    nums1,nums2=get_nums(p1),get_nums(p2)
    print(p1,p2)
    print(nums1,nums2)
    if nums1<=nums2:
        total+=current_pair
    current_pair+=1

print(total)
