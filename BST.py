class node:
    def __init__(self,item=None,left=None,right=None):
        self.item=item
        self.left=left
        self.right=right

class BST:
    def __init__(self):
        self.root=None

    def insert(self,data):
        self.root= self.rinsert(self.root,data)
    def rinsert(self,root,data):
        if root is None:
            return node(data)
        if data > root.item:
            root.right= self.rinsert(root.right,data)
        elif data< root.item:
            root.left = self.rinsert(root.left,data)
        return root
        
        
    def search(self,data):
        return self.rsearch(self.root,data)
    def rsearch(self,root,data):
        if root:
            if root.item== data :
                return root
            elif data<root.item:
                root.left=self.rsearch(root.left,data)
            elif data>root.item:
                root.right= self.rsearch(root.right,data)
        return root
    
    def inorder(self):
        result=[]
        self.rinorder(self.root,result)
        return result
    def rinorder(self,root,result):
        if root:
            self.rinorder (root.left,result)
            result.append(root.item)
            self.rinorder(root.right,result)

    def postorder(self):
        result=[]
        self.rinorder(self.root,result)
        return result
    def rpostorder(self,root,result):
        if root:
            result.append(root.item)
            self.rinorder (root.left,result) 
            self.rinorder(root.right,result)



