numbers=[]
n=int(input("Enter the no.of values"))
i=0
for i in range(n):
  val=int(input("Enter the number"))
  numbers.append(val)
odd_numbers=[]
for num in numbers:
  if num%2!=0:
     odd_numbers.append(num)
print("LIST OF NUMBERS AFTER REMOVING EVEN NUMBERS:",odd_numbers)

