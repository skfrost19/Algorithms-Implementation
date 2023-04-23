from typing import List
import unittest


def bubble_sort(arr: List) -> List:
    size = len(arr)
    for i in range(size):
        for j in range(i, size):
            if arr[j] < arr[i]:
                arr[j], arr[i] = arr[i], arr[j]  # swap

    return arr


class BuubleSortTest(unittest.TestCase):
    def test_bubble_sort(self):
        self.assertEqual(bubble_sort([1, 2, 3, 4]), [1, 2, 3, 4])
        self.assertEqual(bubble_sort([12, 22, 3, 42]), [3, 12, 22, 42])
        self.assertEqual(bubble_sort([]), [])
        self.assertEqual(bubble_sort([1, -2, 3, -4]), [-4, -2, 1, 3])


if __name__ == "__main__":
    unittest.main()
