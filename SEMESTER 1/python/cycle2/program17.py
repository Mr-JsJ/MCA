color_list1=input("ENTER the colors").split()
color_list2=input("ENTER the colors").split()
unique_color=[]
for color in color_list1:
  if color not in color_list2:
    unique_color.append(color)
print("COLOR from list1 not contained i list2:")
print(unique_color)
