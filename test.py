import unittest

from dequeue import Dequeue


class MyTestCase(unittest.TestCase):
    def test_dequeue(self):
        dequeue = Dequeue()
        dequeue.push(1)
        dequeue.push(2)
        dequeue.push(3)
        dequeue.push(4)
        self.assertEqual(1, dequeue.pop())
        self.assertEqual(4, dequeue.leftpop())
        self.assertEqual(2, dequeue.pop())
        self.assertEqual(3, dequeue.leftpop())


if __name__ == '__main__':
    unittest.main()
