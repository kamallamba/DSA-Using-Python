class Node:
    def __init__(self,prev=None,data=None,next=None):
        self.prev=prev
        self.data=data
        self.next=next
class Deque:
    def __init__(self):
        self.front=None
        self.rear=None
        self.item_count=0

    def is_empty(self):
        return self.front==None
    
    def insert_front(self,data):
        n=Node(None,data,self.front)
        if self.is_empty():
            self.rear=n
        else:
            self.front.prev=n
        self.front=n 
        self.item_count+=1          
        
    def insert_rear(self,data):
        n = Node(self.rear,data,None)
        if self.is_empty():
            self.front=n
            
        else:
            self.rear.next=n
        self.rear=n
        self.item_count+=1   

    def delete_front(self):
        if self.is_empty():
            raise IndexError("Nothing to delete in Deque")
        if self.front == self.rear:
            self.front=None
            self.rear=None

        else:
            self.front=self.front.next
            self.front.prev=None
        self.item_count-=1   

    def delete_rear(self):
        if self.is_empty():
            raise IndexError("Nothing to delete in Deque")

        if self.front == self.rear:
            self.front=None
            self.rear=None
        else:
            self.rear =self.rear.prev     
            self.rear.next=None
        self.item_count-=1   

    def get_front(self):
            if self.is_empty():
                raise IndexError("Nothing to delete in Deque")
            else:
                return self.front.data
        
    def get_rear(self):
            if self.is_empty():
                raise IndexError("Nothing to delete in Deque")
            else:
                return self.rear.data
    def size(self):
        return self.item_count
    


d= Deque()
d.insert_front(10)
d.insert_front(20)
d.insert_rear(30)
d.insert_rear(40)
print("first",d.get_front(),"END",d.get_rear())
d.delete_front()
d.delete_rear()
print("first",d.get_front(),"END",d.get_rear())
print(d.size())