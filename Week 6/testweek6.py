class MyQueue():
    def __init__(self):
        self.__data = []
    
    def put(self, data):
        self.__data.append(data)
    
    def get(self):
        if not self.empty():
            self.__data.pop(0)   
        else:
            print('Empty Queue') 
    
    def empty(self):
        if len(self.__data) == 0:
            return True
        else:
            return False

