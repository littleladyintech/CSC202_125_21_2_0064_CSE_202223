# main.py
from linkedlists.singly_linked_list import SinglyLinkedList

def main():
    data_list = [1, 3, 4, 5, 6, 8, 7, 9, 2, 22, 15, 55, 45, 23, 24, 26, 28]

    # Create a singly linked list
    linked_list = SinglyLinkedList()

    # Insert elements from the data_list into the linked list
    for data in data_list:
        linked_list.insert(data)

    # Display the elements of the linked list
    linked_list.display()

    # Test other list operations
    print("Length of the linked list:", linked_list.length())

if __name__ == "__main__":
    main()
