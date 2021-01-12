def search( arr, n):
    high = len(arr) - 1
    mid = 0
    low = 0
    
    while low <= high:
        #mid is the middlel of the array
        mid = (high + low) // 2 # rounds it to the lower value
        print('---middle of array',mid)
        #checking for the n at different portions of the array
        if arr[mid] < n:
            low = mid + 1
        elif arr[mid] > n:
            high = mid - 1
        else:
            return mid
    #if the element isn't in the array
    return print('not in the array', -1 )

#array must be sorted
lookthru = [5,6,8,9,13,14]
to_find = 15

print(search(lookthru, to_find))

#solution 2

def search2(arr, target, lost_index = 0):
  if len(arr) == 0:
    return -1
  mid_index = len(arr) // 2
  mid_value = arr[mid_index]
  left_half = arr[:mid_index]
  right_half = arr[mid_index + 1:]
  # print(mid_value)
  # print(left_half)
  # print(right_half)
  if mid_value == target:
    return mid_index + lost_index
  elif len(arr) == 1 and mid_value != target:
    return -1
  elif mid_value < target:
    return search2(right_half, target, mid_index + 1 + lost_index)
  elif mid_value > target:
    return search2(left_half, target, lost_index)
# print(search2([1,2,3,4,5,6,7,8,9], 5))
# print(search2([1,2,3,4,5,6,7,8,9], 3.5))
print(search2([1,2,3,4,5], 4))
  # find mid index
  # base case:
    # if you got very lucky and the mid value is the target value, return the mid index
    # OR: if the length of array is 1 and the element isn't the value, return -1
    # OR if the length of the array is 0, return -1
  # split the array into left and right halves
  # recur on whichever half of the array might contain the target value
