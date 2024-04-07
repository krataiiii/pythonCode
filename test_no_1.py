# Check duplicate items from list A and list B and append to a new list. Using your  preferred programming language. 
# List A : [1,2,3,5,6,8,9] 
# List B : [3,2,1,5,6,0] 

list = [1,2,3,5,6,8,9,3,2,1,5,6,0] 
newlist = [] 
duplicatelist = [] 
for i in list:
    if i not in newlist:
        newlist.append(i)
    else:
        duplicatelist.append(i) 
print("List of duplicates", duplicatelist)
print("Unique Item List", newlist) 