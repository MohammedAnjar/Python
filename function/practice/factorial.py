def cal_fact(n):
    fact = 1
    for i in range(n,0,-1):
        fact = fact * i
    return fact




n = int(input("Enter number : "))

print(cal_fact(n))
