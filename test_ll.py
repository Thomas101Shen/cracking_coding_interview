from linked_list import LinkedList

def test_linked_list():
    # Initialize LinkedList
    ll = LinkedList()

    # Test printing empty list
    print("Test: Print empty list")
    ll.print()  # Should print "Empty list"

    # Test appending elements
    print("\nTest: Append elements")
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.append(4)
    ll.append(5)
    ll.print()  # Should print "1 -> 2 -> 3 -> 4 -> 5"

    # Test deleting an element
    print("\nTest: Delete element 3")
    ll.delete(3)
    ll.print()  # Should print "1 -> 2 -> 4 -> 5"
    
    print("\nTest: Delete element 6 (non-existent)")
    ll.delete(6)  # Should print "6 not found in list"

    # Test removing duplicates (O(N))
    print("\nTest: Remove duplicates (O(N))")
    ll.append(4)
    ll.append(2)
    ll.print()  # Should print "1 -> 2 -> 4 -> 5 -> 4 -> 2"
    ll.remove_dups_on()
    ll.print()  # Should print "1 -> 2 -> 4 -> 5"

    # Test removing duplicates (O(N^2))
    print("\nTest: Remove duplicates (O(N^2))")
    ll.append(2)
    ll.append(4)
    ll.print()  # Should print "1 -> 2 -> 4 -> 5 -> 2 -> 4"
    ll.remove_dups_onsquare()
    ll.print()  # Should print "1 -> 2 -> 4 -> 5"

    # Test k-th to last element (size based)
    print("\nTest: k-th to last element (size based)")
    ll.k_to_last_size(0)  # Should print "5"
    ll.k_to_last_size(2)  # Should print "2"
    ll.k_to_last_size(5)  # Should print "invalid kth to last"

    # Test k-th to last element (two pointers)
    print("\nTest: k-th to last element (two pointers)")
    ll.k_to_last_two_pointers(0)  # Should print "0 to last element is 5"
    ll.k_to_last_two_pointers(2)  # Should print "2 to last element is 2"
    ll.k_to_last_two_pointers(5)  # Should print "5 is invalid k to last element"

    # Test k-th to last element (recursive)
    print("\nTest: k-th to last element (recursive)")
    ll.k_to_last_rec(0)  # Should print "0 to last element is 5"
    ll.k_to_last_rec(2)  # Should print "2 to last element is 2"
    ll.k_to_last_rec(5)  # Should print "5 is an invalid k to last element for this linkedlist"

    # Test k-th to last element (calculate size)
    print("\nTest: k-th to last element (calculate size)")
    ll.k_to_last_calc_size(0)  # Should print "0 to last element is 5"
    ll.k_to_last_calc_size(2)  # Should print "2 to last element is 2"
    ll.k_to_last_calc_size(5)  # Should print "5 is an invalid k to last

def test_delete_middle_node():
    # Initialize LinkedList
    ll = LinkedList()

    # Test case: delete middle node from an empty list (should raise an exception)
    try:
        print("Test: Delete node from an empty list")
        ll.delete_middle_node(None)
    except Exception as e:
        print(e)  # Should print an exception message

    # Test case: delete the last node (should raise an exception)
    ll.append(1)
    last_node = ll.head.next
    try:
        print("\nTest: Delete the last node")
        ll.delete_middle_node(last_node)
    except Exception as e:
        print(e)  # Should print an exception message

    # Test case: delete a middle node in a list with multiple elements
    ll.append(2)
    ll.append(3)
    ll.append(4)
    ll.append(5)
    ll.print()  # Should print "1 -> 2 -> 3 -> 4 -> 5"

    middle_node = ll.head.next.next  # This is the node with value 3
    print("\nTest: Delete a middle node (3)")
    ll.delete_middle_node(middle_node)
    ll.print()  # Should print "1 -> 2 -> 4 -> 5"

    # Test case: delete another middle node
    middle_node = ll.head.next.next  # This is the node with value 4
    print("\nTest: Delete another middle node (4)")
    ll.delete_middle_node(middle_node)
    ll.print()  # Should print "1 -> 2 -> 5"

    # Test case: delete a node in a list with two elements
    ll2 = LinkedList()
    ll2.append(10)
    ll2.append(20)
    ll2.print()  # Should print "10 -> 20"

    middle_node = ll2.head.next  # This is the node with value 10
    print("\nTest: Delete a node in a list with two elements (10)")
    ll2.delete_middle_node(middle_node)
    ll2.print()  # Should print "20"

def test_partition():
    # Initialize LinkedList
    ll = LinkedList()

    # Test case: partition an empty list (should remain empty)
    print("Test: Partition an empty list")
    ll.partition(3)
    ll.print()  # Should print "Empty list"

    # Test case: partition a list with one element (should remain unchanged)
    ll.append(1)
    print("\nTest: Partition a list with one element")
    ll.partition(3)
    ll.print()  # Should print "1"

    # Test case: partition a list where all elements are less than the pivot
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(1)
    print("\nTest: Partition a list where all elements are less than the pivot")
    ll.partition(3)
    ll.print()  # Should print "1 -> 2 -> 1"

    # Test case: partition a list where all elements are greater than the pivot
    ll = LinkedList()
    ll.append(4)
    ll.append(5)
    ll.append(6)
    print("\nTest: Partition a list where all elements are greater than the pivot")
    ll.partition(3)
    ll.print()  # Should print "4 -> 5 -> 6"

    # Test case: partition a list with elements both less than and greater than the pivot
    ll = LinkedList()
    ll.append(3)
    ll.append(5)
    ll.append(8)
    ll.append(5)
    ll.append(10)
    ll.append(2)
    ll.append(1)
    print("\nTest: Partition a list with elements both less than and greater than the pivot")
    ll.partition(5)
    ll.print()  # Should print "3 -> 2 -> 1 -> 5 -> 5 -> 8 -> 10"

    # Test case: partition a list with elements equal to the pivot
    ll = LinkedList()
    ll.append(5)
    ll.append(5)
    ll.append(5)
    ll.append(5)
    ll.append(5)
    ll.append(5)
    ll.append(5)
    print("\nTest: Partition a list with elements equal to the pivot")
    ll.partition(5)
    ll.print()  # Should print "5 -> 5 -> 5 -> 5 -> 5 -> 5 -> 5"

    # Test case: partition a list where pivot is the smallest element
    ll = LinkedList()
    ll.append(5)
    ll.append(8)
    ll.append(10)
    ll.append(2)
    ll.append(1)
    print("\nTest: Partition a list where pivot is the smallest element")
    ll.partition(1)
    ll.print()  # Should print "1 -> 5 -> 8 -> 10 -> 2"

    # Test case: partition a list where pivot is the largest element
    ll = LinkedList()
    ll.append(5)
    ll.append(8)
    ll.append(10)
    ll.append(2)
    ll.append(1)
    print("\nTest: Partition a list where pivot is the largest element")
    ll.partition(10)
    ll.print()  # Should print "5 -> 8 -> 2 -> 1 -> 10"



# Run the tests
test_linked_list()
test_delete_middle_node()
test_partition()

