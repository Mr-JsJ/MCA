str=input("ENTER THE STRING")
if str.endswith("ing"):
  str=str+"ly"
else:
  str=str+"ing"
print("modified string",str)

