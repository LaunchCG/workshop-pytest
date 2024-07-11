class A:
    def m1(self):
        print('A.m1')

class B(A):
    def m2(self):
        print('B.m2')

b=B()
b.m1()
b.m2()