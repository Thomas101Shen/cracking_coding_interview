class Node:
	def __init__(self, data=None):
		self.next = None
		self.data = data

class LinkedList():

	def __init__(self):
		self.head = Node()
		self.size = 0

	def append(self, d):
		end = Node(d)
		n = self.head
		self.size += 1

		while n.next != None:
			n = n.next
		n.next = end

	def print(self):
		if self.head.next is None:
			print("Empty list")
			return

		n = self.head.next

		while n != None:
			if n.next != None: print(n.data, "->", end = ' ')
			else: print(n.data)
			n = n.next

	def delete(self, d):
		n = self.head

		while n.next is not None:
			if n.next.data == d:
				n.next = n.next.next
				self.size -= 1
				print(f"Deleted {d}")
				return
			n = n.next

		print(f"{d} not found in list")

	def remove_dups_on(self):
		dup_tracker = set()
		n = self.head

		while n.next != None:
			print(f"{n.next.data}---")
			if n.next.data in dup_tracker:
				print("deleting^")
				n.next = n.next.next
				self.size -= 1
			else:
				dup_tracker.add(n.next.data)
				n = n.next

	def remove_dups_onsquare(self):
		n = self.head.next

		while n.next != None:
			print(f"{n.data}---")
			m = n
			while m.next != None:
				if n.data == m.next.data:
					m.next = m.next.next
					self.size -= 1
				else:
					m = m.next
			if n != None: n = n.next

	def k_to_last_size(self, k):
		if k > self.size:
			print("invalid kth to last")
			return
		count = 0
		n = self.head
		while count != self.size - k:
			# print(f"{count}, {self.size - 1 - k}")
			# print(f"current node: {n.data}")
			count += 1
			n = n.next
		print(n.data)

	
	# Create recursive and iterative solution ^




