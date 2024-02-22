#list1 = [1,2,3,2,1]
list1 = [1, "abc", "abc", 1]

list2 = list1.copy()
list2.reverse()

if(list1 == list2):
    print("List is palindrome")

else:
    print("List is not palindrome")