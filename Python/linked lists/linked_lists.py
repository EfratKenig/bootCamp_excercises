"""
NOT FINISHED
"""

class Node:

    def __init__(self, data_val=None):
        self.data_val = data_val
        self.next_val = None

    def __repr__(self):
        return " data: " + str(self.data_val) + " next: " + str(self.next_val)

    def advance_right(self):
        new_node = Node(self.next_val.data_val)
        new_node.next_val = self.next_val.next_val
        self = new_node



class LinkedList:

    def __init__(self, head=None):
        self.head = Node(head.data_val)
        self.tail = self.head
        self.head.next_val = None
        self.len = 1 if self.head else 0

    def reverse_list(self):
        """ returns new reversed list of the given linked list """
        reversed_list = LinkedList(self.tail)
        node = self.head
        tmp_next = node.next_val
        node.next_val = None
        tmp_prev = node

        while node:
            node = tmp_next
            tmp_next = node.next_val
            node.next_val = tmp_prev
            tmp_prev = node

    def __repr__(self):
        l = []
        node = self.head
        for i in range(self.len):
            l.append(node.__repr__())
            node = node.next_val
        return l

    def peek_node(self, val):
        node = self.head
        while node:
            if node.data_val == val:
                # only return the node:
                return node
            else:
                node = node.next_val
        return None

    def enqueue(self, val):
        node = Node(val)
        node.next_val = None
        if self.head is None:
            self.head = node
            self.tail = self.head
        else:
            self.tail.next_val = node
            self.len += 1
            self.tail = node

    def dequeue_tail(self):
        self.len -= 1
        return self.tail

    def dequeue(self, val):
        node = self.head
        prev = None
        tmp_next = None
        while node:
            if node.data_val == val:
                # unlink from list and return:
                tmp_next = node.next_val
                prev.next_val = tmp_next
                self.len -= 1
                if prev is None:
                    self.head = node
                return node
            else:
                prev = node
                node = tmp_next
        return None

    def check_circular_list(self):
        return self.tail.next_val == self.head

    def check_lists_merging(self, head1, head2):
        l1 = LinkedList(head1)
        l2 = LinkedList(head2)
        if l1.tail != l2.tail:
            return False
        long, short = (l1, l2) if l1.len >l2.len else (l2, l1)
        short.reverse_list()
        long.reverse_list()
        left1 = long.head
        left2 = short.head
        merging = False
        for i in range(short.len):
            if left1.data_val == left2.data_val:
                left1.advance_right()
                left2.advance_right()
                merging = True
            else:
                break
        return merging

