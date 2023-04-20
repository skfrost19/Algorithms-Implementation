from typing import List
import unittest


def linear_search(arr : List, ele):
    """
    Params: List of elements, elements_to_be_searched
    Returns: index of element present, None otherwise

    """

    for idx, element in enumerate(arr):
        if element == ele:
            return idx
    
    return None


# Test Cases
class TestLinearSearch(unittest.TestCase):
    def test_linear_search(self):
        self.assertEqual(linear_search([1, 2, 3, 4, 5], 3), 2)
        self.assertEqual(linear_search([1, 2, 3, 4, 5], 7), None)
        self.assertEqual(linear_search([1, 2, 3, 4, 5], 1), 0)
        self.assertEqual(linear_search([1, 2, 3, 4, 5], 5), 4)
        self.assertEqual(linear_search([1, 2, 3, 4, 5], 0), None)
        self.assertEqual(linear_search([], 6), None)
    


if __name__ == "__main__":
    unittest.main()