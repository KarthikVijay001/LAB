n=int(input("Enter the number of elements in the list:"))
number=[]
for i in range(n):
    num=int(input(f"Enter the elements {i+1}:"))
    number.append(num)
even=[]
for num in number:
    if num%2==0:
        even.append(num)
print(f"original list:{number}")
print(f"even numbers:{even}")