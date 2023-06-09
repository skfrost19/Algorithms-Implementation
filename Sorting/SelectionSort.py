from typing import List
import unittest


def selection_sort(arr: List) -> List:
    size = len(arr) - 1
    for i in range(size):
        max_idx = 0
        for j in range(size - i + 1):
            if arr[j] > arr[max_idx]:
                max_idx = j

        arr[size - i], arr[max_idx] = arr[max_idx], arr[size - i]
    return arr


class SelectionSortTest(unittest.TestCase):
    def test_selection_sort(self):
        self.assertEqual(selection_sort([1, 2, 3, 4]), [1, 2, 3, 4])
        self.assertEqual(selection_sort([12, 22, 3, 42]), [3, 12, 22, 42])
        self.assertEqual(selection_sort([]), [])
        self.assertEqual(selection_sort([1, -2, 3, -4]), [-4, -2, 1, 3])


if __name__ == "__main__":
    unittest.main()
