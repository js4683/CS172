import random
from BST import *
import matplotlib.pyplot as plt
import time
def populate(n):
    randlist = []
    tree = BST()
    for i in range(0,n):
        num = random.randint(0,n)
        randlist.append(num)
        tree.append(num)
    return randlist, tree

def check(randlist, n):
    for item in randlist:
        if item == n:
            return True
    return False
lisofruns = []
for i in range(0, 10000, 1000):
        temp = populate(i)
        lisofruns.append(temp)
timeforlis = []
timeforBST = []
n = []
for item in lisofruns:
        count1 = 0
        count2 = 0
        time1 = time.time()
        for thing in item[0]:
                if check(item[0], thing) == True:
                        count1 += 1
        time2 = time.time()
        for thing in item[0]:
                if item[1].isin(thing) == True:
                        count2 += 1
        time3 = time.time()
        timeforlis.append(time2 - time1)
        timeforBST.append(time3 - time2)
        n.append(count1)

plt.plot(n, timeforlis, label = 'list')
plt.plot(n, timeforBST, label = 'BST')
plt.legend()
plt.show()

