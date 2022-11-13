class MinStack:

    def __init__(self):
        self.stack = []
        self.minArr = []
        
    def push(self, val: int) -> None:
        
        currMin = self.getMin()
        if currMin is None or currMin>val:
            self.minArr.append(val)
        else:
            self.minArr.append(currMin)
        
        self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minArr.pop()
        
    def top(self) -> int:
        return self.stack[len(self.stack) - 1]

    def getMin(self) -> int:
        if len(self.stack) == 0:
            return None
        return self.minArr[len(self.minArr) - 1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()