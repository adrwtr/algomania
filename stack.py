from linked_list import *

def print_linked_list(linked_list):
    node = linked_list.head()
    while node:
        print(node.value, end=" ")
        node = node.next

def print_reverd_linked_list(linked_list):
    stack = []

    node = linked_list.head()
    while node:
        stack.append(node.value)
        node = node.next
    
    while stack:
        print(stack.pop(), end=" ")



linked_list = LinkedList()
linked_list.insert_node_to_tail(Node('1'))
linked_list.insert_node_to_tail(Node('2'))
linked_list.insert_node_to_tail(Node('3'))

print("Iniciando\n")
print_linked_list(linked_list)
print("\n")
print_reverd_linked_list(linked_list)



import unittest


class LinkedListTests(unittest.TestCase):
    def setUp(self):
        self.linked_list = LinkedList()
    
    def test_normal(self):
        self.linked_list.insert_node_to_tail(Node('1'))
        self.linked_list.insert_node_to_tail(Node('2'))
        self.linked_list.insert_node_to_tail(Node('3'))

        print_linked_list(self.linked_list)
        self.assertEqual(False, True)
