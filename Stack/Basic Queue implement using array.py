class Queue:
    def __init__(self):
        self.queue = []
    def enque(self,value):
        self.queue.append(value)
    def deque(self):
        if self.is_empty():
            return "queue is empty"
        else:
            return self.queue.pop(0)
    def front(self):
        if self.is_empty():
            return "queue is empty nothing to show"
        return self.queue[0]
    def rear(self):
        if self.is_empty():
            return "queue is empty nothing to show"
        return self.queue[-1]
    def display(self):
        if self.is_empty():
            return "queue is empty nothing to show"
        print(self.queue)
    def size(self):
        return len(self.queue)
    def is_empty(self):
        return len(self.queue)==0

q = Queue()

q.enque(10)
q.enque(20)
q.enque(30)
print(q.deque())
print(q.front())
print(q.rear())
q.display()
print(q.size())
print(q.is_empty())
