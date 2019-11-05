class BSTNode():
    def __init__(self, data, left=None,right=None):
        self.__data = data
        self.__left = left
        self.__right = right
    
    def __str__(self):
        pass
    
    def getData(self):
        return self.__data
    
    def getLeft(self):
        return self.__left
    
    def getRight(self):
        return self.__right
    
    def setRight(self, data):
        self.__right = data
    
    def setLeft(self, data):
        self.__left = data

class BST():
    def __init__(self):
        self.__root = None

    def isEmpty(self):
        if self.__root == None:
    
    def insert(self,data):
        if self.__root == None:
            newNode = BSTNode(data)
        else:
            prev = None
            current = self.__root
            while current != None:
                prev = current
                if data < current.getData():
                    current = current.getLeft()
                else:
                    current = current.getRight()
        newNode = BSTNode(data):
        if data < prev.getData():
            prev.setLeft(newNode)
        else:
            prev.setRight(newNode)
        
        def search(self, data):
            if self.__root == None:
            print('Not Found')
            return None
        else:
            prev = None
            current = self.__root
            while current != None:
                prev = current
                if data == current.getData():
                    print('found it')
                    return current.getData()
                elif data < current.getData:
                    current = current.getLeft()
                else:
                    current = current.getRight()
            print('Not Found')
            return None