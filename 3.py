H =float(input("введите высоту конуса в см"))
R =float(input("введите радиус конуса в см"))
print("Формула площади боковой поверхности конуса S=πR*√(R²+H²)")
J=(R**2+H**2)
import math
num = J
sqrt = math.sqrt(num)
print("Квадратный корень из (R²+H²)" + str(num) + " это " + str(sqrt))
import math
num = R
pi = math.pi*(num)
print("произведение πR=" + str(pi))
S=pi*sqrt
print("площади боковой поверхности конуса " +str(S) + " см²")


print("Формула объема конуса : V=H/3*π*R)")
V=H/3*3.14*R
print("объема конуса " +str(V) + " см³")



