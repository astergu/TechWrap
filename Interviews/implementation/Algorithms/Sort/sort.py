import unittest


def selection_sort(items):
    for i in range(len(items)):
        curr_min = i
        for j in range(i + 1, len(items)):
            if items[j] < items[curr_min]:
                items[j], items[curr_min] = items[curr_min], items[j]

def insertion_sort(items):
    for i in range(len(items)):
        for j in range(i, 0, -1):
            if items[j] < items[j - 1]:
                items[j], items[j - 1] = items[j - 1], items[j]


class TestSorting(unittest.TestCase):
    def test_select_sort(self):
        items = [5, 2, 6, 1, 7, 8, 9, 4, 3]
        answer = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        selection_sort(items)
        self.assertEqual(items, answer)

    def test_insertion_sort(self):
        items = [5, 2, 6, 1, 7, 8, 9, 4, 3]
        answer = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        insertion_sort(items)
        self.assertEqual(items, answer)


if __name__ == '__main__':
    unittest.main()