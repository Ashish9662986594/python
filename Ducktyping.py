class Vscode:                           # class 1

    def execute(self):                                  
        print("Compiling")
        print("Running")

class MyIde:                             #class 2
                                         #When your class like a 1 class and that all things are like 1 class then you also call it like a first class          
                                         #And that things you also called duck typing
    def execute(self):
        print("Check all things")
        print("Check sepll")
        print("COmpiling")
        print("running")


class Laptop:

    def code(self,cpu):
        cpu.execute()

cpu = MyIde()

lap1 = Laptop()

lap1.code(cpu)

