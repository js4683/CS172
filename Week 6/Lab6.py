#Interface Class for a Stack
#Only allows access to the
#Stack commands of the built in list
class Stack:
	#Create a New Empty Stack
	def __init__(self):
		self.__S = []
	#Display the Stack
	def __str__(self):
		return str(self.__S)
	#Add a new element to top of stack
	def push(self,x):
		self.__S.append(x)
	#Remove the top element from stack
	def pop(self):
		return self.__S.pop()
	#See what element is on top of stack
	#Leaves stack unchanged
	def top(self):
		return self.__S[-1]

def postfix(exp):
    stack = Stack()
    parsed = exp.split()
    for item in parsed:
        if item == '+' or item == '-' or item == '*' or item == '/':
            operand1 = stack.top()
            stack.pop()
            operand2 = stack.top()
            stack.pop()
            if item == '+':
                result = int(operand1) + int(operand2)
                stack.push(float(result))
            elif item == '-':
                result = int(operand2) - int(operand1)
                stack.push(float(result))
            elif item == '*':
                result = int(operand1) * int(operand2)
                stack.push(float(result))
            elif item == '/':
                result = int(operand2) / int(operand1)
                stack.push(float(result))
        else:
            stack.push(item)
    print(stack.__str__())
print('Welcome to Postfix Calculator')
print('Enter exit to quit.')
userInp = input('Enter Expression\n')
while True:
    if userInp.lower() == 'exit':
        break
    else:
        postfix(userInp)
        userInp = input('Enter Expression\n')