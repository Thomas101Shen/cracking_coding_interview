from linked_list import LinkedList

def intersect(A: LinkedList, B: LinkedList) -> bool:
	p1 = A.head.next
	p2 = B.head.next

	diff = A.size() - B.size()

	if diff > 0:
		while diff > 0:
			diff -= 1
			p1 = p1.next

	elif diff < 0:
		while diff < 0:
			diff += 1
			p2 = p2.next

	while p1 is not None and p2 is not None:
		if p1 == p2: return True

		p1 = p1.next
		p2 = p2.next

	return False


def create_intersecting_lists(intersection_values, list1_values, list2_values):
    intersecting_list = LinkedList()
    for val in intersection_values:
        intersecting_list.append(val)

    list1 = LinkedList()
    for val in list1_values:
        list1.append(val)
    # Attach the intersecting part
    if list1.head.next:
        tail1 = list1.head
        while tail1.next is not None:
            tail1 = tail1.next
        tail1.next = intersecting_list.head.next

    list2 = LinkedList()
    for val in list2_values:
        list2.append(val)
    # Attach the intersecting part
    if list2.head.next:
        tail2 = list2.head
        while tail2.next is not None:
            tail2 = tail2.next
        tail2.next = intersecting_list.head.next

    if list1.head.next is None and list2.head.next is None and intersecting_list:
    	print("activate")
    	list1.head.next = intersecting_list.head.next
    	list2.head.next = intersecting_list.head.next

    return list1, list2, intersecting_list

def test_intersect():
    # Test case: no intersection
    list1 = LinkedList()
    list2 = LinkedList()
    list1.append(1)
    list1.append(2)
    list1.append(3)
    list2.append(4)
    list2.append(5)
    list2.append(6)
    print("Test: No intersection")
    print("List 1:", end=" ")
    list1.print()
    print("List 2:", end=" ")
    list2.print()
    print("Intersect:", intersect(list1, list2))  # Should print False

    # Test case: intersection
    intersection_values = [7, 8, 9]
    list1_values = [1, 2, 3]
    list2_values = [4, 5]
    list1, list2, _ = create_intersecting_lists(intersection_values, list1_values, list2_values)
    print("\nTest: Intersection")
    print("List 1:", end=" ")
    list1.print()
    print("List 2:", end=" ")
    list2.print()
    print("Intersect:", intersect(list1, list2))  # Should print True

    # Test case: intersection at the head
    intersection_values = [1, 2, 3]
    list1_values = []
    list2_values = []
    list1, list2, _ = create_intersecting_lists(intersection_values, list1_values, list2_values)
    print("\nTest: Intersection at the head")
    print("List 1:", end=" ")
    list1.print()
    print("List 2:", end=" ")
    list2.print()
    print("Intersect:", intersect(list1, list2))  # Should print True

    # Test case: intersection with different lengths
    intersection_values = [10, 11, 12]
    list1_values = [1, 2, 3, 4, 5]
    list2_values = [6, 7]
    list1, list2, _ = create_intersecting_lists(intersection_values, list1_values, list2_values)
    print("\nTest: Intersection with different lengths")
    print("List 1:", end=" ")
    list1.print()
    print("List 2:", end=" ")
    list2.print()
    print("Intersect:", intersect(list1, list2))  # Should print True

    # Test case: one list is empty
    list1 = LinkedList()
    list2 = LinkedList()
    list2.append(1)
    list2.append(2)
    list2.append(3)
    print("\nTest: One list is empty")
    print("List 1:", end=" ")
    list1.print()
    print("List 2:", end=" ")
    list2.print()
    print("Intersect:", intersect(list1, list2))  # Should print False

    # Test case: both lists are empty
    list1 = LinkedList()
    list2 = LinkedList()
    print("\nTest: Both lists are empty")
    print("List 1:", end=" ")
    list1.print()
    print("List 2:", end=" ")
    list2.print()
    print("Intersect:", intersect(list1, list2))  # Should print False

# Run the tests
test_intersect()