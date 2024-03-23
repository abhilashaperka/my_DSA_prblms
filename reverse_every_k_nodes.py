#reverse every k node
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

    
    def insertNode(head, val):
        newnode = Node(val)
        if head is None:
            head = newnode
            return head
        else:
            temp = head
            while temp.next is not None:
                temp = temp.next
            temp.next = newnode
        return head

    
    def lenOfLinkedList(head):
        length = 0
        while head is not None:
            length += 1
            head = head.next
        return length

   
    def reverseKNodes(head, k):
        if head is None or head.next is None:
            return head
        length = Node.lenOfLinkedList(head)
        dummyhead = Node(0)
        dummyhead.next = head
        pre = dummyhead
        cur = None
        nex = None
        while length >= k:
            cur = pre.next
            nex = cur.next
            for i in range(1, k):
                cur.next = nex.next
                nex.next = pre.next
                pre.next = nex
                nex = cur.next
            pre = cur
            length -= k
        return dummyhead.next

    
    def printLinkedList(head):
        while head is not None:
            print(head.val, end="")
            if head.next is not None:
                print("->", end="")
            head = head.next
        print()


if __name__ == "__main__":
    head = None
    k = 3
    head = Node.insertNode(head, 1)
    head = Node.insertNode(head, 2)
    head = Node.insertNode(head, 3)
    head = Node.insertNode(head, 5)
    head = Node.insertNode(head, 6)
    head = Node.insertNode(head, 9)
    print("Original linked list:", end=" ")
    Node.printLinkedList(head)
    print("After reversal of k nodes:", end=" ")
    newhead = Node.reverseKNodes(head, k)
    Node.printLinkedList(newhead)
