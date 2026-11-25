class MinStack:

    def __init__(self):
        self.Min = None
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.Min is None or self.Min > val:
            self.Min = val

    def pop(self) -> None:
        if self.Min == self.stack[-1]:
            self.stack.pop()
            if len(self.stack) == 0:
                self.Min = None
            if len(self.stack) == 1:
                self.Min = self.stack[0]
            if len(self.stack) > 1:
                self.Min = self.stack[0]
                for i in self.stack:
                    if i < self.Min:
                        self.Min = i
        else:
            self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.Min
