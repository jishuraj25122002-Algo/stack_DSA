# Stack implementation using Python List

stack = []

while True:
    print("\n----- STACK MENU -----")
    print("1. Push")
    print("2. Pop")
    print("3. Peek")
    print("4. Display")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    # Push element
    if choice == 1:
        item = input("Enter the element: ")
        stack.append(item)
        print(item, "is pushed into the stack.")

    # Pop element
    elif choice == 2:
        if len(stack) == 0:
            print("Stack is empty!")
        else:
            print(stack.pop(), "is popped from the stack.")

    # Peek top element
    elif choice == 3:
        if len(stack) == 0:
            print("Stack is empty!")
        else:
            print("Top element is:", stack[-1])

    # Display stack
    elif choice == 4:
        if len(stack) == 0:
            print("Stack is empty!")
        else:
            print("Stack elements:", stack)

    # Exit program
    elif choice == 5:
        print("Program closed.")
        break

    else:
        print("Invalid choice! Please try again.")