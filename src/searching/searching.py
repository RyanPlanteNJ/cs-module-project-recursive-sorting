# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    # Your code here
    if len(arr) == 0:
        return -1
    middle_int = (start + end) // 2
    if target == arr[middle_int]:
        return middle_int
    else:
        if target <= arr[middle_int]:
            end = middle_int - 1
        if target > arr[middle_int]:
            start = middle_int + 1
    return binary_search(arr, target, start, end)




# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively
# or iteratively
def agnostic_binary_search(arr, target):
    # Your code here
    pass
