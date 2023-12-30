names=[]
n=int(input("ENTER THE NO.OF NAMES:"))
i=0
for i in range(n):
  name=input("ENTER THE NAME:")
  names.append(name)
count_a=0
for name in names:
  count_a+=name.lower().count("a")
print("no.of 'a&A' in the list",count_a)
