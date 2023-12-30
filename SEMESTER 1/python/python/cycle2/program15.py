string1=input("ENTER THE STRING")
first=string1[0]
modified_string=first 
for char in string1[1:]:
  if char==first:
    modified_string+="$"
  else:
    modified_string+=char
print("modified string=",modified_string)

