# Problem: Design Linked List - https://leetcode.com/problems/design-linked-list/

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.head = None

    def get(self, index: int) -> int:
        if not self.head or index < 0:
            return -1
        current_node = self.head
        while current_node and index:
            current_node = current_node.next
            index -= 1
        return current_node.val if current_node else -1

    def addAtHead(self, val: int) -> None:
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node

    def addAtTail(self, val: int) -> None:
        new_node = Node(val)
        if not self.head:
            self.head = new_node
            return
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        current_node.next = new_node

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0:
            return
        new_node = Node(val)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
            return
        current_node = self.head
        prev = None
        while current_node and index:
            prev = current_node
            current_node = current_node.next
            index -= 1
        if not current_node and index > 0:
            return
        prev.next = new_node
        new_node.next = current_node

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or not self.head:
            return
        if index == 0:
            self.head = self.head.next
            return
        current_node = self.head
        prev = None
        while current_node and index:
            prev = current_node
            current_node = current_node.next
            index -= 1
        if not current_node:
            return
        prev.next = current_node.next
