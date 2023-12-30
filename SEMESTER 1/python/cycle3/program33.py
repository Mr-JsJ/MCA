num=int(input("ENTER THE NUMBER"))
reverse_num=0
while num>0:
  digit=num%10
  reverse_num=reverse_num*10+digit
  num=num//10
print("REVESED NUMBER",reverse_num)
