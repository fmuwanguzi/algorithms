#divides the array until it only has 2 indexes
#compare 2 arrays 
# sorts the different arrays and adds them together as they merge


#whieboarding did not work for me
def mergeSort(myList):
    if len(myList) > 1:
        mid = len(myList) // 2
        left = myList[:mid]
        right = myList[mid:]

        # Recursive call on each half
        mergeSort(left)
        mergeSort(right)

        # Two iterators for traversing the two halves
        i = 0
        j = 0
        
        # Iterator for the main list
        k = 0
        
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
              # The value from the left half has been used
              myList[k] = left[i]
              # Move the iterator forward
              i += 1
            else:
                myList[k] = right[j]
                j += 1
            # Move to the next slot
            k += 1

        # For all the remaining values
        while i < len(left):
            myList[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            myList[k]=right[j]
            j += 1
            k += 1

myList = [54,26,93,17,77,31,44,55,20]
mergeSort(myList)
print(myList)

# class solution 
# #merge

def merge(arr1, arr2):
    output= []
    start_length_arr1 = len(arr1)
    start_length_arr2 = len(arr2)
    target_output_length = start_length_arr1 + start_length_arr2
    
    while len(output) < target_output_length:
        print('--------------')
        print('arr1', arr1)
        print('arr2', arr2)
        print('output',output)
        
        if len(arr1) == 0:
            output += arr2
            arr2 = []
        elif len(arr2) == 0:
            output += arr1
            arr1 = []
        elif arr1[0] < arr2[0]:
            output.append(arr1[0])
            arr1 = arr1[1:] #only the 1 index and everything on the right no 0 index
        else:
            output.append(arr2[0])
            arr2 = arr2[1:]
    return output

print(merge([2], [4]))
print(merge([4], [2]))

#splt

def split(arr):
    print('splitting', arr)
    midpoint = len(arr) // 2
    arr1 = arr[:midpoint]
    arr2 = arr[midpoint:]
    
#basecase

    if len(arr1) <= 1 and len(arr2) <=1:
        return merge(arr1, arr2)
    
    split_arr1 = split(arr1)
    split_arr2 = split(arr2)
    return merge(split_arr1, split_arr2)

print(split([54,26,93,17,77,31,44,55,20]))