from unittest import TestCase

from katas.diagonal.matrix import Matrix


class MatrixTest(TestCase):

    def setUp(self):
        self.matrix = Matrix()

    def test_matrix_has_a_constructor(self):
        self.assertTrue(getattr(self.matrix, '__init__'))

    def test_matrix_should_be_iterable(self):
        self.assertTrue(getattr(self.matrix, '__iter__'))

    def test_all_lines_should_have_three_elements(self):
        self.assertTrue(all(len(n) == 3 for n in self.matrix))

    def test_matrix_should_have_nine_elements(self):
        total = sum(len(line) for line in self.matrix)
        self.assertEquals(9, total)

    def test_when_matrix_is_initialize_without_parameters_should_be_1_to_9(self): #noqa
        expected = [[1,2,3],[4,5,6],[7,8,9]]
        self.assertSequenceEqual(expected, self.matrix.elements)

    def test_left_diagonal_sum_should_be_15(self):
        self.assertEqual(15, self.matrix.left_diagonal_sum())

    def test_right_diagonal_sum_should_be_15(self):
        self.assertEqual(15, self.matrix.right_diagonal_sum())

    def test_left_diagonal_sum_should_be_9_when_value_is_modified(self):
        # 2 2 3
        # 4 3 5
        # 7 8 5
        self.change_left_diagonal_values()
        self.assertEqual(10, self.matrix.left_diagonal_sum())

    def test_right_diagonal_sum_should_be_9_when_value_is_modified(self):
        self.change_right_diagonal_values()
        self.assertEqual(9, self.matrix.right_diagonal_sum())

    def test_diagonal_difference_should_be_zero(self):
        self.assertEqual(0, self.matrix.diagonal_difference())

    def test_diagonal_difference_should_be_3_when_left_diagonal_values_are_modified(self): #noqa
        # 2 2 3
        # 4 3 5
        # 7 8 5
        self.change_left_diagonal_values()
        self.assertEqual(3, self.matrix.diagonal_difference())

    def test_diagonal_difference_should_be_4_when_right_diagonal_values_are_modified(self): #noqa
        # 1 2 1
        # 4 3 6
        # 5 8 9
        self.change_right_diagonal_values()
        self.assertEqual(4, self.matrix.diagonal_difference())

    def change_left_diagonal_values(self):
        self.matrix.elements[0][0] = 2
        self.matrix.elements[1][1] = 3
        self.matrix.elements[2][2] = 5

    def change_right_diagonal_values(self):
        self.matrix.elements[0][2] = 1
        self.matrix.elements[1][1] = 3
        self.matrix.elements[2][0] = 5

