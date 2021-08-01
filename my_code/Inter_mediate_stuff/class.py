''' class '''

#not a private member class 1
class not_private_class_1():
    def __init__(self,name):
        self.name = name

    def makeclass(self):
        print("hai hello not_private_class_1")
        print(self.name)

obj1 = not_private_class_1("ibrahim")

obj1.makeclass()
print(not_private_class_1)

print(obj1.name)
print("======================================================")

#=========================================================================
#not a private member class 2
class not_private_class_2():
    def __init__(self,name):
        self._name = name

    def makeclass(self):
        print("hai hello not_private_class_2")
        print(self._name)

obj2 = not_private_class_2("ibrahim")

obj2.makeclass()
print(not_private_class_2)

print(obj2._name)
print("======================================================")

#==========================================================================
#private member class 
class private_class():
    def __init__(self,name):
        self.__name = name

    def makeclass(self):
        print("hai hello private_class")
        print(self.__name)
    def get_name(self):
        return self.__name

obj3 = private_class("ibrahim")

obj3.makeclass()
print(private_class)

#  error due to __var is private
#print(obj2.__name)

print(obj3.get_name())
print("======================================================")




    
