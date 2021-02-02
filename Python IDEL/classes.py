#classes

class Number:#creating class
    x=10
num=Number()#creating object
print(num)#calling the object

#classes with  main function

class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
p1=person('ram',24)
print(p1.name)
print(p1.age)
class person1:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def myfunc(self):
        print('hello my name is '+self.name)
p2=person1('Raj',27)
p2.myfunc()

#using different to determine self 
class Person2:
    def __init__(mysillyobject, name, age):
        mysillyobject.name = name
        mysillyobject.age = age

    def myfunc(abc):
        print("Hello my name is " + abc.name)

p3= Person2("John", 36)

p3.myfunc()

