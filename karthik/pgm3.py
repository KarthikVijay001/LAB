n=int(input("Enter the no of elements:"))
list=[]
for i in range(n):
    num=int(input(f"Enter element {i+1}:"))
    list.append(num)
unique=[]
for i in list:
    if i not in unique:
        unique.append(i)
print(f"Unique elements are {unique}")