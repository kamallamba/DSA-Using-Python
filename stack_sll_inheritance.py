from SLL import*
class stack(sll):
    
    def is_empty(self):
        return super().is_empty()
    
    def push(self,data):
        self.insert_at_start(data)
        self.count+=1
    
    def pop(self):
        if not self.is_empty():
            data = self.start.data
            self.delete_first()
            self.count -=1
            return data
        else:
            raise IndexError("list is empty")
        
    def peek(self):
        if not self.is_empty():
            return self.start.data
        
    def size(self):
        if not self.is_empty():
            return self.count

mylist= stack()
mylist.push(10)
mylist.push(20)
mylist.push(30)
print(mylist.pop())
print(mylist.peek())
print(mylist.size())
