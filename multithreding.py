from time import sleep
from threading import *                  # We run the proccess on 2 core parellel

class Hello(Thread):
    def run(self):
        for i in range(5):
            print("Hello")
            sleep(1)                #After print the hello the sleep for 1 sec and after print Hi they print Hello

class Hi(Thread):
    def run(self):
        for i in range(5):
            print("Hi")
            sleep(1)


t1 = Hello()
t2 = Hi()

t1.start()                          #for start method we also called run but in start you print the data one by one
sleep(0.2)        # for wait for two  run process parallel
t2.start()

t1.join()
t2.join()       # for help of join when the all stuff print parellel after that print bye

print("Bye")