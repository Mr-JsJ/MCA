str=input("Enter the string:")
n=len(str)
newstr=str[n-1]+str[1:n-1]+str[0]
print("Modified string:",newstr)
