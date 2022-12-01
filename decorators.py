# wrapping output using decorators

def dec(func):
    def owrapper():
        print('_'*20)
        func()
        print('_'*20)
    return owrapper
    

# @dec
def myprint(str="default"):
    """Just prints Hi"""
    print("Hi")
    
# myprint()

# normal version on another branch

wrapp = dec(myprint)
wrapp()

print("\n","\n") # empty lines

# runtime of func normal version

# importing time module
import time
def timer(func):
    def wraaper():
        s_time = time.time()
        val=func()
        e_time = time.time()
        t_time = e_time - s_time
        print(t_time)
        return val
    return wraaper

def wastetime():
    a =[]
    for i in range(40000000):
        a.append(i)
        
totaltime =timer(wastetime)
totaltime()