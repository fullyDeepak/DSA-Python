# using naive Approach
def getOddEvenArray(array):
    odd_arr = []
    even_arr = []
    for i in range(len(array)):
        if array[i] % 2 != 0:
            odd_arr.append(array[i])
        else:
            even_arr.append(array[i])
    return (odd_arr, even_arr)


arr = list(map(int, input().split()))
odd, even = getOddEvenArray(arr)
print(odd, even)


# Using list comprehension
def getOddEvenArray(array):
    oddArr = [x for x in array if x % 2 != 0]
    evenArr = [x for x in array if x % 2 == 0]
    return (oddArr, evenArr)


arr = list(map(int, input().split()))
odd, even = getOddEvenArray(arr)
print(odd, even)


# Using list comprehension with if-else
def getOddEvenArray(array):
    oddArr = []
    evenArr = []
    [oddArr.append(x) if x % 2 != 0 else evenArr.append(x) for x in array]
    return (oddArr, evenArr)


arr = list(map(int, input().split()))
odd, even = getOddEvenArray(arr)
print(odd, even)


# Using filter and lambda
def getOddEvenArray(array):
    oddArr = list(filter(lambda x: x % 2 != 0, array))
    evenArr = list(filter(lambda x: x % 2 == 0, array))
    return (oddArr, evenArr)


arr = list(map(int, input().split()))
odd, even = getOddEvenArray(arr)
print(odd, even)
