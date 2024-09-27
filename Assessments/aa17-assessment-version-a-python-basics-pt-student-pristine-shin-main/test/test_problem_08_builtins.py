from inspect import getsourcelines
from random import randint
import re
import unittest


class TestSquareLists(unittest.TestCase):
    def test_square_lists_works_on_empty_list(self):
        from problem_08_builtins import square_lists

        result = square_lists([])

        self.assertEqual(result, [])

    def test_square_lists_actually_squares_lists(self):
        from problem_08_builtins import square_lists
        lst = []
        expected = []
        for _ in range(0, 100):
            sublst = [randint(0, 10) for _ in range(randint(0, 10))]
            lst.append(sublst)
            expected.append([x**2 for x in sublst])

        result = square_lists(lst)

        self.assertListEqual(result, expected)

    def test_appears_to_use_map_function(self):
        from problem_08_builtins import square_lists
        map_re = re.compile("map")
        strip_comments = re.compile("#.*")
        lines = getsourcelines(square_lists)[0][1:]
        lines = [strip_comments.sub("", line).strip()
                 for line in lines]
        lines = [line for line in lines if map_re.findall(line)]
        self.assertGreaterEqual(len(lines), 1)
