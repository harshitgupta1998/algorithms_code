def count_sort(input_array):
    M=max(input_array)
    count_array=[0]*(M+1)
    # counter of values
    for i in input_array:
        count_array[i]+=1
    # running sum
    for i in range(1,M+1):
        count_array[i]+=count_array[i-1]
    output_array=[0]*len(input_array)
    for i in range(len(input_array)-1,-1,-1):
        output_array[count_array[input_array[i]]-1]=input_array[i]
        count_array[input_array[i]]-=1
    return output_array
# Driver code
if __name__ == "__main__":
    # Input array
    input_array = [4, 3, 12, 1, 5, 5, 3, 9]

    # Output array
    output_array = count_sort(input_array)

    for num in output_array:
        print(num, end=" ")