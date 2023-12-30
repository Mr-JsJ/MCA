list_num=[]
n=int(input("ENTER THE LIMIT:"))
i=0
for i in range(n):
  num=int(input("ENTER THE VALUES:"))
  list_num.append(num)
positive=[num1 for num1 in list_num if num1>0]
N=int(input("ENTER THE LIMIT:"))
squered=[num2 **2 for num2 in range(1,N+1)]
print("THE LIST OF NUMBER:",list_num)
print("+ve numbers=",positive)
print("^2 of numbers=",squered)
word=input("ENTER THE STRING")
print(word)
vowels=[char for char in word if char.lower() in'aeiou']
print("vowels in word",word,"are",vowels)
orginal_val=[ord(char)for char in word]
print(orginal_val)
