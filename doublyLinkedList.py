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
            new_node.prev = current_node
        else:  # head points to none
            self.head = new_node

        self.tail = new_node

    def insert_at_index(self, data, index):
        length = self.length()
        # if index is valid
        if 0 <= index <= length:
            new_node = Node(data)
            if index == 0:
                self.insert_at_beginning(data)
            elif 0 < index < length:
                counter = 0
                current_node = self.head
                while counter != index - 1:
                    counter += 1
                    current_node = current_node.next

                new_node.next = current_node.next
                next_node = current_node.next
                next_node.prev = new_node
                current_node.next = new_node
                new_node.prev = current_node
            elif index == length:
                self.insert_at_end(data)
        else:
            print("invalid index")
            return

    def insert_list_values(self, data_list):
        # removes reference to old doublylinkedlist
        # and creates a new one
        self.head = None
        self.tail = None

        for data in data_list:
            self.insert_at_end(data)

    def insert_value_after(self, value, data):
        index = 0
        current_node = self.head
        while current_node:
            index += 1
            if current_node.data == value:
                self.insert_at_index(data, index)
                return
            current_node = current_node.next

        print(f"{value} not found in doublylinkedlist")

    def remove_at(self, index):
        length = self.length()
        if 0 <= index <= length:
            if index == 0:
                self.head = self.head.next
                self.head.prev = None
            elif 0 < index < length:
                counter = 0
                current_node = self.head
                while counter < index - 1:
                    counter += 1
                    current_node = current_node.next

                next_node = current_node.next
                next_next_node = next_node.next
                current_node.next = next_next_node
                next_next_node.prev = current_node
            elif index == length:
                self.remove_at_end()
        else:
            print(f"remove at index {index} is invalid")

    def remove_by_value(self, value):
        if self.length() == 0:
            print("doublylinkedlist is empty")
            return
        else:
            index = 0
            current_node = self.head
            while current_node:
                if current_node.data == value:
                    self.remove_at(index)
                    return
                current_node = current_node.next
                index += 1

            print(f"no node was found with value: {value}")

    def remove_at_end(self):
        if self.length() == 0:
            print(f"doublylinkedlist is empty")
            return
        else:
            self.tail = self.tail.prev
            self.tail.next = None

    def length(self):
        counter = 0
        if self.head is None:
            return 0
        else:
            node = self.head
            while node:
                counter += 1
                if node.next:
                    node = node.next
                else:
                    self.tail = node
                    break

            return counter

    def display(self):
        if self.length() == 0:
            print(f"empty doublylinkedlist")
            return
        else:
            current_node = self.head
            dllstr = ""
            while current_node:
                dllstr += str(current_node.data) + " -> "
                current_node = current_node.next
            print(f"doublylinkedlist {dllstr}")

    def reverse_display(self):
        if self.length() == 0:
            print(f"empty doublylinkedlist")
            return
        else:
            current_node = self.tail
            dllstr = ""
            while current_node:
                dllstr += str(current_node.data) + " -> "
                current_node = current_node.prev

            print(f"reversed doublylinkedlist: {dllstr}")

    def get_values(self):
        values = []
        node = self.head
        while node:
            values.append(node.data)
            node = node.next

        return values


if __name__ == "__main__":
    dll = DoublyLinkedList()
    dll.insert_at_beginning("samuel")
    dll.insert_at_end("benitez")
    dll.insert_at_end("gipit")
    dll.insert_at_index("sample data node", 3)

    data_list = [1, 2, 3, 4, "meow", 6, 8, 5, 3, "samuel"]
    dll.insert_list_values(data_list)
    dll.insert_value_after("samuel", "gipit")
    dll.remove_at_end()

    values = dll.get_values()
    print(values)
