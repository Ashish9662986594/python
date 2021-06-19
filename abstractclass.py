from abc import ABC, abstractmethod            # abstractclass module


class Computer(ABC):
    @abstractmethod                  # @ this is called decorater
    def process(self):
        pass                           # when you not define the method you only declaire the method that is called abstract method 
                                       # which class who has a absttract method thats also called abstract class
class Laptop(Computer):
    def process(self):
        print("Helo bro")


#com = Computer()
com1 = Laptop()
com1.process()
