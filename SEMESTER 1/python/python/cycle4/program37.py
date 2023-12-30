\def evenorodd(number):
  if(number%2==0):
    return 1
  else:
    return 0
number=int(input("enter the number::"))
n=evenorodd(number)
if(n==1):
 print(number,"is even")
else:
 print(number,"is odd")
