class Node:
    def __init__(self, value):
        self.next = None
        self.prev = None
        self.value = value

    def is_empty(self) :
        return (self.next == None) and (self.prev == None) and (self.value == '')

class LinkedList:
    def __init__(self):
        self.nhead = None
        self.ntail = None        

    def iniciaLista(self):
        self.ntail = Node(None)
        self.nhead = Node(None)
        self.nhead.next = self.ntail
        self.ntail.prev = self.nhead

    def insert_node_to_tail(self, node):
        if (self.ntail == None):
            self.iniciaLista()            

        self.ntail.next = node
        node.prev = self.ntail
        self.ntail = node

    def insert_node_to_head(self, node):
        if (self.nhead == None):
            self.iniciaLista()            

        self.nhead.prev = node
        node.next = self.nhead
        self.nhead = node

    def is_empty(self):
        if (self.nhead == None):
            return True
        
        if (self.ntail == None):
            return True

        return self.nhead.is_empty() and self.ntail.is_empty()

    def head(self):
        return self.nhead

    def tail(self):
        return self.ntail    

    def find(self, valor):
        atual = self.nhead

        if (atual.value == valor):
            return True

        while atual.next != None:
            if (atual.value == valor):
                return True

            atual = atual.next

        return False

    def is_circular(self):
        atual = self.nhead
        if (atual == None):
            return False

        while atual.next != None:
            if (atual.next == self.nhead):
                return True
            atual = atual.next
        return False


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


    def test_find(self):
        self.linked_list.insert_node_to_tail(Node('tail1'))
        self.linked_list.insert_node_to_tail(Node('tail2'))
        self.linked_list.insert_node_to_tail(Node('tail3'))

        self.assertFalse(            
            self.linked_list.find('nada')
        )

        self.assertTrue(            
            self.linked_list.find('tail2')
        )

    def test_is_empty_with_empty_linked_list(self):
        self.assertTrue(self.linked_list.is_empty())

    def test_is_circular(self):
        self.assertFalse(self.linked_list.is_circular())
        self.linked_list.insert_node_to_tail(Node('tail1'))
        self.linked_list.insert_node_to_tail(Node('tail2'))
        self.linked_list.insert_node_to_tail(Node('tail3'))
        
        self.assertFalse(self.linked_list.is_circular())

        self.linked_list.ntail.next = self.linked_list.nhead
        self.assertTrue(self.linked_list.is_circular())
        print(self.linked_list)


print('Iniciando script')
unittest.main()





""" --> codigo original para busca futura
class Node:
    def __init__(self, value):
        self.next = None
        self.value = value


class LinkedList:
    def __init__(self):
        self._head = Node(None)

    def insert_node_to_tail(self, node):
        self.tail().next = node

    def insert_node_to_head(self, node):
        if self._head.next:
            head_element = self._head
            node.next, head_element.next = head_element.next, node
        self._head.next = node

    def is_empty(self):
        return self._head.next is None

    def head(self):
        return self._head.next

    def tail(self):
        current = self._head
        while current.next:
            current = current.next
        return current
"""

"""
Codigo original para desafio > detect-circular-linked-list

def solution(linked_list):
    atual = linked_list.head()
    
    if (atual == None):
        return False

    while atual.next != None:
        if (atual.next == linked_list.head()):
            return True
        atual = atual.next
    return False
"""    