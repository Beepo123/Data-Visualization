"""Creating a linked list"""


class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class Solution:
    """Merge two linkedlist by splicing them
    and return head of new sorted linkedlist"""

    def mergeTwoList(self, list1, list2):
        # case 1: both linkedlist is empty
        # case 2: one linkedlist is emtpy
        # case 3: both have at least 1 node

        if list1 is None and list2 is None:
            return None
        elif list1 is None:
            return list2
        elif list2 is None:
            return list1
        else:
            dummy_node = Node()
            current_node = dummy_node
            while list1 is not None and list2 is not None:
                if list1.data < list2.data:
                    current_node.next = list1
                    list1 = list1.next
                else:
                    current_node.next = list2
                    list2 = list2.next

                current_node = current_node.next

            # append remaining nodes to the merge linked list
            if list1:
                current_node.next = list1
            elif list2:
                current_node.next = list2

        return dummy_node.next

    def sortLinkedList(self, LinkedList):
        pass


class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, self.head)
            return
        else:
            node = Node(data, next=None)
            itr = self.head
            while itr.next:
                itr = itr.next

            itr.next = node
    
    def insert_at(self, index, data):
        """insert node at specified index"""
        if index<0 or index>self.length():
            print(f"not a valid index {index}")
            return
        elif index == 0:
            self.insert_at_beginning(data)
        elif index == self.length():
            self.insert_at_end(data)
        else:
            current = self.head
            counter = 0
            while current:
                if counter == index-1:
                    node = Node(data, current.next)
                    current.next = node
                    break

                current = current.next
                counter += 1

            current.next = node

    def insert_list_values(self, data_list):
        for data in data_list:
            self.insert_at_end(data)

    def insert_after_value(self, data_after, data):
        index = 0
        current = self.head
        while current:
            if current.data == data_after:
                self.insert_at(index+1, data)
                return
            current = current.next
            index += 1

        print(f"no node found with {data_after} data")

    def remove_at(self, index):
        """Remove node at specified index"""
        if index<0 or index>=self.length():
            print(f"not a valid index {index}")
            return

        if index == 0:
            self.head = self.head.next
            return
        
        count = 0
        itr = self.head
        while count < index-1:
            itr = itr.next
            count += 1

        itr.next = itr.next.next
        return
    
    def remove_by_value(self, data):
        node = self.head
        # if head is the node make next node the new head
        if self.head.data == data:
            self.head = node.next
        else:
            while node:
                # if next node is the data then point current node to next next node
                # but if next next node doesn't exists point current.next to none
                if node.next.data == data:
                    if node.next.next:
                        node.next = node.next.next
                    else:
                        node.next = None
                    return
                else:
                    node = node.next
                    if node.data != data and node.next is None:
                        print(f"no node with data {data}")
                        return

    def length(self):
        if self.head == None:
            return 0

        counter = 0
        curr_node = self.head
        while curr_node:
            counter += 1
            curr_node = curr_node.next

        return counter

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

if __name__ == "__main__":
    ll = LinkedList()
    ll.insert_list_values(["banana","mango","grapes","orange"])
    ll.print()
    ll.insert_after_value("mango","apple") # insert apple after mango
    ll.print()
    ll.remove_by_value("orange") # remove orange from linked list
    ll.print()
    ll.remove_by_value("figs")
    ll.print()
    ll.remove_by_value("banana")
    ll.remove_by_value("mango")
    ll.remove_by_value("apple")
    ll.remove_by_value("grapes")
    ll.print()