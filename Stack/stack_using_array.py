class Stack:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        return len(self.stack) == 0

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        if self.is_empty():
            return None
        return self.stack.pop()

    def peek(self):
        if self.is_empty():
            return None
        return self.stack[-1]

    def stack_size(self):
        return len(self.stack)


# Creating a stack
stack = Stack()
stack.push(3)
stack.push(5)
stack.push(9)

# Top of the stack
print("Top of the stack:", stack.peek())

# Popping elements from the stack
print("Popped:", stack.pop())  # 9
print("Popped:", stack.pop())  # 5
