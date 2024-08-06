class QueueNode:
	def __init__(self, data = None):
		self.data = data
		self.next = None

class Queue:

	def __init__(self):
		self.front = None
		self.rear = None
		self._size = 0

	def size(self):
		return self._size

	def enqueue(self, data):
		new_node = Node(data)
		if self.rear is None: # If queue is empty
			self.front = self.rear = new_node
		else:
			new_node.next = self.rear
			self.rear = new_node
		self._size += 1

	def dequeue(self, data):

		if self.rear is None:
			raise IndexError("Dequeue from empty queue")

		node_removed