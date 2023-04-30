import unittest

def pivot(arr, i, j):
    th = i
    idx = i+1
    while i <= j:
        if arr[i] < arr[th]:
            arr[i],arr[idx] = arr[idx],arr[i]
            idx += 1
        i+=1
    arr[idx-1], arr[th] = arr[th], arr[idx-1]
    return idx


def quick_sort(arr, i, j):
    if i>=j:
        return arr

    pivot_idx = pivot(arr, i, j)
    quick_sort(arr, i, pivot_idx-1)
    quick_sort(arr, pivot_idx+1, j)

    return arr

class MergeSort(unittest.TestCase):
    def test_merge_sort(self):
        self.assertEqual(quick_sort([1,2,6,-1,0], 0, 4), [-1,0,1,2,6])
        self.assertEqual(quick_sort([12, 22, 3, 42], 0, 3), [3, 12, 22, 42])
        self.assertEqual(quick_sort([], 0, 0), [])
        self.assertEqual(quick_sort([1, -2, 3, -4], 0, 3), [-4, -2, 1, 3])

if __name__ == "__main__":
    unittest.main()