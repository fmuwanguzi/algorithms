#while arr is not fully sorted 
# first compare the two neighboring elements
# i and i + 1
# if they are backwards, swap them

def is_sorted(arr):
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False
        
    return True

def bubble_sort(arr):
    while not is_sorted(arr):
        for i in range(len(arr) - 1):
            if arr[i] > arr [ i + 1 ]:
                arr[i], arr[i +1] = arr [ i + 1], arr[i]
    
    return arr

print(bubble_sort([ 1, 4, 6, 3, 9]))
    