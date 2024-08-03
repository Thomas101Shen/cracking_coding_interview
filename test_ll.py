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

# Run the tests
test_linked_list()
