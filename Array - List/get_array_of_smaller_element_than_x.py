# using naive approach
def getSmallerThanX(array, x):
    smallerArray = []
    for i in range(len(array)):
        if array[i] < x:
            smallerArray.append(array[i])
    return smallerArray


arr = list(map(int, input().split()))
x = int(input())
smallerList = getSmallerThanX(arr, x)
print(smallerList)


# using list comprehension
def getSmallerThanX(array, x):
    smallerArray = [i for i in array if i < x]
    return smallerArray


arr = list(map(int, input().split()))
x = int(input())
smallerList = getSmallerThanX(arr, x)
print(smallerList)


# using filter and lambda function
def getSmallerThanX(array, x):
    smallerArray = list(filter(lambda a: a < x, array))
    return smallerArray


arr = list(map(int, input().split()))
x = int(input())
smallerList = getSmallerThanX(arr, x)
print(smallerList)
