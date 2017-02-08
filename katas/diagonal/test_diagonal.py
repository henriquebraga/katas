from unittest import TestCase

from katas.diagonal.matrix import Matrix


class DefaultMatrixTest(TestCase):
    '''Tests for matrix basic operations (no parameters are passed when initialized)'''

    def setUp(self):
        self.matrix = Matrix()

    def test_matrix_has_a_constructor(self):
        self.assertTrue(getattr(self.matrix, '__init__'))

    def test_matrix_should_be_iterable(self):
        self.assertTrue(getattr(self.matrix, '__iter__'))

    def test_all_matrix_lines_should_have_three_elements(self):
        self.assertTrue(all(len(n) == 3 for n in self.matrix))

    def test_matrix_should_have_nine_elements(self):
        total = sum(len(line) for line in self.matrix)
        self.assertEquals(9, total)

    def test_when_matrix_is_initialize_without_parameters_should_be_1_to_9(self): #noqa
        expected = [[1,2,3],[4,5,6],[7,8,9]]
        self.assertSequenceEqual(expected, self.matrix.elements)

    def test_primary_diagonal_sum_should_be_15(self):
        self.assertEqual(15, self.matrix.primary_diagonal_sum())

    def test_secondary_diagonal_sum_should_be_15(self):
        self.assertEqual(15, self.matrix.secondary_diagonal_sum())

    def test_primary_diagonal_sum_should_be_9_when_value_is_modified(self):
        # 2 2 3
        # 4 3 5
        # 7 8 5
        self.change_primary_diagonal_values()
        self.assertEqual(10, self.matrix.primary_diagonal_sum())

    def test_secondary_diagonal_sum_should_be_9_when_values_are_modified(self): #noqa
        self.change_secondary_diagonal_values()
        self.assertEqual(9, self.matrix.secondary_diagonal_sum())

    def test_difference_between_diagonals_should_be_zero(self):
        self.assertEqual(0, self.matrix.diagonal_difference())

    def testt_difference_between_diagonals_should_be_3_when_primary_values_are_modified(self): #noqa
        # 2 2 3
        # 4 3 5
        # 7 8 5
        self.change_primary_diagonal_values()
        self.assertEqual(3, self.matrix.diagonal_difference())

    def test_difference_between_diagonals_should_be_4_when_secondary_values_are_modified(self): #noqa
        # 1 2 1
        # 4 3 6
        # 5 8 9
        self.change_secondary_diagonal_values()
        self.assertEqual(4, self.matrix.diagonal_difference())

    def change_primary_diagonal_values(self):
        self.matrix.elements[0][0] = 2
        self.matrix.elements[1][1] = 3
        self.matrix.elements[2][2] = 5

    def change_secondary_diagonal_values(self):
        self.matrix.elements[0][2] = 1
        self.matrix.elements[1][1] = 3
        self.matrix.elements[2][0] = 5


class MatrixInitializedWithNoDefaultValuesTest(TestCase):
    '''Test cases for a matrix when is not initialized passing elements.'''

    def setUp(self):
        self.matrix = Matrix(elements=[(11, 2, 4), (4, 5, 6), (10, 8, -12)])

    def test_primary_diagonal_sum_should_be_4(self):
        self.assertEquals(4, self.matrix.primary_diagonal_sum())

    def test_secondary_diagonal_sum_should_be_15(self):
        self.assertEquals(19, self.matrix.secondary_diagonal_sum())

    def test_difference_between_diagonals_should_be_4(self): #noqa
        self.assertEqual(15, self.matrix.diagonal_difference())


class Matrix4x4Test(TestCase):
    '''Test cases for a 4x4 Matrix.'''

    def setUp(self):
        self.matrix = Matrix(
            elements=[
                (1,2,3,4),
                (5,6,7,8),
                (9,10,11,12),
                (13,14,15,16)
            ]
        )

    def test_all_matrix_lines_should_have_four_elements(self):
        self.assertTrue(all(len(n) == 4 for n in self.matrix))

    def test_matrix_should_have_sixteen_elements(self):
        total = sum(len(line) for line in self.matrix)
        self.assertEquals(16, total)

    def test_primary_diagonal_sum_should_be_34(self):
        self.assertEqual(34, self.matrix.primary_diagonal_sum())

    def test_secondary_diagonal_sum_should_be_34(self):
        self.assertEqual(34, self.matrix.secondary_diagonal_sum())

    def test_difference_between_diagonals_should_be_0(self):
        self.assertEqual(0, self.matrix.diagonal_difference())


