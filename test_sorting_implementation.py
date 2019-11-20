import unittest
from sorting_implementations import *

class MyTestCase(unittest.TestCase):
    def test_sorting(self):
        """
        Testing for sortin algorithms: Quick Sort, Merge Sort, Bubble Sort, Selection Sort, Insertion Sort
        :return: None
        """
        numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]
        numbers2 = [7, 2, 3, 1, 5, 6, 8]
        numbers3 = [3, 2, 0, 1]
        # Merge Sort
        self.assertEqual(str(merge_sorter(numbers)), '[0, 1, 2, 4, 5, 6, 44, 63, 87, 99, 283]')
        self.assertEqual(str(merge_sorter(numbers2)), '[1, 2, 3, 5, 6, 7, 8]')
        self.assertEqual(str(merge_sorter(numbers3)), '[0, 1, 2, 3]')
        # Quick Sort
        self.assertEqual(str(quick_sorter(numbers)), '[0, 1, 2, 4, 5, 6, 44, 63, 87, 99, 283]')
        self.assertEqual(str(quick_sorter(numbers2)), '[1, 2, 3, 5, 6, 7, 8]')
        self.assertEqual(str(quick_sorter(numbers3)), '[0, 1, 2, 3]')
        # Bubble Sort
        self.assertEqual(str(bubble_sort(numbers)), '[0, 1, 2, 4, 5, 6, 44, 63, 87, 99, 283]')
        self.assertEqual(str(bubble_sort(numbers2)), '[1, 2, 3, 5, 6, 7, 8]')
        self.assertEqual(str(bubble_sort(numbers3)), '[0, 1, 2, 3]')
        # Selection Sort
        self.assertEqual(str(selection_sort(numbers)), '[0, 1, 2, 4, 5, 6, 44, 63, 87, 99, 283]')
        self.assertEqual(str(selection_sort(numbers2)), '[1, 2, 3, 5, 6, 7, 8]')
        self.assertEqual(str(selection_sort(numbers3)), '[0, 1, 2, 3]')
        # Insertion Sort
        self.assertEqual(str(insertion_sort(numbers)), '[0, 1, 2, 4, 5, 6, 44, 63, 87, 99, 283]')
        self.assertEqual(str(insertion_sort(numbers2)), '[1, 2, 3, 5, 6, 7, 8]')
        self.assertEqual(str(insertion_sort(numbers3)), '[0, 1, 2, 3]')





if __name__ == '__main__':
    unittest.main()
