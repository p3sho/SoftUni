class Stack:
    def __init__(self):
        self.data = []

    def push(self, element):
        if not isinstance(element, str):
            raise ValueError("Only strings can be added to the stack.")
        self.data.append(element)

    def pop(self):
        if not self.is_empty():
            return self.data.pop()

    def top(self):
        if not self.is_empty():
            return self.data[-1]

    def is_empty(self):
        return len(self.data) == 0

    def __str__(self):
        elements = ', '.join(reversed(self.data))
        return f"[{elements}]"


if __name__ == "__main__":
    stack = Stack()
    print(stack.is_empty())

    stack.push("apple")
    stack.push("banana")
    stack.push("cherry")
    print(stack)

    print(stack.top())

    popped_element = stack.pop()
    print(popped_element)

    print(stack)

    print(stack.is_empty())
