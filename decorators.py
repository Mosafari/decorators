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