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

brackets_open = ["{","[","("]
brackets_closed = ["}","]",")"]

def check_expresion(exp):
    stack1 = Stack(100)
    for i in exp:
        if i in brackets_open:
            stack1.push(i)
        elif i in brackets_closed:
            openning = stack1.pop()
            if not brackets_open.index(openning) == brackets_closed.index(i):
                return False
    if stack1.isEmpty():
        return True
    else:
        return False
    

print(check_expresion("r{i(gojdriogm)dg}"))
print(check_expresion("e{w(ub[ndcfo)iwen]c)}"))
