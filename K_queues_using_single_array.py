class KQueues:
    def __init__(self, k, capacity):
        self.k = k  # Number of queues
        self.capacity = capacity  # Total capacity of the array
        self.queue = [None] * capacity  # Array to store elements
        self.front = [-1] * k  # Array to store front indices of each queue
        self.rear = [-1] * k  # Array to store rear indices of each queue
        self.next = list(range(1, capacity)) + [-1]  # Array to store next available index after each element
        self.free = 0  # Index of the first available position in the array

    def is_empty(self, q_num):
        return self.front[q_num] == -1

    def is_full(self, q_num):
        return self.free == -1

    def enqueue(self, q_num, item):
        if self.is_full(q_num):
            print("Queue", q_num, "is full")
            return

        next_free = self.next[self.free]  # Get the next available index
        if self.is_empty(q_num):
            self.front[q_num] = self.rear[q_num] = self.free
        else:
            self.next[self.rear[q_num]] = self.free
            self.rear[q_num] = self.free
        self.queue[self.free] = item
        self.free = next_free
        print("Enqueued to Queue", q_num, ":", item)
        self.display(q_num)

    def dequeue(self, q_num):
        if self.is_empty(q_num):
            print("Queue", q_num, "is empty")
            return None
        item = self.queue[self.front[q_num]]
        next_free = self.front[q_num]
        self.front[q_num] = self.next[self.front[q_num]]
        self.next[next_free] = self.free
        self.free = next_free
        if self.front[q_num] == -1:
            self.rear[q_num] = -1
        print("Dequeued from Queue", q_num, ":", item)
        self.display(q_num)
        return item

    def peek(self, q_num):
        if self.is_empty(q_num):
            print("Queue", q_num, "is empty")
            return None
        return self.queue[self.front[q_num]]

    def display(self, q_num):
        if self.is_empty(q_num):
            print("Queue", q_num, "is empty")
            return
        print("Queue", q_num, "elements are:", end=" ")
        i = self.front[q_num]
        while i != self.rear[q_num]:
            print(self.queue[i], end=" ")
            i = self.next[i]
        print(self.queue[i])
k = int(input("Enter the number of queues: "))
capacity = int(input("Enter the total capacity of the array: "))
k_queues = KQueues(k, capacity)
print("1.enqueue")
print("2.dequeue")
print("3.peek")
print("4.display")
print("5.exit")
while True:
    operation = int(input("Enter operation: "))
    
    if operation == 1:
        q_num = int(input("Enter queue number: "))
        item = input("Enter item to enqueue: ")
        k_queues.enqueue(q_num, item)
    elif operation == 2:
        q_num = int(input("Enter queue number: "))
        k_queues.dequeue(q_num)
    elif operation == 3:
        q_num = int(input("Enter queue number: "))
        print("Peek:", k_queues.peek(q_num))
    elif operation == 4:
        q_num = int(input("Enter queue number: "))
        k_queues.display(q_num)
    elif operation == 5:
        print("Exiting...")
        break
    else:
        print("Invalid operation. Please enter enqueue, dequeue, peek, display, or exit.")
