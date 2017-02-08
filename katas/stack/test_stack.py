from unittest import TestCase
from katas.stack.stack import BoundedStack, UnderFlowError, NegativeCapacityError, OverFlowError


class TestStack(TestCase):

    def setUp(self):
        self.stack = BoundedStack.make(2)

    def test_stack_should_be_empty_when_created(self):
        self.assertTrue(self.stack.is_empty())

    def test_stack_should_has_no_elements_when_created(self):
        self.assertEqual(0, len(self.stack))

    def test_stack_should_not_be_empty_after_push(self):
        self.stack.push(1)
        self.assertFalse(self.stack.is_empty())

    def test_stack_should_be_one_after_push(self):
        self.stack.push(1)
        self.assertEquals(1, len(self.stack))

    def test_stack_should_be_empty_after_push_and_pop(self):
        self.stack.push(1)
        self.stack.pop()
        self.assertTrue(self.stack.is_empty())

    def test_when_one_is_pushed_and_popped_should_be_one(self):
        self.stack.push(1)
        self.assertEquals(1, self.stack.pop())

    def test_when_one_and_two_are_pushed_two_and_one_are_popped(self):
        [self.stack.push(n) for n in range(1, 3)]
        nums = [self.stack.pop() for n in range(2)]
        self.assertSequenceEqual([2, 1], nums)

    def test_when_one_is_pushed_one_is_on_top(self):
        self.stack.push(1)
        self.assertEqual(1, self.stack.top())

    def test_when_one_and_two_are_pushed_two_is_on_top(self):
        self.stack.push(1)
        self.stack.push(2)
        self.assertEqual(2, self.stack.top())

    def test_when_push_past_limit_stack_should_overflows(self):
        with self.assertRaises(OverFlowError):
            [self.stack.push(1) for n in range(3)]

    def test_when_pop_with_no_elements_should_raise(self):
        with self.assertRaises(UnderFlowError):
            self.stack.pop()

    def test_when_create_a_stack_with_negative_size_should_raise_error(
       self):
        with self.assertRaises(NegativeCapacityError):
            BoundedStack.make(-10)

    def test_when_create_stack_with_zero_capacity_any_push_should_overflows(
       self):
        self.stack = BoundedStack.make(0)
        with self.assertRaises(OverFlowError):
            self.stack.push(2)

    def test_when_stack_is_empty_top_should_be_none(self):
        self.assertEqual(None, self.stack.top())

    def test_when_stack_has_one_and_two_should_find_one(self):
        self.stack.push(1)
        self.stack.push(2)
        self.assertEqual(1, self.stack.find(1))





