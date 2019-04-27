import pytest
from typing import List

def binary_search_rec(arr, n):
    return binary_search_rec_aux(arr, n, 0, len(arr))


def binary_search_rec_aux(arr, n, low, high):
    if low >= high:
        return False
    mid = (high + low) // 2
    if n == arr[mid]:
        return True
    if n > arr[mid]:
        return binary_search_rec_aux(arr, n, mid+1, high)
    else:
        return binary_search_rec_aux(arr, n, low, mid)

def binary_search_it(arr, n):
    if len(arr) == 0:
        return False

    low = 0
    high = len(arr) 
    
    while low < high:
        mid = (low + high) // 2
        if arr[mid] == n:
            return True
        elif n < arr[mid]:
            high = mid
        else:
            low = mid + 1
    return False

def closest_number(arr: List[int], n: int) -> int:

    low = 0
    high = len(arr)

    if n <= arr[0]:
        return arr[0]
    elif n >= arr[-1]:
        return arr[-1]

    while low < high:
        mid = (low + high) // 2
        
        if arr[mid] == n:
            return n

        elif n < arr[mid]:
            # Search left

            if mid > 0 and n > arr[mid-1]:
                return get_closest(arr[mid-1], arr[mid], n)

            high = mid
        else:
            if mid < n-1 and n < arr[mid+1]:
                return get_closest(arr[mid+1], arr[mid], n)
            low = mid+1


    return arr[mid]

def get_closest(a, b, n):
    return a if abs(n - a) < abs(n-b) else b

class TestBinarySearch:
    def test_binary_search_rec_1(self):
        arr = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
        assert binary_search_rec(arr, 23) == True

    def test_binary_search_rec_2(self):
        arr = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
        assert binary_search_rec(arr, 4) == False

    def test_binary_search_rec_3(self):
        arr = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
        assert binary_search_rec(arr, -8) == False

    def test_binary_search_rec_4(self):
        arr = [-14, -7, -4, 0, 16, 23, 38, 56, 72, 91]
        assert binary_search_rec(arr, -7) == True

    def test_binary_search_it_1(self):
        arr = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
        assert binary_search_it(arr, 23)

    def test_binary_search_it_2(self):
        arr = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
        assert binary_search_it(arr, 4) == False

    def test_binary_search_it_3(self):
        arr = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
        assert binary_search_it(arr, -8) == False

    def test_binary_search_rec_5(self):
        arr = [-14, -7, -4, 0, 16, 23, 38, 56, 72, 91]
        assert binary_search_it(arr, -7) == True

    def test_closest_number_1(self):
        arr = [1, 2, 4, 5, 6, 6, 8, 9]
        assert closest_number(arr, 11) == 9

    def test_closest_number_2(self):
        arr = [2, 5, 6, 7, 8, 8, 9]
        assert closest_number(arr, 4) == 5
