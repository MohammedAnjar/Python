"""num = [1,4,9,16,25,36,49,56,64,81,100]

for i in num:
    print(i)
"""

num = (1,4,9,16,25,36,49,56,64,81,100,49)
x = 49
idx = 0
for el in num:
    if(el == x):
        print(el , "found at idx", idx)
    idx += 1