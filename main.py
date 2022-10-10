print("Введите коэффициенты уравнения")
print("ax^2 + bx + c = 0:")
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

dis = b ** 2 - 4 * a * c
print("Дискриминант D =", dis)

if dis > 0:
    x1 = (-b + dis ** 0.5) / (2 * a)
    x2 = (-b - dis ** 0.5) / (2 * a)
    print("x1 = ", x1 )
    print("x2 = ", x2 )
elif dis == 0:
    x = -b / (2 * a)
    print("x = ",x)
else:
    print("Корней нет")