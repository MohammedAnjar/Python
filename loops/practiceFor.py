"""#find sum of first n number (using for)

n = int(input("Enter number : "))
sum = 0
for i in range(1,n+1):
    sum += i
print(sum)""" 

#factorial using for loop

n = int(input("Enter number : "))
fact = 1
for i in range(n,0,-1):
    fact = fact * i
print(fact)    