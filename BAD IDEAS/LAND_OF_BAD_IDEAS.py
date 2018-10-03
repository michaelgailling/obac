import pickle

# Use a string as a way of creating global variable names
# Worst of the bad ideas so far
globals()["herp"] = 0
print(herp)

# The more forgiving abuse of the above is demonstrated below encapsulated in a class where it belongs
class BadIdeaClass1():
    def __init__(self):
        setattr(self, 'herp', 'derp')
        print(self.herp)
    def derp(self):
        print("derp")

BIC1 = BadIdeaClass1()
print(BIC1.herp)

# More uses of strings as a form of aliasing functions with dictionaries
# Probably the best of the worst ideas so far
def Derp():#derp
    print("adur?")#adur


def Herp():#derp
    print("adur?")#adur

# dictionary -> function
hurdur = {"derp": Derp(),
          "herp": Herp()}

hurdur["herp"]
hurdur["derp"]


class BadIdeaClass2():
    def __init__(self):
        setattr(self, "BIC", BadIdeaClass1)

BIC2 = BadIdeaClass2

picklestring = pickle.dumps(BIC1)
print(picklestring)
BIC1 = None
print(pickle.loads(picklestring).herp)


def Handle_File_Type(fname):
    ext = ""
    for i in fname:
        if i == "." or ext:
            ext += i
    print(ext)

Handle_File_Type("derp.txt")

try:
    print("BUGGY CODE GOES HERE")
except Exception as err:
    print(err)


import timeit

#A testing function that takes a while

def costly_func():
   return map(lambda x: x^2, range(10))

#If you want to test a function with parameters you need to wrap it first... for some reason

def WrapperFUN(func, *args, **kwargs):
        return func(*args, **kwargs)

#Pass the function as a parameter -> Receive average time of function based on the number of runs. Defaults to a single run.

def TimeProfileFUN(func, runs=1, type="average"):
    dts = 0.0
    for i in range(0, runs):
        dts += timeit.timeit(func)
    return dts/runs

#Wrap it
#wrapped = WrapperFUN(costly_func())

#Profile it
print(TimeProfileFUN(costly_func, 10))