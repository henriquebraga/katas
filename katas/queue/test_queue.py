from unittest import TestCase
from katas.queue.queue import (
    Queue,
    OverFlowError,
    NegativeCapacityError,
    UnderFlowError
)



class TestQueue(TestCase):

    def setUp(self):
        self.queue = Queue.make(2)

    def test_when_creates_a_queue_should_be_empty(self):
        self.assertTrue(self.queue.is_empty())

    def test_when_creates_a_queue_should_have_no_elements(self):
        self.assertEquals(0, len(self.queue))
        
    def test_after_push_queue_should_not_be_empty(self):
        self.queue.push(1)
        self.assertFalse(self.queue.is_empty())

    def test_after_push_queue_should_have_one_element(self):
        self.queue.push(1)
        self.assertEquals(1, len(self.queue))

    def test_after_push_and_pop_a_queue_should_be_empty(self):
        self.queue.push(1)
        self.queue.pop()
        self.assertTrue(self.queue.is_empty())

    def test_after_push_one_queue_should_be_one_on_top(self):
        self.queue.push(1)
        self.assertEqual(1, self.queue.top())

    def test_after_push_two_and_one_queue_should_be_two_on_top(self):
        self.queue.push(2)
        self.queue.push(1)
        self.assertEqual(2, self.queue.top())

    def test_after_push_one_and_then_pop_should_be_one(self):
        self.queue.push(1)
        self.assertEqual(1, self.queue.pop())

    def test_after_push_two_and_one_and_then_pop_should_be_two(self):
        self.queue.push(2)
        self.queue.push(1)
        self.assertEqual(2, self.queue.pop())

    def test_when_push_more_than_capacity_should_raise_overflow(self):
        with self.assertRaises(OverFlowError):
            self.queue.push(1)
            self.queue.push(2)
            self.queue.push(3)

    def test_when_creates_queue_with_negative_capacity_should_raise_negative_capacity(
       self):
        with self.assertRaises(NegativeCapacityError):
            self.queue = Queue.make(-2)

    def test_when_pops_with_no_elements_should_raise_underflow(self):
        with self.assertRaises(UnderFlowError):
            self.queue.pop()

    def test_when_checks_on_top_of_the_queue_when_empty_should_raise_underflow(
       self):
        with self.assertRaises(UnderFlowError):
            self.queue.top()

























        