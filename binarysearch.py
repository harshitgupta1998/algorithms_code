def binarySearch(arr,low,high,val):
    while (low<=high):
        mid=low+(high-low//2)
        print(mid)
        if arr[mid]==val:
            return mid
        elif arr[mid]>val:
            high=mid-1
        else:
            low=mid+1
    return -1

if __name__ == '__main__':
    arr = [2, 3, 4, 10, 40]
    x = 3
    # Function call
    result = binarySearch(arr, 0, len(arr)-1, x)
    if result != -1:
        print("Element is present at index", result)
    else:
        print("Element is not present in array")