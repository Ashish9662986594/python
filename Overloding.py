class Student:
    
    def __init__(self,m1,m2):
        self.m1 = m1
        self.m2 = m2

    def __add__(self, other):
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2
        s3 = Student(m1,m2)

        return s3

    def __gt__(self, other):                      # gt is greter than method 
        r1 = self.m1 + self.m1
        r2 = other.m2 + other.m2

        if r1 > r2:
            return True
        else:
            return False


        

s1 = Student(23,3345)
s2 = Student(24,45)

s3 = s1 + s2

if s1 > s2:
    print("s1 wins")

else: 
    print("s2 losee")