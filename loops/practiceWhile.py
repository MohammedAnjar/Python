#find sum of first n number (using while)

n = int(input("Enter number : "))

i = 1
sum = 0
while(i <= n):
    sum = sum + i
    i += 1
print(sum)