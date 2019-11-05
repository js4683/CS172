class Contact():
    def __init__(self, name, email):
        self.__name = name
        self.__email = email
    def getName(self):
        return self.__name
    def __str__(self):
        return 'name: ' + self.__name + '\nEmail:  ' + self.__email

class Friend(Contact):
    def __init__(self, name, email, phone):
        super().__init__(name, email)
        self.__phone = phone
    def __str__(self):
        return super().__str__() + '\nPhone: ' + self.__phone

a = Contact("matt", 'knsjf')
b = Friend('nsjfns', 'jsdbsnd', 'sjbdfjs')
lst = [a, b]
for i in range(len(lst)):
    return lst[i].__str__()
