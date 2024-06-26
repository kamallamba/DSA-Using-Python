class Queue:
    def __init__(self):
        self.myqueue = []
        self.count = 0
    
    def is_empty(self):
        return len(self.myqueue) == 0
    
    def enqueue(self,data):
        self.myqueue.insert(0,data)
        self.count += 1
        
    def print_queue(self):
        if not self.is_empty():
            for i in reversed(self.myqueue):
                print(i,end=" ")   
        else:
            raise IndexError("Empty Queue")
        print() 
          
    def dequeue(self):
        if not self.is_empty():
            self.count -= 1
            return self.myqueue.pop(-1)
            
        else:
            raise IndexError("No data in the Queue")
        
    def get_front(self):
        if not self.is_empty():
            return self.myqueue[-1]
        else:
            raise IndexError("No data in the Queue")
        
    def get_rear(self):
        if not self.is_empty():
            return self.myqueue[0]
        
    def size(self):
        return self.count
    
    
a = Queue()
a.enqueue(1)
a.enqueue(2)
a.enqueue(3)
a.enqueue(4)
a.enqueue(5)
a.dequeue()
print(a.get_front())
print(a.get_rear())

a.print_queue()
print(a.size())



q1= Queue()
try:
    print(q1.get_front())
except IndexError as  e:
    print (e.args[0])

q1.enqueue(10)
q1.enqueue(20)
q1.enqueue(30)
q1.enqueue(40)
q1.enqueue(50)
print('front',q1.get_front(),'rear',q1.get_rear())
