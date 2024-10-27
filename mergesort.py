def merger(arr,l,m,h):
    # use temp arrays to store the left and right subarray
    left = arr[l:m+1]
    right = arr[m+1:h+1]
    i=0
    j=0
    k=l
    # start updating arr based on the value from these sections
    while i<len(left) and j<len(right):
        if left[i]<=right[j]:
            arr[k]=left[i]
            i+=1
        else:
            arr[k]=right[j]
            j+=1
        k+=1

    
    while i<len(left):
        arr[k]=left[i]
        i+=1
        k+=1
    while j<len(right):
        arr[k]=right[j]
        j+=1
        k+=1
def merge_sort(arr,l, r):
    
    if l<r:
        m=(l+r)//2
        merge_sort(arr,l,m)
        merge_sort(arr,m+1,r)
        merger(arr,l,m,r)
    
def print_list(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()

# Driver code
if __name__ == "__main__":
    arr = [12, 11, 13, 5, 6, 7]
    print("Given array is")
    print_list(arr)

    merge_sort(arr, 0, len(arr) - 1)

    print("\nSorted array is")
    print_list(arr)