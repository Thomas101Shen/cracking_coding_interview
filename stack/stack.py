class Node:
	def __init__(self, data = None):
		self.next = None
		self.data = data


class Stack:

	def __init__(self):
		self.head = None

	def isEmpty(self) -> bool:
		return self.head is None

	def push(self, data):
		new_node = Node(data)
		new_node.next = self.head
		self.head = new_node

	def pop(self):
		if self.isEmpty():
			raise IndexError("pop from empty stack")
		popped_node = self.head
		self.head = self.head.next
		return popped_node.data

	def peek(self):
		if self.isEmpty():
			raise IndexError("peek from empty stack")
		return self.head.data

	def print(self):
		current = self.head
		while current is not None:
			print(current.data, end = "->")
			current = current.next
		print("None")