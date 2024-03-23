class QueueWithTwoStacks:
    def __init__(self):
        self.stack_enqueue = []
        self.stack_dequeue = []

    def enqueue(self, item):
        self.stack_enqueue.append(item)
        print("Enqueued:", item)

    def dequeue(self):
        if not self.stack_dequeue:
            if not self.stack_enqueue:
                return "Queue is empty"
            while self.stack_enqueue:
                self.stack_dequeue.append(self.stack_enqueue.pop())
        item = self.stack_dequeue.pop()
        print("Dequeued:", item)
        return item

    def peek(self):
        if not self.stack_dequeue:
            if not self.stack_enqueue:
                return "Queue is empty"
            while self.stack_enqueue:
                self.stack_dequeue.append(self.stack_enqueue.pop())
        return self.stack_dequeue[-1]

    def is_empty(self):
        return not self.stack_enqueue and not self.stack_dequeue

    def display(self):
        if self.is_empty():
            print("Queue is empty")
        else:
            print("Queue elements are:", end=" ")
            print(*self.stack_dequeue[::-1], sep=" ")

queue = QueueWithTwoStacks()
print("1.enqueue")
print("2.dequeue")
print("3.peek")
print("4.display")
print("5.exit")
while True:
    operation = int(input("Enter operation which you want to perform on queue: "))    
    if operation == 1:
        item = input("Enter item to enqueue: ")
        queue.enqueue(item)
    elif operation == 2:
        print("Dequeued item:", queue.dequeue())
    elif operation == 3:
        print("Peek:", queue.peek())
    elif operation == 4:
        queue.display()
    elif operation == 5:
        print("Exiting...")
        break
    else:
        print("Invalid operation. Please enter enqueue, dequeue, peek, display, or exit.")
