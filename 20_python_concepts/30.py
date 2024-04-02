class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)
        print(f"{item} enqueued into the queue.")

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty. Cannot dequeue.")
        else:
            dequeued_item = self.items.pop(0)
            print(f"{dequeued_item} dequeued from the queue.")
            return dequeued_item

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

queue = Queue()

queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)

dequeued_item = queue.dequeue()
dequeued_item = queue.dequeue()
dequeued_item = queue.dequeue()

dequeued_item = queue.dequeue()