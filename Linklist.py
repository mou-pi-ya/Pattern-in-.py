class Node:
    """Class to represent a single node in a linked list."""
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    """Class to manage the linked list."""
    def __init__(self):
        self.head = None

    def add_node(self, data):
        """Add a node to the end of the list."""
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        # Traverse to the end of the list
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def print_list(self):
        """Print all elements in the list."""
        if self.head is None:
            print("List is empty.")
            return
        current = self.head
        print("Linked List:", end=" ")
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def delete_nth_node(self, n):
        """Delete the nth node from the list (1-based index)."""
        try:
            if self.head is None:
                raise IndexError("Cannot delete from an empty list.")
            if n <= 0:
                raise IndexError("Index must be a positive integer (1-based index).")

            # Deleting the head node
            if n == 1:
                print(f"Deleting node at position {n} with value '{self.head.data}'.")
                self.head = self.head.next
                return

            # Traverse to the node just before the one to delete
            current = self.head
            for i in range(n - 2):
                if current.next is None:
                    raise IndexError("Index out of range.")
                current = current.next

            if current.next is None:
                raise IndexError("Index out of range.")

            print(f"Deleting node at position {n} with value '{current.next.data}'.")
            current.next = current.next.next

        except IndexError as e:
            print(f"Error: {e}")


# ---------- Testing the implementation ----------
if __name__ == "__main__":
    # Create linked list and add some nodes
    ll = LinkedList()
    ll.add_node(10)
    ll.add_node(20)
    ll.add_node(30)
    ll.add_node(40)

    print("\nInitial List:")
    ll.print_list()

    # Delete 2nd node (should remove 20)
    print("\nDeleting 2nd node:")
    ll.delete_nth_node(2)
    ll.print_list()

    # Delete 1st node (should remove 10)
    print("\nDeleting 1st node:")
    ll.delete_nth_node(1)
    ll.print_list()

    # Attempt to delete out-of-range index
    print("\nTrying to delete 10th node (out of range):")
    ll.delete_nth_node(10)

    # Attempt to delete from an empty list
    print("\nDeleting all remaining nodes:")
    ll.delete_nth_node(1)  # Deletes 30
    ll.delete_nth_node(1)  # Deletes 40
    ll.print_list()
    
    print("\nAttempting to delete from an empty list:")
    ll.delete_nth_node(1)
