n=int(input(f"Enter the no of elements:"))
list = []
for i in range(n):
    a = int(input(f"Enter 1st element :"))
    b = int(input(f"Enter 2nd element :"))
    tup=(a,b)
    list.append(tup)
tuple=tuple(list)
print(f"The tuple is: {tuple}")
for i in range(n):
    for j in range(0,n-i-1):
        if list[j][1]>list[j+1][1]:
            temp=list[j]
            list[j]=list[j+1]
            list[j+1]=temp
print(f"Sorted={list}")