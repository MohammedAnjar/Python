#sum of first n number using recurssion
def sum(n):
    if(n==1):
        return 1 
    return sum(n-1) + n

n = int(input("Enter number : "))
print(sum(n))

