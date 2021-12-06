class Node:
    def __init__(self, value):
        self.next = None
        self.prev = None
        self.value = value

class LinkedList:
    def __init__(self):
        self.nhead = Node('')
        self.ntail = Node('')
        self.nhead.next = self.ntail
        self.ntail.prev = self.nhead

    def insert_node_to_tail(self, node):
        self.ntail.next = node
        node.prev = self.ntail
        self.ntail = node

    def insert_node_to_head(self, node):
        self.nhead.prev = node
        node.next = self.nhead
        self.nhead = node

    def is_empty(self):
        pass

    def head(self):
        return self.nhead

    def tail(self):
        return self.ntail

import unittest

class LinkedListTests(unittest.TestCase):
    def setUp(self):
        self.linked_list = LinkedList()
    
    def test_insert_first_node_to_tail(self):
        self.linked_list.insert_node_to_tail(Node('tail'))

        self.assertEqual(
            'tail',
            self.linked_list.tail().value
        )

    def test_insert_two_node_to_tail(self):
        self.linked_list.insert_node_to_tail(Node('tail1'))
        self.linked_list.insert_node_to_tail(Node('tail2'))

        self.assertEqual(
            'tail2',
            self.linked_list.tail().value
        )

    def test_insert_first_node_to_head(self):
        self.linked_list.insert_node_to_head(Node('head'))

        self.assertEqual(
            'head',
            self.linked_list.head().value
        )

print('Iniciando script')
unittest.main()