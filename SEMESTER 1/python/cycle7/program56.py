file = open("file1.txt","r")
lines=[]
for line in file:
	lines.append(line)
print(lines)
file.close()
