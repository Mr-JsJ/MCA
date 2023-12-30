list=input("ENTER THE WORDS SEPERATED BY SPACE").split()
long_len=0
for word in list:
  if len(word)>long_len:
    long_len=len(word)
print("LENGTH OF LONGEST WORD IS :",long_len)

