def avgElement(arr):
    avg = 0
    for i in range(0,len(arr)):
        avg = avg + arr[i]
    return avg / len(arr)