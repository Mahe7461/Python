#list comprehension fetch full list in to a new list
vegetable=['carrat','onion','toomato','beans','potato']
newlis=[]
for i in vegetable:
    newlis.append(i)
print(newlis)

#To fetch the specific item
newlist=[]
for i in vegetable:
    if 'i' in i:
        
        newlist.append(i)
print(newlist)

# in single line
newitem=[x for x in vegetable if 'a' in x]
print(newitem)
