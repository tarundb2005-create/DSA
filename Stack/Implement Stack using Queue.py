class MyStack:

    def __init__(self):
        self.q = []
        

    def push(self, x: int) -> None:
        self.q.append(x)
        for _ in range(len(self.q)-1):
            self.q.append(self.q.pop(0))

    def pop(self) -> int:
        if self.empty():
            return "No value to pop"
        else:
            return self.q.pop(0)

    def top(self) -> int:
        if self.empty():
            return "No value in top"
        else:
            return self.q[0]

    def empty(self) -> bool:
        return len(self.q)==0
