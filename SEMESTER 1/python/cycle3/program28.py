num_list=input("ENTER THE VALUES TO LIST SEPARETED BY SPACE:").split()
num_list1=[int(num)for num in num_list]
total=0
for num in num_list1:
  total+=num
print("SUM =",total)

