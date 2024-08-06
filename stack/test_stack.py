from stack import Stack
if __name__ == "__main__":
    stack = Stack()
    stack.push(10)
    stack.push(20)
    stack.push(30)
    stack.print()  # Should print "30 -> 20 -> 10 -> None"

    print("Popped:", stack.pop())  # Should print "Popped: 30"
    stack.print()  # Should print "20 -> 10 -> None"

    print("Peek:", stack.peek())  # Should print "Peek: 20"
    print("Is stack empty?", stack.isEmpty())  # Should print "Is stack empty? False"

    print("popping from stack")
    print(stack.pop())
    print(stack.pop())
    print("Is stack empty?", stack.isEmpty())  # Should print "Is stack empty? True"

    # Uncommenting the following lines will raise an IndexError
    # stack.pop()
    # stack.peek()