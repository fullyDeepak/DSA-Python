# using naive approach
def getReverseArr(array):
    newArray = []
    for i in range(len(array)):
        newList = []
        newList.append(array[i])
        newArray = newList + newArray
    return newArray


arr = list(map(int, input().split()))

reversedArr = getReverseArr(arr)
print(reversedArr)


# using reverse loop
def getReverseArr(array):
    newArray = []
    for i in range(len(array), 0, -1):
        newArray.append(array[i-1])
    return newArray


arr = list(map(int, input().split()))

reversedArr = getReverseArr(arr)
print(reversedArr)


# using reverse indexing
def getReverseArr(array):
    newArray = []
    for i in range(1, len(array)+1):
        newArray.append(array[-i])
    return newArray


arr = list(map(int, input().split()))

reversedArr = getReverseArr(arr)
print(reversedArr)


# using list slicing
def getReverseArr(arr):
    # slicing syntax [start : stop : step]
    return arr[::-1]  # OR arr[len(arr):0:-1]


arr = list(map(int, input().split()))

reversedArr = getReverseArr(arr)
print(reversedArr)
