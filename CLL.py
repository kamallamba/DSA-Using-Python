class Node:
    def __init__(self,item=None,next=None):
        self.item = item
        self.next = next
        
class CLL:
    def __init__(self,last=None):
        self.last = last
        
    def is_empty(self):
        return self.last == None
    
    def insert_at_start(self,data):
        n = Node(data)
        if not self.is_empty():
            n.next = self.last.next
            self.last.next = n
        else:
            self.last = n
            self.last.next = self.last
                 
    def insert_at_last(self,data):
        n = Node(data)
        if not self.is_empty():
            n.next = self.last.next
            self.last.next = n
            self.last = n
        else:
            self.last = n
            self.last.next = self.last
        
    def search(self,data):
        if not self.is_empty():
            temp = self.last.next
            while temp != self.last:
                if temp.item == data:
                    return temp
                temp = temp.next
            if temp.item == data:
                return temp
        return None
    
    def insert_after(self,temp,data):
        if temp is not None:
            n = Node(data,temp.next)
            temp.next = n
            if temp == self.last:
                self.last = n
            
    def print_list(self):
        if not self.is_empty():
            temp = self.last.next
            while temp != self.last:
                print(temp.item,end=' ')
                temp = temp.next
            print(temp.item)
            
    def delete_first(self):
        if not self.is_empty():
            temp = self.last.next
            if temp == self.last:
                self.last = None
            else:
                self.last.next = self.last.next.next
                
    def delete_last(self):
        if not self.is_empty():
            if self.last.next == self.last:
                self.last = None
            else:
                temp = self.last.next
                while temp.next != self.last:
                    temp = temp.next
                temp.next = self.last.next
                self.last = temp
        
    def delete_item(self,data):
        if not self.is_empty():
            if self.last.next == self.last:
                if self.last.item == data:
                    self.last = None
            else:
                if self.last.next.item == data:
                    self.delete_first()
                else:
                    temp = self.last.next
                    while temp != self.last:
                        if temp.next == self.last:
                            if self.last.item == data:
                                self.delete_last()
                                break
                            if temp.next.item == data:
                                temp.next = temp.next.next
                                break
                            temp = temp.next                       
                        
        else:
            print("No such data to delete")                
                       
                        
                    
                
mylist = CLL()
mylist.insert_at_start(10)
mylist.insert_at_last(20)
mylist.insert_after(mylist.search(10),15)
mylist.delete_item(15)


mylist.print_list()
