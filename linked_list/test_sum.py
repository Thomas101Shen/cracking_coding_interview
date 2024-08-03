from linked_list import LinkedList

def test_sum_list():
    # Helper function to create a linked list from a list of values
    def create_linked_list(values):
        ll = LinkedList()
        for value in values:
            ll.append(value)
        return ll.head.next

    # Test case: sum of two empty lists
    ll1 = LinkedList()
    ll2 = LinkedList()
    result = LinkedList()
    result.head, variable = ll1.sum_list(ll1.head.next, ll2.head.next)
    print("Test: Sum of two empty lists")
    result.print()  # Should print "Empty list"

    # Test case: sum of one empty list and one non-empty list
    ll1 = LinkedList()
    ll2 = LinkedList()
    ll2.append(4)
    ll2.append(3)
    result = LinkedList()
    result.head, variable = ll1.sum_list(ll1.head.next, ll2.head.next)
    print("Test: Sum of one empty list and one non-empty list")
    result.print()  # Should print "3 -> 4"

    # Test case: sum of two non-empty lists with no carryover
    ll1 = LinkedList()
    ll1.append(3)
    ll1.append(2)
    ll2 = LinkedList()
    ll2.append(5)
    ll2.append(4)
    result = LinkedList()
    result.head, variable = ll1.sum_list(ll1.head.next, ll2.head.next)
    print("Test: Sum of two non-empty lists with no carryover")
    result.print()  # Should print "6 -> 8"

    # Test case: sum of two non-empty lists with carryover
    ll1 = LinkedList()
    ll1.append(6)
    ll1.append(5)
    ll2 = LinkedList()
    ll2.append(8)
    ll2.append(7)
    result = LinkedList()
    result.head, variable = ll1.sum_list(ll1.head.next, ll2.head.next)
    print("Test: Sum of two non-empty lists with carryover")
    result.print()  # Should print "2 -> 5 -> 1"

    # Test case: sum of lists with different lengths
    ll1 = LinkedList()
    ll1.append(9)
    ll1.append(9)
    ll1.append(9)
    ll2 = LinkedList()
    ll2.append(1)
    result = LinkedList()
    result.head, variable = ll1.sum_list(ll1.head.next, ll2.head.next)
    print("Test: Sum of lists with different lengths")
    result.print()  # Should print "0 -> 0 -> 0 -> 1"

# Run the tests
test_sum_list()