class EL():
    def __init__(self, inc = 0, ft = 0, yrd = 0):
        self.__inches = inc
        self.__feet = ft
        self.__yards = yrd
    def cleanup(self):
        self.__feet += self.__inches // 2
        self.__inches = self.__inches % 12
        self.__yards += self.__feet //3
        self.__feet = self.__feet%3
    def __str__(self):
        ansStr = ''
        ansStr += str(self.__feet) + 'ft '
        ansStr += str(self.__yards) + 'yards '
        ansStr += str(self.__inches) + 'inches '
        return ansStr
    def __add__(self, other):
        newEL = EL(self.__inches + other.__inches, self.__feet + other.__feet, self.__yards + other.__yards)
        return newEL
    def totalInches(self):
        return self.__inches + self.__feet*12 + self.__yards*36
    def __gt__(self, other):
        return self.totalInches() > other.totalInches()
    def __eq__(self, other):
        return self.totalInches() == other.totalInches()
    def __getitem__(self, index):
        if index == 0:
            return self.__inches
        elif index == 1:
            return self.__feet
        elif index == 2:
            return self.__yards
        else:
            print('index out of range')
a = EL(30)
b = EL()
c= EL(1,2,3)
d = EL(30)
print(a==d)
print(a[2])


d = a + c         #d = a.add(c)
d += d
if a > b:
    print('larger')


print(a)
print(b)
print(c)
print(d) #print(d.__str__())