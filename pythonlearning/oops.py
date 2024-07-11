class MyClass:
    def myMethod1(self):
        pass
    @staticmethod
    def myMethod2(name):
        print(name)

mc1 = MyClass()
mc1.myMethod1()
#mc1.myMethod2('123','John')
MyClass().myMethod1()
#MyClass().myMethod2('123','John')
MyClass.myMethod2('John')

class MyClass2:
    a,b =10,20
    def add(self):
        print(self.a+self.b)
    def mul(self):
        print(self.a*self.b)

mc=MyClass2()
mc.add()
mc.mul()

i,j=1,2 #Global var
class MyClass3:
    a,b=10,20 # class Variables
    def add(self,x,y):
        print(x+y)
        print(self.a+self.b)
        print(i+j)

mc = MyClass3()
mc.add(25,35)
mc.add(i,j)


a,b=1,2 #Global var
class MyClass3:
    a,b=10,20 # class Variables
    def add(self,a,b):
        print(a+b)
        print(self.a+self.b)
        print(globals()['a']+globals()['b']) #Global Variables

mc = MyClass3()
mc.add(25,35)

class MyClass:
    def __init__(self):
        print('constructor')
    def m1(self):
        print('m1')
    def m2(self,x,y):
        return x+y

mc=MyClass()
mc.m1()
print(mc.m2(1,2))

class Emp:
    eid=""
    name=""
    age=""
    def __init__(self,eid,name,age):
        self.eid=eid
        self.name=name
        self.age=age
    def display(self):
        print(self.eid,self.name,self.age)

e1=Emp("001","Kumar",38)
e1.display()
e2=Emp("002","Kumar",38)
e2.display()

print("Constructor to display")
class Emp:
    eid=""
    name=""
    age=""
    def __init__(self,eid,name,age):
        self.eid=eid
        self.name=name
        self.age=age
    def __str__(self):
        return self.eid

e1=Emp("001","Kumar",38)
print(e1)




