# Function to insert an element at the bottom of a stack
def insert_at_bottom(stack, item):
    if not stack:  # If stack is empty, push the item
        stack.append(item)
    else:
        # Pop all elements to reach the bottom
        temp = stack.pop()
        insert_at_bottom(stack, item)
        # Push back the popped elements
        stack.append(temp)

# Function to reverse the stack
def reverse_stack(stack):
    if stack:
        # Pop the top element
        temp = stack.pop()
        # Reverse the remaining stack
        reverse_stack(stack)
        # Insert the popped element at the bottom
        insert_at_bottom(stack, temp)

# Example usage:
stack = [1, 2, 3, 4, 5]
reverse_stack(stack)
print(stack)  # Output should be [5, 4, 3, 2, 1]
