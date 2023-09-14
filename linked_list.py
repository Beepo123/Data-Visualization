"""Creating a linked list"""


class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class Solution:
    """Merge two linkedlist by splicing them
    and return head of new sorted linkedlist"""

    def mergeTwoList(self, list1, list2):
        # list1 = self.sortLinkedList(list1)
        # list2 = self.sortLinkedList(list2)

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
        else:
            node = Node(data, next=None)
            itr = self.head
            while itr.next:
                itr = itr.next

            itr.next = node

    def insert_list_values(self, data_list):
        for data in data_list:
            self.insert_at_end(data)

    def print_ll_len(self):
        if self.head == None:
            return 0

        counter = 0
        curr_node = self.head
        while curr_node:
            counter += 1
            curr_node = curr_node.next

        print(counter)


if __name__ == "__main__":
    ll = LinkedList()
    ll.insert_at_beginning(10)
    
    nums = [1,2,3,4,5]
    ll.insert_list_values(nums)
    ll.print()