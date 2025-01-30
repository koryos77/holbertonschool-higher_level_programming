#!/usr/bin/python3
"""
Module that defines a class Square.
This module contains the definition of Square with an attribute 'size'
"""


class Node:
    """
    Class that defines a node of a singly linked list.

    Attributes:
        data (int): The data stored in the node.
        next_node (Node or None): The next node in the list,
        or None if it's the last node.
    """

    def __init__(self, data, next_node=None):
        """
        Initializes a new Node with the given data and next_node.

        Args:
            data (int): The value to store in the node.
            next_node (Node or None): The next node in
            the list (default is None).
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """
        Retrieves the data stored in the node.

        Returns:
            int: The data stored in the node.
        """
        return self._data

    @data.setter
    def data(self, value):
        """
        Sets the data for the node, ensuring it's an integer.

        Args:
            value (int): The value to store in the node.

        Raises:
            TypeError: If the value is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self._data = value

    @property
    def next_node(self):
        """
        Retrieves the next node linked to the current node.

        Returns:
            Node or None: The next node, or None if it's the last node.
        """
        return self._next_node

    @next_node.setter
    def next_node(self, value):
        """
        Sets the next node for the current node,
        ensuring it's either None or a Node.

        Args:
            value (Node or None): The next node to link to.

        Raises:
            TypeError: If the value is not a Node object or None.
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self._next_node = value


class SinglyLinkedList:
    """
    Class that defines a singly linked list.

    Attributes:
        head (Node or None): The first node in the list,
        or None if the list is empty.
    """

    def __init__(self):
        """
        Initializes an empty singly linked list.
        """
        self.head = None

    def __str__(self):
        """
        Creates a string representation of the singly linked list.

        Returns:
            str: A string where each node's data is printed on a new line.
        """
        result = []
        current_node = self.head
        while current_node is not None:
            result.append(str(current_node.data))
            current_node = current_node.next_node
        return "\n".join(result)

    def sorted_insert(self, value):
        """
        Inserts a new node with the given value into the list in sorted order.

        Args:
            value (int): The value to insert into the list.

        The method ensures that the list remains sorted in increasing order
        after the insertion.
        """
        new_node = Node(value)
        if self.head is None or self.head.data >= value:
            new_node.next_node = self.head
            self.head = new_node
        else:
            current = self.head
            while (current.next_node is not None and
                   current.next_node.data < value):
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node
