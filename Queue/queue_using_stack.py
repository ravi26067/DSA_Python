class Queue:
    def __init__(self):
        self.s1 = list()
        self.s2 = list()

    def enQueue(self, x):

        # Move all elements from s1 to s2
        while len(self.s1) != 0:
            self.s2.append(self.s1.pop())

        # Push new item to s1
        self.s1.append(x)

        # Push everything back to s1
        while len(self.s2) != 0:
            self.s1.append(self.s2.pop())

    def deQueue(self):
        if len(self.s1) == 0:
            return -1

        return self.s1.pop()

    def printQueue(self):
        if not self.s1:
            print("Queue is empty")
        else:
            print("Queue:", self.s1[::-1])


q = Queue()
q.enQueue(5)
q.enQueue(10)
q.enQueue(1)
q.printQueue()
q.deQueue()
q.printQueue()
