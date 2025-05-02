print("Name: Sumit Ramani")
print("Roll No: 24BEE124")
list = [(), (1, 2), (), (3,), (4, 5, 6), ()]
filteredlist = []
for t in list:
    if t != ():
        filteredlist.append(t)

print("Filtered list:", filteredlist)
