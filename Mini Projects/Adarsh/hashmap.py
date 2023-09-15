def main():
    hashMap = {}

    for i in range(0, 10):
        key = int(input("Enter the value : "))
        if hashMap.get(key):
            hashMap[key] += 1
        else:
            hashMap[key] = 1

    return hashMap


def findMax(hashmap):
    values = hashmap.items()
    maximum = (0, 0)
    for i in values:
        if maximum[1] < i[1]:
            maximum = i

    print(maximum[0])


newMap = main()
print("The element with the highest frequency is:")
findMax(newMap)
