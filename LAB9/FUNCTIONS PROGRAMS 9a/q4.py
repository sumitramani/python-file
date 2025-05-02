print("Name: Sumit Ramani")
print("Roll No: 24BEE124")
lst = ['madam','Python',"malayalam","12321"]
new_lst=[]
for char in lst:
    str=char[::-1]
    if(str==char):
        new_lst.append(char)
print(new_lst)
        