"""i = 1

while i <= 100:

    print(i)
    i += 1  """

"""i = 100

while i>0:
    
    print(i)
    i -= 1"""

"""
n = int(input("Enter number : "))
i = 1
while i<=10:
    
    print(n*i)
    i += 1"""


"""i = 1
while i<=10:
    print(i*i)
    i+=1"""

"""list = [1,4,9,16,25,36,49,56,64,81,100]

idx = 0
while (i <= len(list)-1):
    print(list[idx])
    idx += 1
"""

"""num = (1,4,9,16,25,36,49,56,64,81,100)

i = 0

while i <= len(num)-1:
    if num[i] == 56:
        print(num[i], "found")

    i += 1
"""

"""# Break statement
i = 0
while i <= 5:

    print(i)
    if (i == 3):
        break
    i += 1
"""

i = 0

while (i <= 5):

    if(i == 3):
        i += 1
        continue
    print(i)
    i += 1