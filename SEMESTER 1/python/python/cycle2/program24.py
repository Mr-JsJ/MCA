dictionary={}
N=int(input("Enter the no.of values"))
i=0
for i in range(N):
  new_key=input("Enter the key shouid be a alphabet")
  new_val=int(input("Enter the value number"))
  dictionary[new_key]=new_val 
ascend_dict=dict(sorted(dictionary.items()))
print("Dictionary in ascending order by keys:",ascend_dict)
descend_dict=dict(sorted(dictionary.items(),reverse=True))
print("Dictionary in descening order by keys:",descend_dict)
