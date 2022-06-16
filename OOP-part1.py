class Cau:
    def sum(self,x,y):
        return x+y
    def mull(slef,x,y):
        return x*y
    def power(self,x,y):
        return x**y
print("for sum:....")
xs = int(input("type i number: "))
ys = int(input("type aother number: "))
Sum = Cau()
print(f"{xs} + {ys} = {Sum.sum(xs,ys)}")
print("for mull:....")
xm = int(input("type i number: "))
ym = int(input("type aother number: "))
print(f"{xs} x {ys} = {Sum.mull(xm,ym)}")
print("for power:....")
xp = int(input("type i number: "))
yp = int(input("type i power of number: "))
print(f"{xp} xx {yp} = {Sum.power(xp,yp)}")
