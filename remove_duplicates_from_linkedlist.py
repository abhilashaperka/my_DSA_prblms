class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

    def push(self, newdata):
        newnode = Node(newdata)
        newnode.next = self
        return newnode

    def printlist(self):
        temp = self
        while temp:
            print(temp.data, end="")
            if temp.next:
                print("->", end="")
            temp = temp.next
        print()

    def removeduplicates(self):
        track = {}
        prev = None
        current = self
        while current:
            if current.data in track:
                prev.next = current.next
            else:
                track[current.data] = True
                prev = current
            current = current.next


# driver code
head = Node(20)
head = head.push(2)
head = head.push(10)
head = head.push(2)
head = head.push(43)
head = head.push(2)
head = head.push(6)

print("Linked list before removal of duplicates:", end=" ")
head.printlist()

print("Linked list after removing duplicates:", end=" ")
head.removeduplicates()
head.printlist()
