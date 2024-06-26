
class node:
    def __init__ (self,data=None,next=None):
        self.data=data
        self.next = next
        

class sll:
    def __init__(self,start=None):
        self.start = start
        self.count = 0

    
    def is_empty(self):
        return self.start==None
    
    def insert_at_start(self,data):
        n= node(data,self.start)
        self.start= n


    def insert_at_last(self,data):
        n=node(data)
        if self.is_empty():
            self.start = n
        else:
            temp = self.start
            while temp.next is not None:
                temp = temp.next
            temp.next = n
    
    def search(self,data):
        if not self.is_empty():
            temp = self.start
            while temp is not None:
               if temp.data == data :
                    return temp
               temp = temp.next 
        return None
    def insert_after(self,temp,data):
        if temp is  not None:
            n = node(data,temp.next)
            temp.next= n


    def print_list(self):
        temp= self.start
        while temp is not None:
            print(temp.data, end=" ")
            temp = temp.next

    def delete_first(self):
        if self.start is not  None:
            self.start = self.start.next

    def delete_last(self):
        if self.start is None:
            pass
        elif self.start.next is None:
            self.start = None
        else:    
            temp = self.start
            while temp.next.next is not None:
                temp = temp.next
            temp.next = None
    def delete_item (self,data):
        if self.start is None:
            pass
        
        elif self.start.next is None:
            if self.start.data ==  data:
                self.start = None 

        else :
            temp = self.start
            if temp.data == data:
                self.start = temp.next
            else:
                while temp.next is not  None:
                    if temp.next.data == data:
                        temp.next = temp.next.next
                        break

                    temp = temp.next
                    

                
mylist=sll()
mylist.insert_at_start(1)
mylist.insert_at_start(2)
mylist.insert_after(mylist.search(2),3)
mylist.insert_at_last(4)
mylist.delete_item(1)
mylist.print_list()
print(mylist.is_empty())
