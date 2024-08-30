class Queue:
    def __init__(self,max):
        self.max = max
        self.queue = []
    def enqueue(self,value):
        if self.sizeOfQueue() < self.max:
            self.queue.append(value)
        else:
            print("Queue overflow")
    def dequeue(self):
        if self.sizeOfQueue() > 0:
            return self.queue.pop(0)
        else:
            print("queue underflow")
    def sizeOfQueue(self):
        return len(self.queue)
    def displayQueue(self):
        print(self.queue)
    def front(self):
        return self.queue[0]
    def rear(self):
        return self.queue[self.sizeOfQueue()-1]
        
queue1 = Queue(3)
queue1.enqueue(12)
queue1.displayQueue()
queue1.enqueue(34)
queue1.displayQueue()
print(queue1.front())
print(queue1.rear())
queue1.enqueue(56)
queue1.displayQueue()
queue1.enqueue(321)
queue1.displayQueue()
queue1.dequeue()
queue1.displayQueue()
queue1.dequeue()
queue1.displayQueue()
print(queue1.front())
print(queue1.rear())
queue1.dequeue()
queue1.displayQueue()
queue1.dequeue()
queue1.displayQueue()