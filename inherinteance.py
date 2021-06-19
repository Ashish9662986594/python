class A:                                             # Parent class
    def feature1(self):
        print("The feature1 is working")

    def feature2(self):
        print("The feature2 is working")

class B():                                    #B is a child class                                # That is called inheritance

    def feature3(self):
        print("The feature3 is working")

    def feature4(self):
        print("The feature4 is working")

class C(A,B):                           #This also called a multi inheritance
    
    def feature5(self):
        print("The feature5 is working")






a1 = C()

a1.feature3()