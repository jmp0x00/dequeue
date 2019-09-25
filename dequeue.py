class Dequeue(object):

    def __init__(self):
        self.stack = []
        self.reversed_stack = []
        pass

    @staticmethod
    def _move(a, b):
        while len(a) > 0:
            b.append(a.pop())

    def push(self, obj):
        if len(self.stack) == 0:
            self._move(self.reversed_stack, self.stack)
            self.stack.append(obj)
        else:
            self.reversed_stack.append(obj)
            self._move(self.stack, self.reversed_stack)

    def pop(self):
        if len(self.reversed_stack) == 0:
            self._move(self.stack, self.reversed_stack)
        return self.reversed_stack.pop()

    def leftpop(self):
        if len(self.stack) == 0:
            self._move(self.reversed_stack, self.stack)
        return self.stack.pop()