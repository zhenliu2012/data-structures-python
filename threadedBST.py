
# coding: utf-8




class BinarySearchTree:

    def __init__(self):
        self.root = None
        self.size = 0

    def length(self):
        return self.size

    def __len__(self):
        return self.size

    def put(self,key,val):
        if self.root:
            self._put(key,val,self.root)
        else:
            self.root = TreeNode(key,val)
        self.size = self.size + 1

    def _put(self,key,val,currentNode):
        if key < currentNode.key:
            if currentNode.hasLeftChild():
                self._put(key,val,currentNode.leftChild)
            else:
                currentNode.leftChild = TreeNode(key,val,parent=currentNode)
        elif key == currentNode.key: # replace node data if the key is already in the BST
            currentNode.replaceNodeData(key, 
                                        val, 
                                        currentNode.leftChild, 
                                        currentNode.rightChild)
        else:
            if currentNode.hasRightChild():
                self._put(key,val,currentNode.rightChild)
            else:
                currentNode.rightChild = TreeNode(key,val,parent=currentNode)
                
    def __setitem__(self,k,v):
        self.put(k,v)
        self.setThread()

    def get(self,key):
        if self.root:
            res = self._get(key,self.root)
            if res:
                  return res.payload
            else:
                  return None
        else:
            return None

    def _get(self,key,currentNode):
        if not currentNode:
            return None
        elif currentNode.key == key:
            return currentNode
        elif key < currentNode.key:
            return self._get(key,currentNode.leftChild)
        else:
            return self._get(key,currentNode.rightChild)

    def __getitem__(self,key):
        return self.get(key)

    def __contains__(self,key):
        if self._get(key,self.root):
            return True
        else:
            return False

    def delete(self,key):
        if self.size > 1:
            nodeToRemove = self._get(key,self.root)
            if nodeToRemove:
                self.remove(nodeToRemove)
                self.size = self.size-1
            else:
                 raise KeyError('Error, key not in tree')
        elif self.size == 1 and self.root.key == key:
            self.root = None
            self.size = self.size - 1
        else:
             raise KeyError('Error, key not in tree')

    def __delitem__(self,key):
        self.delete(key)
        self.setThread()
        
    def remove(self,currentNode):
        if currentNode.isLeaf(): #leaf
            if currentNode == currentNode.parent.leftChild:
                currentNode.parent.leftChild = None
            else:
                currentNode.parent.rightChild = None
        elif currentNode.hasBothChildren(): #interior
            succ = currentNode.findSuccessor()
            succ.spliceOut()
            currentNode.key = succ.key
            currentNode.payload = succ.payload

        else: # this node has one child
            if currentNode.hasLeftChild():
                if currentNode.isLeftChild():
                    currentNode.leftChild.parent = currentNode.parent
                    currentNode.parent.leftChild = currentNode.leftChild
                elif currentNode.isRightChild():
                    currentNode.leftChild.parent = currentNode.parent
                    currentNode.parent.rightChild = currentNode.leftChild
                else:
                     currentNode.replaceNodeData(currentNode.leftChild.key,
                                    currentNode.leftChild.payload,
                                    currentNode.leftChild.leftChild,
                                    currentNode.leftChild.rightChild)
            else:
                if currentNode.isLeftChild():
                    currentNode.rightChild.parent = currentNode.parent
                    currentNode.parent.leftChild = currentNode.rightChild
                elif currentNode.isRightChild():
                    currentNode.rightChild.parent = currentNode.parent
                    currentNode.parent.rightChild = currentNode.rightChild
                else:
                    currentNode.replaceNodeData(currentNode.rightChild.key,
                                    currentNode.rightChild.payload,
                                    currentNode.rightChild.leftChild,
                                    currentNode.rightChild.rightChild)

    def inorder_nonrecur( self ):
        curr = self.root
        if curr == None:
            return
        else:
            curr = curr.findMin()
            print( curr.key )
        while curr != None:
                curr = curr.findSuccessor()
                if curr != None:
                    print( curr.key )
        return

# define a function to reset thread     
    def setThread( self ):
        currNode = self.root
        if currNode == None:
            return
        else:
            currNode = currNode.findMin()
        while currNode != None:
            currNode.succ = currNode.findSuccessor()
            currNode = currNode.findSuccessor()
            





class TreeNode:
    def __init__(self,key,val,left=None,right=None,parent=None,succ=None):
        self.key = key
        self.payload = val
        self.leftChild = left
        self.rightChild = right
        self.parent = parent
        self.succ = succ #add reference to its successor
        
    def hasSuccessor(self):
        return self.findSuccessor()
    
    def hasLeftChild(self):
        return self.leftChild

    def hasRightChild(self):
        return self.rightChild

    def isLeftChild(self):
        return self.parent and self.parent.leftChild == self

    def isRightChild(self):
        return self.parent and self.parent.rightChild == self

    def isRoot(self):
        return not self.parent

    def isLeaf(self):
        return not (self.rightChild or self.leftChild)

    def hasAnyChildren(self):
        return self.rightChild or self.leftChild

    def hasBothChildren(self):
        return self.rightChild and self.leftChild

    def spliceOut(self):
        if self.isLeaf():
            if self.isLeftChild():
                self.parent.leftChild = None
            else:
                self.parent.rightChild = None
        elif self.hasAnyChildren():
            if self.hasLeftChild():
                if self.isLeftChild():
                    self.parent.leftChild = self.leftChild
                else:
                    self.parent.rightChild = self.leftChild
                self.leftChild.parent = self.parent
            else:
                if self.isLeftChild():
                    self.parent.leftChild = self.rightChild
                else:
                    self.parent.rightChild = self.rightChild
                self.rightChild.parent = self.parent

    def findMin(self):
        current = self
        while current.hasLeftChild():
            current = current.leftChild
        return current

    def replaceNodeData(self,key,value,lc,rc):
        self.key = key
        self.payload = value
        self.leftChild = lc
        self.rightChild = rc
        if self.hasLeftChild():
            self.leftChild.parent = self
        if self.hasRightChild():
            self.rightChild.parent = self
            
    def findSuccessor(self):
        succ = None
        if self.hasRightChild():
            succ = self.rightChild.findMin()
        else:
            if self.parent:
                if self.isLeftChild():
                    succ = self.parent
                else:
                    self.parent.rightChild = None
                    succ = self.parent.findSuccessor()
                    self.parent.rightChild = self
        return succ




if __name__ == "__main__":
    
    #test
    mytree = BinarySearchTree()
    mytree[3]="red"
    mytree[4]="blue"
    mytree[6]="yellow"
    mytree[2]="at"

    print( mytree[6] )
    print( mytree[2] )
    print( mytree.root.leftChild.key )
    print( mytree.root.leftChild.succ.key )
    print( mytree.root.rightChild.key )
    print( mytree.root.rightChild.succ.key )

    #test succ after adding and deleting a node
    mytree[5]="test1"
    print( mytree[5] )
    print( mytree.root.rightChild.key )
    print( mytree.root.rightChild.succ.key )

    del mytree[5]
    print( mytree.root.rightChild.key )
    print( mytree.root.rightChild.succ.key )

    mytree[1]="test2"
    print( mytree[1] )
    print( mytree.root.leftChild.leftChild.key )
    print( mytree.root.leftChild.leftChild.succ.key )
        
    #test the case where the key to be added is already in the BST
    mytree[2]="test3"
    print( mytree[2] )
    print( mytree.root.leftChild.key )
    print( mytree.root.leftChild.succ.key )
    
    #excercise3
    print("inorder traversal: ")
    mytree.inorder_nonrecur()

