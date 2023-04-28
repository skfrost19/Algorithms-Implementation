from typing import List
import unittest

def merge(arr1: List, arr2: List) -> List:
    itr1 = 0
    itr2 = 0
    m,n = len(arr1), len(arr2)
    final_arr = []
    while (itr1 != m and itr2 != n):
        if arr1[itr1] < arr2[itr2]:
            final_arr.append(arr1[itr1])
            itr1 += 1
        elif arr1[itr1] > arr2[itr2]:
            final_arr.append(arr2[itr2])
            itr2 += 1
        else:
            final_arr.append(arr1[itr1])
            final_arr.append(arr2[itr2])
            itr1 += 1
            itr2 += 1
    while (itr1 < m):
        final_arr.append(arr1[itr1])
        itr1 += 1
    while (itr2 < n):
        final_arr.append(arr2[itr2])
        itr2 += 1
    return final_arr

def merge_sort(arr: List, m: int, n: int) -> List:
    if m == n:
        return arr
    mid = (m+n)// 2
    left_arr = merge_sort(arr[0: mid+1], 0, mid)
    right_arr = merge_sort(arr[mid+1: ], mid+1, n)
    return merge(left_arr, right_arr)

class MergeSort(unittest.TestCase):
    def test_merge_sort(self):
        self.assertEqual(merge_sort([1,2,6,-1,0], 0, 4), [-1,0,1,2,6])
        self.assertEqual(merge_sort([12, 22, 3, 42], 0, 3), [3, 12, 22, 42])
        self.assertEqual(merge_sort([], 0, 0), [])
        self.assertEqual(merge_sort([1, -2, 3, -4], 0, 3), [-4, -2, 1, 3])

if __name__ == "__main__":
    unittest.main()