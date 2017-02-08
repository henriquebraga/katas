# not multiple: return own number
#multiple of 3: return fizz
#multiple of 5: return buzz
from functools import partial
multiple_of = lambda base, num : num % base == 0
multiple_of_3 = partial(multiple_of, 3)
multiple_of_5 = partial(multiple_of, 5)

def robot(pos):

    say = str(pos)

    if multiple_of_3(pos):
        say = 'fizz'

    if multiple_of_5(pos):
        say = 'buzz'

    if multiple_of_3(pos) and multiple_of_5(pos):
        say = 'fizzbuzz'

    return say

#Tests
assert all(robot(pos) == 'fizz' for pos in (3, 6, 9))
assert all(robot(pos) == 'buzz' for pos in (5, 10, 20))
assert all(robot(pos) == 'fizzbuzz' for pos in (15, 30, 45))



