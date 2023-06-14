# This file is initialized with a code version of this
# question's sample test case. Feel free to add, edit,
# or remove test cases in this file as you see fit!

import program
import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        input = [1, 3, 3, 2, 4, 1, 5, 3, 2]
        expected = 9
        actual = program.largestRectangleUnderSkyline(input)
        self.assertEqual(actual, expected)

testProgram = TestProgram()
testProgram.test_case_1()