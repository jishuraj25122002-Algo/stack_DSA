# Stack Implementation using Python List

stack = []

while True:
    print("\n----- STACK MENU -----")
    print("1. Push")
    print("2. Pop")
    print("3. Peek")
    print("4. Display")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    # Push Operation
    if choice == 1:
        item = input("Enter element to push: ")
        stack.append(item)
        print(item, "pushed into the stack.")

    # Pop Operation
    elif choice == 2:
        if len(stack) == 0:
            print("Stack Underflow! Stack is empty.")
        else:
            item = stack.pop()
            print(item, "popped from the stack.")

    # Peek Operation
    elif choice == 3:
        if len(stack) == 0:
            print("Stack is empty.")
        else:
            print("Top element is:", stack[-1])

    # Display Operation
    elif choice == 4:
        if len(stack) == 0:
            print("Stack is empty.")
        else:
            print("Stack elements (Top to Bottom):")
            
            # Brute force traversal
            for i in range(len(stack) - 1, -1, -1):
                print(stack[i])

    # Exit
    elif choice == 5:
        print("Exiting the program...")
        break

    else:
        print("Invalid choice! Please try again.")