input_line=input("ENTER THE LINE OF TEXT")
words=input_line.split()
word_count={}
for word in words:
  word=word.strip('.,!?').lower()
  word_count[word]=word_count.get(word,0)+1
print("WORD OCCURRENCS:",word_count)
