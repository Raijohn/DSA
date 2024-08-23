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

stack1  = Stack(3)
stack1.push(2)
stack1.showstack()

stack1.push(5)
stack1.showstack()

stack1.push(9)
stack1.showstack()

print(stack1.top())

stack1.push(91)
stack1.showstack()

for i in range(4):
    print(stack1.pop())
    stack1.showstack()