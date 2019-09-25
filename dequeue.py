class Dequeue(object):

    def __init__(self):
        self.stack = []
        self.reversed_stack = []

    @staticmethod
    def _move(a, b):
        while len(a) > 0:
            b.append(a.pop())

    def push(self, obj):
        if not self.stack:
            self._move(self.reversed_stack, self.stack)
            self.stack.append(obj)
        else:
            self.reversed_stack.append(obj)
            self._move(self.stack, self.reversed_stack)

    def pop(self):
        if not self.reversed_stack:
            self._move(self.stack, self.reversed_stack)
        return self.reversed_stack.pop()

    def leftpop(self):
        if not self.stack:
            self._move(self.reversed_stack, self.stack)
        return self.stack.pop()
