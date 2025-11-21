# define a function to remove vowels from a string

def vowel():
  S = input("Enter the string ")
  S1 = S.uppercase()
  newS = ""

 # main stuff here
  for i in range(len(S)):
    # something looks messed up here
    if( S1[i] !="A" OR S1[i] !='E' OR S1[i] !='I' OR S1[i] !='O' OR S1[i] !='U'''):
       newS += S[i]
  print(newS)
vowels()
