class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete(self, data):
        if self.head is None:
            print("List is empty")
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        current_node = self.head
        while current_node.next:
            if current_node.next.data == data:
                current_node.next = current_node.next.next
                return
            current_node = current_node.next
        print("Element not found in the list")

    def display(self):
        if self.head is None:
            print("List is empty")
            return
        current_node = self.head
        while current_node:
            print(current_node.data, end=" ")
            current_node = current_node.next
        print()

linked_list = LinkedList()
print("1.append")
print("2.prepend")
print("3.delete")
print("4.display")
print("5.exit")

while True:
    operation = int(input("Enter operation: "))
    
    if operation ==1:
        data = input("Enter data to append: ")
        linked_list.append(data)
        linked_list.display()
    elif operation == 2:
        data = input("Enter data to prepend: ")
        linked_list.prepend(data)
        linked_list.display()
    elif operation == 3:
        data = input("Enter data to delete: ")
        linked_list.delete(data)
        linked_list.display()
    elif operation == 4:
        linked_list.display()
    elif operation == 5:
        print("Exiting...")
        break
    else:
        print("Invalid operation. Please enter append, prepend, delete, display, or exit.")
