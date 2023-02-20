# using naive approach
def avgOfArr(array):
    sums = 0
    length = 0
    for i in range((len(array))):
        sums += array[i]
        length += 1
    return sums/length


arr = list(map(int, input().split()))
average = avgOfArr(arr)
print(average)


# With built-in function named sum and len
def avgOfArr(array):
    return sum(array)/len(array)


arr = list(map(int, input().split()))
average = avgOfArr(arr)
print(average)
