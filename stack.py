# Implementation of simple stack operations
# Last in first out (LIFO)


class Stack:

    # create a stack
    def __init__(self):
        self.stack = []

    # push the data into the stack
    def push(self, data):
        self.stack.append(data)
        return "data pushed into the stack successfully.."

    # pop the last item out
    def pop(self):
        if Stack.isempty(self):
            return "Stack is empty.."
        else:
            ele = self.stack[len(self.stack)-1]
            self.stack.remove(ele)
            return ele

    # return the last item
    def peek(self):
        if Stack.isempty(self):
            return "Stack is empty"
        else:
            return self.stack[len(self.stack)-1]

    # Check the stack is empty or not
    def isempty(self):
        return len(self.stack) == 0

    # return the length of the stack
    def len(self):
        return len(self.stack)

    # return the stack
    def find(self):
        return self.stack


st = Stack()

print st.push(1)
print st.push(2)
print st.push(3)

print st.pop()

print st.peek()

print st.isempty()

print st.len()

print st.find()

