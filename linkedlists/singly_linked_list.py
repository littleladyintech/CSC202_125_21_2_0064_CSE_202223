# linkedlists/singly_linked_list.py
from nodes.node import Node

class SinglyLinkedList:
    def __init__(self):
        """
        Initialize an empty singly linked list.
        """
        self.head = None

    def insert(self, data):
        """
        Insert a new element at the end of the linked list.
        """
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def display(self):
        """
        Display the elements of the linked list.
        """
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        print(elements)

    def length(self):
        """
        Calculate the length of the linked list.
        """
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count