#!/usr/bin/python3
class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        return (self.__data)

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        if value and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        new_node = Node(value)
        if self.__head is None:
            self.__head = new_node
        else:
            tmp_node = self.__head
            while (tmp_node.next_node):
                tmp_node = tmp_node.next_node
            new_node.next_node = tmp_node.next_node
            tmp_node.next_node = new_node

    def __str__(self):
        values = []
        nodes = self.__head
        while nodes:
            values.append(str(nodes.data))
            nodes = nodes.next_node
        return ('\n'.join(values))
