print("Name: Sumit Ramani")
print("Roll No: 24BEE124")
list = ["trisha" ,"maya", ("jai" ,"veeru"),"jaya"]
a = len(list)
c=0
d=0
for i in list:
    if isinstance(i,tuple):
        c+=len(i)
    else:
        d+=1
print(f"The number of boys are {c}")
print(f"The number of girls are {d}")