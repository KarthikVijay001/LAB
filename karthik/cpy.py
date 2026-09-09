src = open("src.txt", "r")
dest = open("destination.txt", "w")
while True:
  ch = src.read(1)
  if not ch:
   break
  dest.write(ch)
src.close()
dest.close()
print("File copied successfully!")