def senior():
   amount=int(input("Enter the amount:"))
   time=int(input("Enter the duration:"))
   interest=(amount*12*time)/100
   print("Simple interest=",interest)
def other():
   amount=int(input("Enter the amount:"))
   time=int(input("Enter the duration:"))
   interest=(amount*10*time)/100
   print("Simple interest=",interest)

age=int(input("Enter the age:"))
if age>50:
  print("YOU ARE SENIOR CITIZEN")
  senior()
else:
  print("YOU ARE NOT SENIOR CITIZEN")
  other()

