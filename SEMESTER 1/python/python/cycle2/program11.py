x=[]
n=int(input("Entr the no.of valus:"))
for i in range(n):
 a=int(input("Enter the integer:"))
 if a<100:
  x.append(a)
 else:
  x.append("over")
print("LIST:",x)
