# Counting both lower and upper case letters from a string

l = 0
u = 0
S=input("Enter a string ")

# main stuff under here
for i in S:
  if(i.isupper()):
    u+=1
  elif(i.islower()):
    l+=1

print("Number of lowercase letters ",l)
print("Number of uppercase letters ",u)
