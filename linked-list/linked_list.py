class Node:
    def __init__(self, value, prev_node, next_node):
        self.value = value
        self.prev_node = prev_node
        self.next_node = next_node


class LinkedList:
    def __init__(self):
        self.first_node = None
        self.last_node = None
        self.length = 0

    def push(self, number):
        if self.last_node:
            self.last_node.next_node = Node(number, self.last_node, None)
            self.last_node = self.last_node.next_node
        else:
            self.first_node = self.last_node = Node(number, None, None)
        self.length += 1

    def pop(self):
        if self.last_node:
            value = self.last_node.value
            if self.last_node.prev_node:
                self.last_node = self.last_node.prev_node
                self.last_node.next_node = None
            else:
                self.first_node = self.last_node = None
            self.length -= 1
            return value
        else:
            raise IndexError("Linked list is empty.")

    def unshift(self, number):
        if self.first_node:
            self.first_node.prev_node = Node(number, None, self.first_node)
            self.first_node = self.first_node.prev_node
        else:
            self.first_node = self.last_node = Node(number, None, None)
        self.length += 1

    def shift(self):
        if self.first_node:
            value = self.first_node.value
            if self.first_node.next_node:
                self.first_node = self.first_node.next_node
                self.first_node.prev_node = None
            else:
                self.first_node = self.last_node = None
            self.length -= 1
            return value
        else:
            raise IndexError("Linked list is empty.")

    def __len__(self):
        return self.length

    def __iter__(self):
        index = self.first_node
        while index:
            yield index.value
            index = index.next_node
