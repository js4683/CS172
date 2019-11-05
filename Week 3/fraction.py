class Fraction():
    #Constructor. Puts fraction in simplest form
    def __init__(self,a,b):
        self.num = a
        self.den = b
        self.simplify()
    #Print Fraction as a String
    def __str__(self):
        if self.den==1:
            return str(self.num)
        else:
            return str(self.num)+"/"+str(self.den)
    #Get the Numerator
    def getNum(self):
        return self.num
    #Get the Denominator
    def getDen(self):
        return self.den
    #Give Numerical Approximation of Fraction
    def approximate(self):
        return self.num/self.den
    #Simplify fraction
    def simplify(self):
        x = self.gcd(self.num,self.den)
        self.num = self.num // x
        self.den = self.den // x
    #Find the GCD of a and b
    def gcd(self,a,b):
        if b==0:
            return a
        else:
            return self.gcd(b,a % b)
    #Complete these methods in lab
    def __add__(self,other):
        num = (self.num*other.den + other.num*self.den)
        den = (self.den * other.den)
        return Fraction(num, den)
    
    def __sub__(self,other):
        num = (self.num*other.den - other.num*self.den)
        den = (self.den * other.den)
        return Fraction(num, den)
    
    def __mul__(self,other):
        num = (self.num*other.num)
        den = (self.den * other.den)
        return Fraction(num, den)
    
    def __truediv__(self,other):
        num = self.num*other.den
        den = self.den*other.num
        return Fraction(num, den)
    
    def __pow__(self,exp):
        if exp < 0:
            num = self.den
            den = self.num
            x = Fraction(num/den)
            return x**k
        elif exp == 0:
            return 1
        else:
            num = self.num**(exp-1)
            denom = self.den**(exp-1)
            num1 = self.num*num
            den1 = self.den*denom
            return Fraction(num1, den1)

