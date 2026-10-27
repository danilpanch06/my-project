import math
print ("1 -  древесина, 2 - керамика, 3 - зерно")
x = int(input("Введите номер материала (1-3): "))
if x == 1:
    k = 0.008
elif x == 2:
    k = 0.004
else:
    k = 0.012
m = float(input("Введите массу m: "))
w1 = float(input("Введите начальную влажность w1: "))
w2=w1
while w2>=w1:
    w2 = float(input("Введите конечную влажность w2 (меньше w1): "))
    if w2 >= w1:
        print ("Ошибка: w2 должна быть меньше w1")
t = float(input("Введите температуру t: "))
mw = m*(w1-w2) / (100-w2)
tau = (1 / k) * math.log(w1/w2)
if tau < 2:
    klass = "Быстрая сушка"
elif tau <= 12:
    klass = "Нормальная сушка"
else:
    klass = "Длительная сушка"
print ("Масса удаляемой воды", mw)
print ("Время сушки", tau)
print ("Класс сушки", klass)