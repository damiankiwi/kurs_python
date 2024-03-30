class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def delete(self, data):
        if self.head is None:
            print("List is empty")
            return

        if self.head.data == data:
            self.head = self.head.next
            return

        current = self.head
        prev = None
        while current and current.data != data:
            prev = current
            current = current.next

        if current is None:
            print("Data not found")
            return

        prev.next = current.next

ll = LinkedList()
ll.insert(1)
ll.insert(2)
ll.insert(3)
ll.insert(4)
ll.insert(5)

print("Initial linked list:")
ll.display()

print("\nLinked list after deleting node with data 3:")
ll.delete(3)
ll.display()

print("\nLinked list after deleting node with data 1:")
ll.delete(1)
ll.display()