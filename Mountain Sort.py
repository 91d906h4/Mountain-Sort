"""
Mountain Sort

Best Case: O(n)
Average Case: O(n^2)
Worst Case: O(n^2)

Method: Merging

Approach:
    In one scan, we select and index some numbers
    from left to right and from right to left once.

Remarks:
    2023/03/23 I it came to my mind, and I thought
    I was the "father" of this algorithm, I named
    it the "Mountain Sort" because the best-case
    of behavious of this algorithm is like a mou-
    ntain.

    This is the first algorithm I figured out by
    myself, although it had been publish at 2018,
    for me, it still means a lot to me.

    https://en.wikipedia.org/wiki/Strand_sort
"""

def merge(arr1: list, arr2: list) -> list:
    l1, l2 = len(arr1), len(arr2)
    p1, p2 = 0, 0
    result = []
    
    while p1 < l1 and p2 < l2:
        if arr1[p1] < arr2[p2]:
            result.append(arr1[p1])
            p1 += 1
        else:
            result.append(arr2[p2])
            p2 += 1
    
    result = result + arr1[p1:] + arr2[p2:]

    return result

def mountainSort(array: list) -> list:
    length = len(array) # Get the length of array.
    counter = 0 # Check how many elements are found. If all elements are found, then return the result.
    result = [] # The result of sorted array.
    recorder = {} # Check if element is found.

    while counter < length:
        left, l = [], float("-inf")
        right, r = [], float("-inf")

        for i in range(length):
            if i not in recorder and array[i] > l:
                l = array[i]
                left.append(l)
                recorder[i] = 1
                counter += 1

            if length - i - 1 not in recorder and array[length - i - 1] > r:
                r = array[length - i - 1]
                right.append(r)
                recorder[length - i - 1] = 1
                counter += 1

        result = merge(result, merge(left, right))
    
    return result