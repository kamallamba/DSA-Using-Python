class deque:
    def __init__(self):
        self.items=[]

    def is_empty(self):
        return self.items==[]
    
    def insert_front(self,item):
        self.items.insert(0,item)

    def insert_rare(self,item):
        self.items.append(item)

    def delete_front(self):
        if self.is_empty():
            raise IndexError("the list is empty")
        else:
            self.items.pop(0)

    def delete_rare(self):
        if self.is_empty():
          raise IndexError("deque is empty ")
        else:
            self.items.pop()

    def get_front(self):
        if self.is_empty():
            raise IndexError("The deque is empty")
        else:
            return self.items[0]


        
    def get_rare(self):     
        if self.is_empty():
            raise IndexError("deque is empty ")    
        else:
            return self.items[-1]
            
    def size(self):
        return len(self.items)
d1=deque()
d1.insert_front(20)
d1.insert_front(10)

d1.insert_rare(30)
d1.insert_rare(40)
d1.delete_front()
d1.delete_rare()

print(d1.size())
print("FRONT",d1.get_front(),'END',d1.get_rare())



