map1 = {}

#1 2 3 2 7 5 7 8 9 7  
for i in range(0, 10):
    key = int(input("Enter the value : "))
    if map1.get(key):
        map1[key]+=1
    else:
        map1[key] = 1

val = map1.keys()
