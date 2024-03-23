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

    def remove_last_occurrence(self, data):
        if self.head is None:
            print("List is empty")
            return

        last_occurrence = None
        current_node = self.head
        prev_last_occurrence = None
        prev_node = None

        while current_node:
            if current_node.data == data:
                prev_last_occurrence = prev_node
                last_occurrence = current_node
            prev_node = current_node
            current_node = current_node.next

        if last_occurrence is None:
            print("Element not found in the list")
            return

        if last_occurrence == self.head:
            self.head = self.head.next
            return

        prev_last_occurrence.next = last_occurrence.next

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
print("2.remove last occurence")
print("3.display")
print("4.exit")
while True:
    operation = int(input("Enter operation: "))    
    if operation == 1:
        data = input("Enter data to append: ")
        linked_list.append(data)
        linked_list.display()
    elif operation ==2:
        data = input("Enter data to remove last occurrence: ")
        linked_list.remove_last_occurrence(data)
        linked_list.display()
    elif operation == 3:
        linked_list.display()
    elif operation == 4:
        print("Exiting...")
        break
    else:
        print("Invalid operation. Please enter append, remove_last_occurrence, display, or exit.")
