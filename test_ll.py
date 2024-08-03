from linked_list import LinkedList

# Test cases
ll = LinkedList()
ll.print()  # Should print "Empty list"

# Append test
print("----Append test-----")
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)
ll.append(5)
ll.print()  # Should print "1 -> 2 -> 3 -> 4 -> 5"

# Delete test
print("----Delete test-----")
ll.delete(3)
ll.print()  # Should print "1 -> 2 -> 4 -> 5"
ll.delete(6)  # Should print "6 not found in list"

# Remove duplicates O(N) test
print("----O(N) remove duplicates test-----")
ll.append(4)
ll.append(2)
ll.print()  # Should print "1 -> 2 -> 4 -> 5 -> 4 -> 2"
ll.remove_dups_on()
ll.print()  # Should print "1 -> 2 -> 4 -> 5"
print("size: ", ll.size)

# Remove duplicates O(N^2) test
print("----O(N^2) remove duplicates test-----")
ll.append(2)
ll.append(4)
ll.print()  # Should print "1 -> 2 -> 4 -> 5 -> 2 -> 4"
ll.remove_dups_onsquare()
ll.print()  # Should print "1 -> 2 -> 4 -> 5"
print("size: ", ll.size)

# Kth to last element test
print("----kth to last element test----")
ll.k_to_last_size(0)  # Should print "5"
ll.k_to_last_size(2)  # Should print "2"
ll.k_to_last_size(5)  # Should print "Invalid kth to last"

