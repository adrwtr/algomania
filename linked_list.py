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
        self.ntail = Node('')
        self.nhead = Node('')
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

    def is_empty_with_empty_linked_list(self):
        self.assertTrue(self.linked_list.is_empty())


print('Iniciando script')
unittest.main()
