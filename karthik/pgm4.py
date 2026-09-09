m=int(input("Enter the starting number:"))
n=int(input("Enter the ending number;"))
sqr={i*i for i in range(m,n+1)if i%2==0}
print(f"Square of even numbers between {m} and {n} is {sqr}")