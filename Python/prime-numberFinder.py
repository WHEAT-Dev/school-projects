num = int(input("Enter the number "))
n = 0

#finding number of factors
for i in range (a):
  if(a % i == 0):
    n++

if(n == 2): #prime number have only 2 factors
  print(num," is a prime number")
else:
  print(num," is not prime number")
