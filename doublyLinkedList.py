class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


class DoublyLinkedList:
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail
        
    def insert_at_beginning(self, data):
        """Insert node at the beginning of doubly linkedlist"""
        new_node = Node(data, next=self.head)
        new_node.next = self.head
        if self.head:
            self.head.prev = new_node
        else:
            self.tail = new_node

        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        current_node = self.head
        # if tail node exists, add to at end
        if self.tail:
            end_node = self.tail
            end_node.next = new_node
            new_node.prev = end_node
            self.tail = new_node
            return
        
        # if there are node/s but no reference to tail
        if current_node:
            while current_node.next:
                current_node = current_node.next
            current_node.next = new_node
        else: # head points to none
            self.head = new_node
            
        self.tail = new_node

    def insert_at_index(self, data, index):
        pass

    def insert_list_values(self):
        pass

    def insert_after_value(self):
        pass

    def remove_at(self):
        pass

    def remove_by_value(self):
        pass

    def length(self):
        counter = 0
        if self.head is None:
            return 0
        else:
            node = self.head
            while node:
                node = node.next
                counter += 1
            return counter

    def display(self):
        node = self.head
        dllstr = ""
        while node:
            dllstr += str(node.data) + " -> "
            node = node.next
        print(dllstr)

if __name__ == "__main__":
    dll = DoublyLinkedList()
    # dll.insert_at_beginning("samuel")
    # dll.insert_at_end("benitez")
    # dll.insert_at_end("gipit")
    dll.display()
    print(dll.length())