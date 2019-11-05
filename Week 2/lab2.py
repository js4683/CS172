import datetime
t = str(datetime.datetime.now())
class Item():
    def __init__(self, tax, name='', price=0):
        self.name = name
        self.price = price
        self.taxable = tax
    def __str__(self):
        return self.name
    def getPrice(self):
        return self.price
    def getTax(self,tax):
        if tax == 'yes':
            ft = Reciept.tax_rate*self.price
            ft += ft
            return
        else:
            return 0
class Reciept():
    def __init__(self, ps=[]):
        self.tax_rate = .07
        self.purchases = ps
    def __str__(self):
        for thing in self.purchases:
            print ('%s________%s' % (Item.__str__(), Item.getPrice()))
    def addItem(self, np):
        self.purchases.append(np)
        print(Reciept.__str__)
        
print('Welcome to Receipt Creator')
r = Reciept()
while True:
    I = input('Enter Item Name:\n')
    P = float(input('Enter Item Price:\n'))
    T = input('Is the item taxable (yes/no):\n')
    Q = input('Add another item (yes/no):\n')
    if Q == 'no':
        ans = Item(I, P, T)
        aans = r.addItem(ans)
        print('---- Receipt', t, '----' )
        print(aans)
        break
    else:
        ans = Item(I, P, T)
        aans = r.addItem(ans)
        print('---- Receipt', t, '----' )
        print(aans)
