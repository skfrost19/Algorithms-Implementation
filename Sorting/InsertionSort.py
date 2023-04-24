from typing import List
import unittest

def insertion_sort(arr: List) -> List:
    n = len(arr)
    for i in range(1, n):
        j = i-1
        while (j >= 0 and arr[j] > arr[i]):
            j -= 1
        temp_val = arr[i]
        arr.pop(i)
        arr.insert(j+1, temp_val)
    
    return arr

class InsertionSortTest(unittest.TestCase):
    def test_insertion_sort(self):
        self.assertEqual(insertion_sort([1,2,6,-1,0]), [-1,0,1,2,6])
        self.assertEqual(insertion_sort([12, 22, 3, 42]), [3, 12, 22, 42])
        self.assertEqual(insertion_sort([]), [])
        self.assertEqual(insertion_sort([1, -2, 3, -4]), [-4, -2, 1, 3])

if __name__ == "__main__":
    unittest.main()