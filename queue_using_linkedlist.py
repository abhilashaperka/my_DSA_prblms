class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        return self.front is None

    def enqueue(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        if self.is_empty():            
            print("queue is empty")
        else:
            data = self.front.data
            if self.front == self.rear:
                self.front = None
                self.rear = None
            else:
                self.front = self.front.next
            return data

    def peek(self):
        if self.is_empty():
            print("queue is empty")
        else:
            return self.front.data

    def display(self):
        curr = self.front
        while curr:
            print(curr.data, end=" ")
            curr = curr.next
        print()

queue = Queue()
queue.enqueue(1)
queue.enqueue(3)
queue.enqueue(9)
queue.enqueue(7)
queue.enqueue(5)
print("queue elements are:")
queue.display()
print("peek:", queue.peek())
print("dequeue:", queue.dequeue())
print("queue elements after dequeue:")
queue.display()
