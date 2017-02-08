class Matrix:

    def __init__(self, elements=None):
        self.elements = elements or ([1, 2, 3], [4, 5, 6], [7, 8, 9])


    def left_diagonal_sum(self):
        return sum(element for line_no, line in enumerate(self)
                   for element_no, element in enumerate(line)
                   if line_no == element_no)

    def right_diagonal_sum(self):
        return sum(element for line_no, line in enumerate(self)
                   for element_no, element in enumerate(line)
                   if line_no + element_no == 2)

    def diagonal_difference(self):
        return abs(self.left_diagonal_sum() - self.right_diagonal_sum())

    def __iter__(self):
        return iter(self.elements)




