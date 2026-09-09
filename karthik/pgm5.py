txt=input("Enter a string:")
unique=set()
for ch in txt:
    unique.add(ch)
print(f"Unique characters in string: {unique}")