class Stack:
    
    def __init__(self):
        self.pila = []
    
    def push(self, item):
        self.pila.append(item)
        
    def pop(self):
        if self.pila == []:
            return "Stack Empty"
        return self.pila.pop()
    def peek(self):
        if self.pila == []:
            return "Stack Empty"
        return self.pila[-1]

 
s = Stack()
s.push(10)
s.push(20)
print(s.peek())  # Output: 20
print(s.pop())   # Output: 20
print(s.pop())   # Output: 10
print(s.pop())   # Output: "Stack is empty"    
        