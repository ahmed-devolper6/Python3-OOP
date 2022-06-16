#inherthias
class Cau:
    def sum(self,x,y):
        return x+y
    def mull (self,x,y):
        return x*y
    def __init__(slef, name):
        print(f"my name is {name}")
        print("Simple Calculator")
        print("_________________")
class SciCau(Cau):
    def power(self,x,y):
        return x**y
total = SciCau("ahmed")
print("\t SUM")
print("_________________")
xs =int(input("Enter i number: "))
ys = int(input("Enter anther number number: "))
print(f"the total is\n{xs} + {ys} = {total.sum(xs,ys)}")
print("\t MULL")
print("_________________")
xm =int(input("Enter i number: "))
ym = int(input("Enter anther number number: "))
print(f"the total is\n{xm} X {ym} = {total.mull(xm,ym)}")
print("\t POWER")
print("_________________")
xp =int(input("Enter i number: "))
yp = int(input("Enter anther number number: "))
print(f"the total is\n{xp} X {yp} = {total.mull(xp,yp)}")
