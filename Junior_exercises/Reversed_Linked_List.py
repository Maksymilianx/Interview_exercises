class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


""" A node is implemented as a class named Node . The class contains the definition to create an object instance,
    in this case, with two variables - data to keep the node value, 
    and next to store the reference to the next node in the list. """


class LinkedList:

    # Function to initialize head
    def __init__(self):
        self.head = None

    def reverseUtil(self, current, previous):

        # If last node let it be head
        if current.next is None:
            self.head = current

            # Update next as previous node
            current.next = previous
            return

        # Save current.next node for recursive call
        """ Recursion e.g. 
            A physical world example would be to place two parallel mirrors facing each other. 
            Any object in between them would be reflected recursively."""

        next = current.next

        # And update next
        current.next = previous
        self.reverseUtil(next, current)

    # reverse function mainly calls reverseUtil() with previous as None
    def reverse(self):
        if self.head is None:
            return
        self.reverseUtil(self.head, None)

    # Function to insert a new node at the beginning
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    # Utility function to print the linked LinkedList
    def printList(self):
        temp = self.head
        while (temp):
            print(temp.data)
            temp = temp.next


lst = LinkedList()
lst.push(8)
lst.push(9)
lst.push(8)
lst.push(7)
lst.push(6)
lst.push(5)
lst.push(4)
lst.push(3)
lst.push(2)
lst.push(1)

print("Given linked list")
lst.printList()
lst.reverse()
print("\nReverse linked list")
lst.printList()
