class Node:
    def __init__(self,val):
        self.info = val
        self.left = None
        self.right = None
    def insert(self, val):

        if val < self.info:
            if self.left is None:
                self.left = Node(val)
            else:
                self.left.insert(val)
        elif val > self.info:
            if self.right is None:
                self.right = Node(val)
            else:
                self.right.insert(val)
    def inOrder(self):
        if self.left:
            self.left.inOrder()
        print (self.info, end=" "),
        if self.right:
            self.right.inOrder()
    def preOrder(self):
        print(self.info, end=" "),
        if self.left:
            self.left.preOrder()
        if self.right:
            self.right.preOrder()
    def postOrder(self):
        if self.left:
            self.left.postOrder()
        if self.right:
            self.right.postOrder()
        print(self.info, end=" "),
    def search(self,val):
        if val < self.info:
            if self.left is None:
                return None
            else:
               return self.left.search(val)
        elif val > self.info:
            if self.right is None:
                    return None
            else:
                return self.right.search(val)
        else:
            return True

    def height(self):
        a = 0
        b = 0
        if self.left:
            a = 1+self.left.height()
        if self.right:
            b = 1+self.right.height()
        if a > b:
            return a
        else:
            return b

    # def levelOrder(self):
BT = Node(23) #Root
BT.insert(10)
BT.insert(16)
BT.insert(19)
BT.insert(65)
BT.insert(45)
BT.insert(24)
BT.insert(50)
BT.insert(67)
BT.inOrder()
print(" ")
BT.postOrder()
print(" ")
BT.preOrder()
print(" ")
print(BT.search(24))
print(BT.search(1))
print(BT.search(242131))
print(BT.height())
