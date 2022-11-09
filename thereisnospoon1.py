import sys
import math
import numpy as np
lst = []

def compute_neighbors(w,h, idx):
    for i, j in idx:
        if i+1 == w:
            right_x = -1
            left_x = -1
        else:
            right_x = i+1
            left_x
        if j+1 == h:
            bottom_y = -1
        else:
            bottom_y = j+1
        
        print(f'{i} {j} {right_x} {j} {i} {bottom_y}')



# Don't let the machines win. You are humanity's last hope...

width = int(input())  # the number of cells on the X axis
height = int(input())  # the number of cells on the Y axis
for i in range(height):
    line = input()  # width characters, each either 0 or .
    lst.append(list(line))
lst = np.array(lst)
#print("Debug messages... ",lst  , file=sys.stderr, flush=True)

power_node = np.where(lst=='0', 1, 0)
print("Debug messages... ",power_node  , file=sys.stderr, flush=True)
print("Debug messages... ",np.nonzero(power_node)  , file=sys.stderr, flush=True)
xx, yy = np.nonzero(power_node)
idx = list(zip(yy,xx))
compute_neighbors(width, height, idx)

# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)


# Three coordinates: a node, its right neighbor, its bottom neighbor
#print("0 0 1 0 0 1")
