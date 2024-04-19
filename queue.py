#Circular Queue

class Queue:
    def __init__(self, capacity) :
        self.capacity = capacity
        self.arr = [None] * capacity
        self.front = 0
        self.rear = 0

    def isEmpty(self) :
        return self.front == self.rear
    
    def isFull(self) :
        return self.front == (self.rear) % self.capacity
    
    def enqueue(self, data):
        if not self.isFull() :
            self.rear = (self.rear + 1) % self.capacity
            self.arr[self.rear] = data
            
        else : print("FULL")

    def dequeue(self) :
        if not self.isEmpty() :
            self.front = (self.front + 1) % self.capacity
            data = self.arr[self.front]
            return data
        
        else : print("EMPTY")

    def size(self) :
        return (self.rear - self.front + self.capacity) % self.capacity
    
    def peek(self) :
        if not self.isEmpty() :
            return self.arr[(self.front + 1) % self.capacity]
        
        else : print("EMPTY")

        

        

        