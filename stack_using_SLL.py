from sll import *

class stack:
    def __init__(self):
        self.mylist = sll()
        self.count = 0

    def is_empty(self):
        return self.mylist.is_empty()
    
    def push(self,data):
        self.mylist.insert_at_start(data)
        self.count +=1

    def pop(self):
        
        if not self.is_empty():
            data = self.mylist.start.data
            self.mylist.delete_first()
            self.count -=1
            return data
        else:
            raise IndexError("stack is empty")
        
    def peek(self):
        if not self.is_empty():
          return self.mylist.start.data

    def size(self):
        return self.count
    
s = stack()
s.is_empty()
s.push(10)
s.push(20)
s.push(30)
s.pop()
print(s.size())
print(s.peek())

