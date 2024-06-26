class stack:
    def __init__(self):
        self.list=[]

    def is_empty(self):
        return len(self.list) == 0

    
    def push(self,data):
        self.list.append(data)
        
    
    def pop(self):
        if not self.is_empty():
            self.list.pop( (len(self.list))-1)
        else :
            print("The List Is Blank nothing to pop")

    def peak(self):
        index = len(self.list)-1
        if not self.is_empty():
            print(self.list[index])
        else:
            print("stack is empty nothing to peak")

    def size(self):
        return len(self.list)

mylist= stack()
print(mylist.is_empty())
print(mylist.push(1))
mylist.push(1)
mylist.peak()
print(mylist.size())
print(mylist.pop())
print(mylist.pop())



