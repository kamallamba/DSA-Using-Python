class Node:
    def __init__(self,prev=None,item=None,next=None):
        self.prev = prev
        self.item = item
        self.next = next
        
class CDLL:
    
    def __init__(self,start=None):
        self.start = start
        
    def is_empty(self):
        return self.start == None
    
    def insert_at_start(self,data):
        if not self.is_empty():
            n = Node(self.start.prev,data,self.start)
            self.start.prev.next = n
            self.start.prev = n
            self.start = n
        else:
            n = Node(None,data,None)
            n.prev = n
            n.next = n
            self.start = n
            
    def insert_at_last(self,data):
        if not self.is_empty():
            n = Node(self.start.prev,data,self.start)
            self.start.prev.next = n
            self.start.prev = n
        else:
            n = Node(None,data,None)
            n.prev = n
            n.next = n
            self.start = n
                    
    def search(self,data):
        if not self.is_empty():
            temp = self.start
            while temp.next != self.start:
                if temp.item == data:
                    return temp
                temp = temp.next
            if temp.item == data:
                return temp
        return None
    
    def insert_after(self,temp,data):
        if temp is not None:  
            n = Node(temp,data,temp.next)
            temp.next.prev = n
            temp.next = n  
        else:
            print("NO SUCH NODE")
            
    def print_list(self):
        if not self.is_empty():
            temp = self.start
            while temp.next != self.start:
                print(temp.item,end=" ")
                temp = temp.next
            print(temp.item)
            print()

        else:
            print("NO DATA IN THE LIST TO PRINT")
        
    def delete_first(self):
        if not self.is_empty():
            if self.start.next == self.start:
                self.start = None
            else:
                temp = self.start
                temp.prev.next = temp.next
                temp.next.prev = temp.prev
                self.start = temp.next          
        else:
            print("No item to delete.")
                
    def delete_last(self):
        if not self.is_empty():
            if self.start.next == self.start:
                self.start = None
            else:
                temp = self.start.prev
                temp.prev.next = self.start
                self.start.prev = temp.prev        
        else:
            print("No data to delete")      
                    
    def delete_item(self,data):
        if not self.is_empty ():
            if self.start.next == self.start:
                if self.start.item == data:
                    self.start = None
            else:
                temp = self.start
                if temp.item== data:
                    self.delete_first()
                    return("Item deleted.")
                    
                else:
                    while temp.next != self.start:
                        temp= temp.next
                        if temp.item == data:
                            temp.prev.next =temp.next
                            temp.next.prev= temp.prev
                            return("Item deleted.")
        else:
            print("No Such Data To Delete")


                                   
mylist = CDLL()
mylist.insert_at_start(2)
mylist.insert_at_last(4)
mylist.insert_at_start(1)
mylist.insert_after(mylist.search(2),3)
mylist.insert_at_last(6)
# mylist.delete_first()
# mylist.delete_last()
mylist.delete_item(1)
mylist.print_list()
