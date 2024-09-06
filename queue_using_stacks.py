class Stack:
    def __init__(self,max):
        self.max = max
        self.stack = []
    def push(self,value):
        if len(self.stack) < self.max:
            self.stack.append(value)
        else:
            print("stack overflow")

    def pop(self):
        if not self.isEmpty():
            return self.stack.pop() 
        else:
            print("stack underflow")

    def isEmpty(self):
        if len(self.stack) == 0:
            return True
        else:   
            return False
    
    def top(self):
        return self.stack[-1]
 
    def showstack(self):
        print(self.stack)

    def size(self):
        return len(self.stack)

class Queue:
    def __init__(self,max):
        self.max = max
        self.queue = Stack(max)
        self.temStack = Stack(max)
    def enqueue(self,value):
        if self.queue.size() < self.max:
            while not self.queue.isEmpty():
                self.temStack.push(self.queue.pop())
            self.queue.push(value)
            while not self.temStack.isEmpty():
                self.queue.push(self.temStack.pop())
        else:
            print("queue is full")

    def dequeue(self):
        if self.queue.size() > 0:
            return self.queue.pop()
        else:
            print("underflow")

    def displayQueue(self):
        self.queue.showstack()

queue1 = Queue(3)
queue1.enqueue(12)
queue1.displayQueue()
queue1.enqueue(34)
queue1.displayQueue()
queue1.enqueue(56)
queue1.displayQueue()
queue1.enqueue(321)
queue1.displayQueue()
queue1.dequeue()
queue1.displayQueue()
queue1.dequeue()
queue1.displayQueue()
queue1.dequeue()
queue1.displayQueue()
queue1.dequeue()
queue1.displayQueue()