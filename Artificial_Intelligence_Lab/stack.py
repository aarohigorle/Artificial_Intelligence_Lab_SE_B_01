# Initialize an empty list to represent the stack
stack = []
def push(item):
    stack.append(item)
    print(f"Pushed: {item}")

def pop():
    if is_empty():
        return "Stack is empty"
    popped_item = stack.pop()
    print(f"Popped: {popped_item}")
    return popped_item

def is_empty():
    return len(stack) == 0

def size():
    return len(stack)

push(10)
push(30)

print(f"Current stack: {stack}")
print(f"Stack size: {size()}")
pop()
print(f"Stack after pop: {stack}")

print(f"Is stack empty? {is_empty()}")
pop()
pop()
print(f"Is stack empty? {is_empty()}")
print(pop()) 
