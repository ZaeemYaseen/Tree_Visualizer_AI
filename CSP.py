from constraint import *
#Question number-01
print("\n===QUESTION NUMBER-01===")
obj = Problem()
obj.addVariable("a",[1,2,3])
obj.addVariable("b",[4,5,3])
print("POSSIBLE SOLUTIONS:  ")
print(obj.getSolutions())

obj.addConstraint(lambda a, b: a != b,("a", "b"))
print("DESIRED SOLUTIONS:  ")
print(obj.getSolutions())

#Question number-02
print("\n===QUESTION NUMBER-02===")
obj1 = Problem()
obj1.addVariable("a",[2,4,6,8,10,12])
obj1.addVariable("b",[3,6,12,15])
print("POSSIBLE SOLUTIONS:  ")
print(obj1.getSolutions())

obj1.addConstraint(lambda a, b: a == b and a==6,("a", "b"))
print("DESIRED SOLUTIONS:  ")
print(obj1.getSolutions())