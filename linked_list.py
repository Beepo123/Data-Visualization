"""Creating a linked"""

class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node
    
    def print(self):
        if self.head is None:
            print("Linked list is empty")
            return
        else:
            itr = self.head
            llstr = ""
            while itr:
                llstr += str(itr.data) + "--->"
                itr = itr.next 
            print(llstr)
            
    def insert_at_end(self, data):
        if self.head is None:
                self.head = Node(data, self.head)
                return

        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = Node(data, next=None)

    def insert_values(self, data_list):
        # remove reference to previous linked list
        # to create new linked list using data_list
        self.head = None
        for data in data_list:
            self.insert_at_end(data)



if __name__ == '__main__':
    numbers = [x for x in range(10)]
    more_numbers = [x for x in range(10, 20)]

    ll = LinkedList()
    for num in more_numbers:
        ll.insert_at_end(num)

    ll.insert_values(numbers)
    ll.print()
    print("end of file")