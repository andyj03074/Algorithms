# Stack

class Stack:

    def __init__(self, capacity):
        self.capacity = capacity
        self.arr = [None] * self.capacity
        self.top = -1

    def isEmpty(self):
        return self.top == -1

    def isFull(self):
        return self.top + 1 == self.capacity

    def push(self, data):
        if (not self.isFull()):
            self.top += 1
            self.arr[self.top] = data

        else:
            print("Stack Overflow!")

    def pop(self):
        if not self.isEmpty():
            data = self.arr[self.top]
            self.top -= 1
            return data
    
        else:
            print("Stack Underflow!")

    def size(self):
        if not self.isEmpty(): return self.top + 1

    def peek(self):
        if not self.isEmpty(): return self.arr[self.top]
        else: 
            print("No Data!")


capacity = int(input())

stack = Stack(capacity)

while(1):
    N = input()
    if N == 'push' :
        stack.push(input())

    elif N == 'pop' :
        print(stack.pop())

    elif N == 'peek' :
        print(stack.peek())

    elif N == 'size' :
        print(stack.size())

    elif N == 'exit' :
        break