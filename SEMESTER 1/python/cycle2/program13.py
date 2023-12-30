List1=[]
List2=[]
common=[]
n1=int(input("ENTER THE NO.OF VALUES IN LIST1"))
n2=int(input("ENTER THE NO.OF VALUES IN LIST2"))
print("ENTER THE INTEGER VALUES IN 1ST LIST")
i=0
for i in range(n1):
  num=int(input(""))
  List1.append(num)
print("ENTER THE INTEGER VALUES IN 2ND LIST")
i=0
for i in range(n2):
  num=int(input(""))
  List2.append(num)
if len(List1)==len(List2):
   print("BOTH LIST HAVE SAME LENGTH.")
else:
   print("BOTH LIST HAVE DIFFERENT LENGTH.")
if sum(List1)==sum(List2):
  print("SUM OF BOTH LIST ARE SAME")
else:
  print("SUM OF BOTH LIST ARE DIFFERENT")
for value1 in List1:
   for value2 in List2:
     if value1==value2:
       common.append(value1)
if common:
 print("COMMON VALUES ARE:",common)
else:
 print("NO COMMON VAULES")

