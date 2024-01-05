class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None
        self.size = 0

    def is_empty(self):
        return self.top is None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node
        self.size += 1

    def pop(self):
        if self.is_empty():
            raise ValueError("Stack is empty")
        else:
            data = self.top.data
            self.top = self.top.next
            self.size -= 1
            return data

    def peek(self):
        if self.is_empty():
            raise ValueError("Stack is empty")
        else:
            return self.top.data

    def stack_size(self):
        return self.size


stack = Stack()
stack.push(5)
stack.push(10)
stack.push(15)

print("Stack size:", stack.size)  # Output: Stack size: 3
print("Top element:", stack.peek())  # Output: Top element: 15

popped = stack.pop()
print("Popped element:", popped)  # Output: Popped element: 15
print("Top element:", stack.peek()) # Output: Top element: 10
print("Stack size after pop:", stack.size)  # Output: Stack size after pop: 2
