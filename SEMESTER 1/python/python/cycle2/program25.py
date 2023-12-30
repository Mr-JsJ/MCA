dict1={}
dict2={}
n1=int(input("ENTER THE LIMIT OF FIRST DICTIONARY:"))
i=0
for i in range(n1):
 new_key=input("ENTER THE ALPHABET KEY")
 new_value=input("ENTER THE VALUE INTEGER")
 dict1[new_key]=new_value
n2=int(input("ENTER THE LIMIT OF SECOND DICTIONARY:"))
i=0
for i in range(n2):
 new_key=input("ENTER THE ALPHABET KEY")
 new_value=input("ENTER THE VALUE INTEGER")
 dict2[new_key]=new_value

merged_dict=dict1.copy()
merged_dict.update(dict2)
print("dictionary1:",dict1)
print("dictionary2:",dict2)
print("Merged dictionary:",merged_dict)
