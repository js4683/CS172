class Node():
    def __init__(self, data, next = None):
        self.__data = data
        self.__next = next
        
    def getData(self):
        return self.__data
    def getNext(self):
        return self.__next
    def setData(self,d):
        self.__data = d
    def setNext(self,n):
        self.__next = n
    def __str__(self):
        return str(self.__data) + " whose next node is " + str(self.__next)

class linkedList():
    def __init__(self):
        self.__head = None
    def append(self, data):
        temp1 = Node(data)
        if self.__head == None:
            self.__head == temp1
        else:
            self.__head = temp1
            while temp1.getNext() != None:
                temp1 = temp1.getNext()
            temp1.setNext(temp1)
    def __str__(self):
        temp = self.__head
        mystr = ''
        while temp != None:
            mystr += str(temp) + '->'
        mystr += "None"
        return mystr
    def __len__(self):
        temp = self.__head
        count = 0
        if self.__head == None:
            return 0
        while temp.getNext() != None:
            temp = temp.getNext()
            count += 1
        return count
    def __getItem__(self, index):
        pass
if __name__ == "__main__": 
    myll = linkedList()
    myll.append('hello')
    myll.append('yolo')
    print(myll)