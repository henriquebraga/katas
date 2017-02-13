class Matrix:

    def __init__(self, elements=None):
        self.elements = elements or ([1, 2, 3], [4, 5, 6], [7, 8, 9])

    def primary_diagonal_sum(self):
        return sum(element for line_no, line in enumerate(self)
                   for element_no, element in enumerate(line)
                   if line_no == element_no)

    def secondary_diagonal_sum(self):
        return sum(element for line_no, line in enumerate(self)
                   for element_no, element in enumerate(line)
                   if line_no + element_no == len(line) - 1)

    def _traverse(self):
        return (element for line_no, line in enumerate(self)
                   for element_no, element in enumerate(line))

    def diagonal_difference(self):
        return abs(self.primary_diagonal_sum() - self.secondary_diagonal_sum())

    def __iter__(self):
        return iter(self.elements)



