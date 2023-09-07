map1={}
for i in range(0,10):
    key=int(input("Enter the key:"))
    if map1.get(key):
        map1[key]+=1
    else:
        map1[key]=1
print(map1)

#Finding a number having max occurance
val=map1.items()
max=(0,0)  #(number,occurrance)
for i in val:
    if(max[1]<i[1]):
        max=i 
print("Max occurance num:",max[0])

#Finding duplicate value and removing 
l=[map1.keys()]
print(l)