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


	def k_to_last_two_pointers(self, k):
		# Calculate size of array then go back to kth to last? (No need maybe do in another implementation)
		# First pointer is k ahead of second pointer
		# When second pointer reaches end of array print first pointer data
		# If second pointer is None then print invalid k to last element and return nothing
		p1 = self.head.next
		p2 = self.head.next
		i = 0

		while i != k:
			if p2 is None:
				print(f"{k} is invalid k to last element")
				return
			else:
				i += 1
				p2 = p2.next

		while p2.next is not None:
			p1 = p1.next
			p2 = p2.next

		print(f"{k} to last element is {p1.data}")


	def k_to_last_rec(self, k):
		def _k_to_last(node, k):
			if node is None:
				return -1, None

			index, result = _k_to_last(node.next, k)

			index += 1

			if index == k:
				return index, node


			return index, result

		index, node = _k_to_last(self.head.next, k)
		
		if node: print(f"{k} to last element is {node.data}")
		else: print(f"{k} is an invalid k to last element for this linkedlist")

	def k_to_last_calc_size(self, k):
		# Calculate size then incriment to size - k

		size = 0
		cur = self.head.next

		while cur != None:
			size += 1
			cur = cur.next

		if k >= size:
			print(f"{k} is invalid k to last")
			return
		else:
			index = 0
			result = self.head.next
			while index != size - k - 1:
				result = result.next
				index += 1
			print(f"{k} to last element is {result.data}")
			return


	def delete_middle_node(self, node):
		# Delete a middle node

		if node is None or node.next == None:
			raise Exception(f"{node} is either an invalid node or an end node")

		print(f"Deleting node: {node.data}")

		next_node = node.next
		node.data = next_node.data
		node.next = next_node.next
		self.size -= 1


	def partition(self, pivot):
		''' 
		Partition array around pivot with smaller elements on left bigger elements
		on the right (unsorted)
		'''

		if self.head.next == None:
			return

		left = LinkedList()
		right = LinkedList()

		it = self.head.next # Iterator
		counter = 0 # Count num of nodes same value as val

		while it != None:
			if it.data < pivot:
				left.append(it.data)
			elif it.data > pivot:
				right.append(it.data)
			else:
				counter += 1
			it = it.next

		while counter > 0:
			left.append(pivot)
			counter -= 1

		# Could improve by adding a tail to linkedlist

		it = right.head.next

		while it != None:
			left.append(it.data)
			it = it.next

		self.head.next = left.head.next

	def partition_optimize_v1(self, pivot: int):

		# This assumes that the linkedlist only contains integers
		# Actual problem states that pivot only needs to be in right side
		# Therefore this will return different values than the previos function

		left_head, right_head = Node(), Node()
		left_tail, right_tail = left_head, right_head

		it = self.head.next

		if it == None: return # If empty list nothing to do, save computing power

		while it != None:
			next_node = it.next # Save next node
			it.next = None # Disconnect current node from the list to save storage

			if it.data < pivot: # If the current node is smaller than
				left_tail.next = it
				left_tail = it
			else:
				right_tail.next = it
				right_tail = it


			it = next_node

		# combine left and right side
		left_tail.next = right_head.next

		# Update original list's head to point to new partitioned list
		self.head.next = left_head.next

	def sum_list(self, A, B, carry: int = 0):
		# Non trivial solution, no converting to str or int and adding and re converting
		# Inputs are reverse lists with unit digit leading
		# ex: 132 is 2 -> 3 -> 1
		if A is None and B is None and carry == 0:
			sum_head = Node()
			return sum_head, sum_head

		total = carry

		if A:
			total += A.data
			A = A.next
		if B:
			total += B.data
			B = B.next

		carry = total // 10
		cur_val = total % 10

		cur_node = Node(cur_val)

		sum_head, prev_node = self.sum_list(A, B, carry)

		prev_node.next = cur_node

		return sum_head, cur_node
		# Can make this a helper function in another function to return
		# just sum_head (see palindrome recursive)

	def sum_list_optimized(self, A, B, carry: int = 0):
		carry = 0
		dummy_head = Node()
		cur = dummy_head

		while A is not None or B is not None or carry != 0: # 56 + 78
			total = carry
			if A:
				total += A.data
				A = A.next
			if B:
				total += B.data
				B = B.next

			cur_val = total % 10
			carry = total // 10

			cur.next = Node(cur_val)
			cur = cur.next
		return self.reverse_ls(dummy_head.next)

	def sum_list_forward(self, A, B, carry: int = 0):

		stackA, stackB = [], []

		while A is not None:
			stackA.append(A.data)
			A = A.next

		while B is not None:
			stackB.append(B.data)
			B = B.next

		carry = 0
		dummy_head = Node()
		cur = dummy_head

		print(f"stackA: {stackA}, stackB: {stackB}, carry: {carry}")


		while stackA or stackB or carry != 0: # 56 + 78
			total = carry			
			if stackA:
				total += stackA.pop()
			if stackB:
				total += stackB.pop()

			cur_val = total % 10
			carry = total // 10

			cur.next = Node(cur_val)
			cur = cur.next
		return self.reverse_ls(dummy_head.next)

	def reverse_ls(self, node):
		prev = None
		current = node

		while current is not None:
			next_node = current.next
			current.next = prev
			prev = current
			current = next_node

		return prev

	def palindrome(self):
		stack = []

		it = self.head.next

		while it is not None:
			stack.append(it.data)
			it = it.next

		it = self.head.next
		while stack:
			char = stack.pop()
			if char != it.data : return False
			it = it.next

		return True

	def palindrome_rec(self):

		is_palindrome, _ = self._palindrome_rec_helper(self.head.next, self.size)
		return is_palindrome

	def _palindrome_rec_helper(self, current, length):
		'''
		This works by going to the middle node
		then using the call stack to compare
		nodes of equal distance from the middle.
		next_node represents a node on the right side
		of the palindrome.
		current node represents a node on the left side of the palindrome.
		If next_node is None then there is no character to match the
		node on the left side with therefore function returns False.
		If next_node is not equal to current node then left side character
		does not match with right side character.
		'''

		if current is None or length == 0: # Evens
			return True, current
		elif length == 1: # Odds
			return True, current.next

		is_palindrome, next_node = self._palindrome_rec_helper(current.next, length - 2)

		if not is_palindrome or next_node is None:
			return False, next_node

		is_palindrome = (current.data == next_node.data)
		return is_palindrome, next_node.next



