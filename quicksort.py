def partition(arr,l,h):
    pivot=arr[h]
    i=l-1
    for j in range(l,h):
        if arr[j]<pivot:
            i+=1
            swap(arr,i,j)
    swap(arr,i+1,h)
    # return the new pivot
    return i+1


def quicksort(arr,l,h):
    if l<h: # stopping condition
        p=partition(arr,l,h)
        quicksort(arr,l,p-1)
        quicksort(arr,p+1,h)

def swap(arr,i,j):
    arr[i],arr[j]=arr[j],arr[i]




if __name__ == "__main__":
    arr = [10, 7, 8, 9, 1, 5]
    n = len(arr)
    quicksort(arr, 0, n - 1)
    for val in arr:
        print(val, end=" ")