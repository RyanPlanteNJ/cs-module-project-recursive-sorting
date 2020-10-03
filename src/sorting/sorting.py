# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge_1(arrA, arrB, merged = []):
    # elements = len(arrA) + len(arrB)
    # merged_arr = [0] * elements
    # Your code here
    merged_arr = merged
    current = 0
    if len(arrA) == 0:
        merged_arr.append(arrB[0:])
        return merged_arr
    elif len(arrB) == 0:
        merged_arr.append(arrA[0:])
        return merged_arr
    if arrA[current] <= arrB[current]:
        merged_arr.append(arrA[current])
        return merge(arrA[current+1:], merged_arr)
    else:
        merged_arr.append(arrB[current])
        return merge(arrB[current+1], merged_arr)

def merge(arrA, arrB):
    return arrA + arrB


# TO-DO: implement the Merge Sort function below recursively

def partition(arr):
    left = []
    right = []
    pivot = arr[0]

    for value in arr[1:]:
        if value <= pivot:
            left.append(value)
        else:
            right.append(value)
    return left, pivot, right

def merge_sort(arr):
    # Your code here
    if arr == []:
        return arr
    left, pivot, right = partition(arr)
    return merge_sort(left) + [pivot] + merge_sort(right)

# STRETCH: implement the recursive logic for merge sort in a way that doesn't
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists
# or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr, start, mid, end):
    # Your code here
    pass


def merge_sort_in_place(arr, l, r):
    # Your code here
    pass
