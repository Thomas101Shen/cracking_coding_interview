from linked_list import LinkedList


def create_linked_list(values):
    ll = LinkedList()
    for value in values:
        ll.append(value)
    return ll

# Test cases
def test_palindrome():
    # Test case: palindrome for an empty list
    ll = LinkedList()
    print("Test: Palindrome for an empty list")
    print(ll.palindrome())  # Should print True (an empty list is considered a palindrome)

    # Test case: palindrome for a single element list
    ll = create_linked_list([1])
    print("Test: Palindrome for a single element list")
    print(ll.palindrome())  # Should print True

    # Test case: palindrome for a list with odd length
    ll = create_linked_list([1, 2, 3, 2, 1])
    print("Test: Palindrome for a list with odd length")
    print(ll.palindrome())  # Should print True

    # Test case: palindrome for a list with even length
    ll = create_linked_list([1, 2, 2, 1])
    print("Test: Palindrome for a list with even length")
    print(ll.palindrome())  # Should print True

    # Test case: non-palindrome list
    ll = create_linked_list([1, 2, 3, 4])
    print("Test: Non-palindrome list")
    print(ll.palindrome())  # Should print False

def test_palindrome_rec():
    # Test case: palindrome for an empty list
    ll = LinkedList()
    print("Test: Palindrome for an empty list")
    print(ll.palindrome_rec())  # Should print True (an empty list is considered a palindrome)

    # Test case: palindrome for a single element list
    ll = create_linked_list([1])
    print("Test: Palindrome for a single element list")
    print(ll.palindrome_rec())  # Should print True

    # Test case: palindrome for a list with odd length
    ll = create_linked_list([1, 2, 3, 2, 1])
    print("Test: Palindrome for a list with odd length")
    print(ll.palindrome_rec())  # Should print True

    # Test case: palindrome for a list with even length
    ll = create_linked_list([1, 2, 2, 1])
    print("Test: Palindrome for a list with even length")
    print(ll.palindrome_rec())  # Should print True

    # Test case: non-palindrome list
    ll = create_linked_list([1, 2, 3, 4])
    print("Test: Non-palindrome list")
    print(ll.palindrome_rec())  # Should print False

# Run the tests
test_palindrome()
print("--------Recursive test is below-------------")
test_palindrome_rec()