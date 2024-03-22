class TwoStacks:
    def __init__(self, capacity):
        self.capacity = capacity
        self.arr = [None] * capacity
        self.top1 = -1  # Top index for stack 1
        self.top2 = self.capacity  # Top index for stack 2

    def is_full1(self):
        return self.top1 + 1 == self.top2

    def is_full2(self):
        return self.top2 - 1 == self.top1

    def push1(self, item):
        if self.is_full1():
            print("Stack 1 is full. Cannot push item.")
        else:
            self.top1 += 1
            self.arr[self.top1] = item

    def push2(self, item):
        if self.is_full2():
            print("Stack 2 is full. Cannot push item.")
        else:
            self.top2 -= 1
            self.arr[self.top2] = item

    def pop1(self):
        if self.top1 == -1:
            print("Stack 1 is empty. Nothing to pop.")
            return None
        else:
            item = self.arr[self.top1]
            self.arr[self.top1] = None
            self.top1 -= 1
            return item

    def pop2(self):
        if self.top2 == self.capacity:
            print("Stack 2 is empty. Nothing to pop.")
            return None
        else:
            item = self.arr[self.top2]
            self.arr[self.top2] = None
            self.top2 += 1
            return item

    def display1(self):
        if self.top1 == -1:
            print("Stack 1 is empty.")
        else:
            print("Stack 1 elements:")
            for i in range(self.top1, -1, -1):
                print(self.arr[i])

    def display2(self):
        if self.top2 == self.capacity:
            print("Stack 2 is empty.")
        else:
            print("Stack 2 elements:")
            for i in range(self.top2, self.capacity):
                print(self.arr[i])


# Example usage with user input:
capacity = int(input("Enter the capacity of the two stacks: "))
two_stacks = TwoStacks(capacity)

while True:
    print("\nTwo Stacks Operations:")
    print("1. Push to Stack 1")
    print("2. Push to Stack 2")
    print("3. Pop from Stack 1")
    print("4. Pop from Stack 2")
    print("5. Display Stack 1")
    print("6. Display Stack 2")
    print("7. Exit")

    choice = input("Enter your choice (1-7): ")

    if choice == '1':
        item = int(input("Enter the item to push onto Stack 1: "))
        two_stacks.push1(item)
    elif choice == '2':
        item = int(input("Enter the item to push onto Stack 2: "))
        two_stacks.push2(item)
    elif choice == '3':
        popped_item = two_stacks.pop1()
        if popped_item is not None:
            print("Popped item from Stack 1:", popped_item)
    elif choice == '4':
        popped_item = two_stacks.pop2()
        if popped_item is not None:
            print("Popped item from Stack 2:", popped_item)
    elif choice == '5':
        two_stacks.display1()
    elif choice == '6':
        two_stacks.display2()
    elif choice == '7':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please enter a valid option (1-7).")
