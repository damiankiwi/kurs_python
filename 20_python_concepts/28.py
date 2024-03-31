class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            return "Stack is empty. Cannot pop."
        else:
            return self.items.pop()

    def display(self):
        if self.is_empty():
            print("Stack is empty.")
        else:
            print("Stack elements:")
            for item in reversed(self.items):
                print(item)

stack = Stack()

stack.push(1)
stack.push(2)
stack.push(3)

stack.display()

print("\nPopping elements from the stack:")
print(stack.pop())
print(stack.pop())
print(stack.pop())

print("\nDisplaying elements in the stack after popping:")
stack.display()