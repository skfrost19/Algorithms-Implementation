from typing import List
import unittest

def binary_search(arr: List, ele):
    """
    Params: List of sorted elements, element to be searched
    Return: index of found element, None otherwise
    """
    low , high = 0, len(arr)-1
    while low <= high:
        mid = (low+high)//2
        if arr[mid] == ele:
            return mid
        if arr[mid] < ele:
            low = mid+1
        else:
            high = mid-1
    return None


# Unittest
class TestBinarySearch(unittest.TestCase):
    def test_binary_search(self):
        self.assertEqual(binary_search([1,2,3,45], 2), 1)
        self.assertEqual(binary_search([1,28,30,45,76], 2), None)
        self.assertEqual(binary_search([1,2,3,45], -21), None)
        self.assertEqual(binary_search([], 2), None)


if __name__ == "__main__":
    unittest.main()



    