# Checks if array is sorted

def issorted(l):
    return all(l[i] <= l[i+1] for i in range(len(l)-1))

# Bubble sort O(n^2) average and worst case. Memory O(1)
# Swaps 
# You can optimise this by observing that the nth pass puts the nth element into place 
# The nested loops show that it is O(n^2)

def bubblesort(arr):
    swapped = True
    n = len(arr)
    while swapped:
        swapped = False
        for i in range(1, n):
            if arr[i-1] > arr[i]:
                arr[i-1], arr[i] = arr[i], arr[i-1]
                swapped = True
        n -= 1
    return arr

# Selection sort O(n^2) average and worst case. Memory O(1)
# Linear search to find the smallest element and swap it with the front of the array. Then find the second smallest... etc.
# Heapsort is an improved version of selection sort

def selectionsort(arr):
    for j in range(len(arr)-1):
        # Assume first element is minimum
        imin = j
        for i in range(j, len(arr)):
            if arr[i] < arr[imin]:
                imin = i
        if imin != j:
            arr[imin], arr[j] = arr[j], arr[imin]

    return arr

# Merge sort O(nlog(n)) avergae and worst case. Memory: O(n)
# Sorts the two halves and merges then back together
# The actual sort happens during the merge
# The memory is O(n) becuase of the copying that happens

def mergesort(arr):
    if len(arr)>1:
        mid = len(arr)//2
        lefthalf = arr[:mid]
        righthalf = arr[mid:]

        mergesort(lefthalf)
        mergesort(righthalf)

        # Now merge
        i = j = k = 0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                arr[k] = lefthalf[i]
                i += 1
            else: 
                arr[k] = righthalf[j]
                j += 1

            k += 1

        # Finished left
        while i < len(lefthalf):
            arr[k] = lefthalf[i]
            i += 1
            k += 1
        
        # Finish right
        while j < len(righthalf):
            arr[k] = righthalf[j]
            j += 1
            k += 1

        return arr

# Quicksort O(nlog(n)) avergage, O(n^2) worst case. Memory O(log(n))
# Pick a pivot element, and partition it such that all numbers < pivot are left of it, and > pivot are right of it
# However, depending on the value of the pivot the sorting could be very slow because it could be nowhere near the median.
# This is why the worst case is O(n^2)

def quicksort(arr, left, right):
    if left < right:
        index = partition(arr, left, right)
        # Sort left half
        if left < index - 1:
            quicksort(arr, left, index - 1)
        # Sort right half
        if index < right:
            quicksort(arr, index, right)

    return arr
    
def partition(arr, left, right):
    # This is called the Hoare partitioning scheme
    # Use two indicies that start at the ends of the array being partitioned that move towards each other until they detect an inversion
    # The inverted elements are then swapped
    # When the indicies meet the algorithm stops and returns the final index
    # The algorithm guarantees lo <= p < hi which implies both resulting partitions are nonempty, hence there is no risk of infinite recursion

    # Pick some pivot point
    pivot = arr[left]
    
    while left <= right:
        # Find element on the left that should be on the right
        while arr[left] < pivot:
            left += 1

        # Find element on the right that should be on the left
        while arr[right] > pivot:
            right -= 1

        # Swap elements and move left and right indicies
        if left <= right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1

    return left

# Radix sort O(kn) 
# Takes advantage of the fact that integers have a finite number of bits
# We iterate through each digit of the number and group number by each digit
# Comparision sorting algorithms cannot do better than O(nlog(n))
# But radix has a runtime of O(kn) where n is the number of elements and k is the number of passes of the sorting algorithm

# Binary search

def binarysearch(a, x):
    assert issorted(a)
    low = 0
    high = len(a)-1
    
    while low <= high:
        mid = (low + high)//2

        if a[mid] == x:
            return mid
        elif a[mid] > x:
            # REMEBER THE +1 and -1s !!
            high = mid - 1
        elif a[mid] < x:
            low = mid + 1

    raise LookupError("Element not found!")

def binarysearchrecursive(a, x):
    # Pre: array must be sorted
    assert issorted(a)
    return binarysearchhelper(a, x, 0, len(a)-1)

def binarysearchhelper(a, x, low, high):
    if low > high:
        raise LookupError("Element not found!")

    mid = (low + high)//2

    if a[mid] == x:
        return mid
    elif a[mid] > x:
        # Remeber these +1, -1s because you don't want to repeat mid
        return binarysearchhelper(a, x, low, mid-1)
    elif a[mid] < x:
        return binarysearchhelper(a, x, mid+1, high)




if __name__ == "__main__":
    arr = [5, 1, 2, 6, 3, 19, -300, 59, 3]
    print(arr)
    sarr = bubblesort(arr)
    print(sarr)
    assert issorted(sarr)
    arr = [5, 1, 2, 6, 3, 19, -300, 59, 3]
    sarr = selectionsort(arr)
    print(sarr)
    assert issorted(sarr)
    arr = [5, 1, 2, 6, 3, 19, -300, 59, 3]
    sarr = mergesort(arr)
    print(sarr)
    assert issorted(sarr)
    arr = [5, 1, 2, 6, 3, 19, -300, 59, 3]
    sarr = quicksort(arr, 0, len(arr)-1)
    print(sarr)
    assert issorted(sarr)
    index = binarysearchrecursive(sarr, -300)
    print(index)

    try:
        binarysearchrecursive(sarr, 32132)
    except Exception as e:
        print(e)
    index = binarysearchrecursive(sarr, -300)
    print(index)

    index = binarysearch(sarr, 19)
    print(index)

    try:
        binarysearch(sarr, 32132)
    except Exception as e:
        print(e)
