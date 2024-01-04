file = open("file1.txt","r")
file2 = open("file2.txt","w")
line = file.readlines()
for i in range(len(line)):
	if(i%2!=0):
		file2.write(line[i])
file.close()
file2.close()
