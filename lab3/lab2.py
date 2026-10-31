import math

# 1. Меню и выбор материала через match-case
print("1 — Древесина")
print("2 — Керамика")
print("3 — Зерно")

k = 0
material = ""

while k == 0:
    try:
        choice = int(input("Выберите материал (1, 2 или 3): "))
        match choice:
            case 1:
                material = "Древесина"
                k = 0.008
            case 2:
                material = "Керамика"
                k = 0.004
            case 3:
                material = "Зерно"
                k = 0.012
            case _:
                print("Нет такого пункта! Введите 1, 2 или 3.")
    except ValueError:
        print("Нужно ввести цифру!")

# 2. Ввод массы m (от 1 до 5000)
m = 0.0
while m < 1 or m > 5000:
    try:
        m = float(input("Масса материала m (от 1 до 5000 кг): "))
        if m < 1 or m > 5000:
            print("Масса вне диапазона!")
    except ValueError:
        print("Введите число!")

# 3. Ввод начальной влажности w1 (от 5 до 60)
w1 = 0.0
while w1 < 5 or w1 > 60:
    try:
        w1 = float(input("Начальная влажность w1 (от 5 до 60 %): "))
        if w1 < 5 or w1 > 60:
            print("Влажность w1 вне диапазона!")
    except ValueError:
        print("Введите число!")

# 4. Ввод конечной влажности w2 (от 0.01 до 30 и строго меньше w1)
w2 = 999.0
while w2 <= 0 or w2 > 30 or w2 >= w1:
    try:
        w2 = float(input("Конечная влажность w2 (от 0 до 30 %, меньше w1): "))
        if w2 <= 0 or w2 > 30:
            print("Влажность w2 должна быть от 0 до 30 %!")
        elif w2 >= w1:
            print("Конечная влажность должна быть строго МЕНЬШЕ начальной!")
    except ValueError:
        print("Введите число!")

# 5. Ввод температуры t (от 40 до 250)
t = 0.0
while t < 40 or t > 250:
    try:
        t = float(input("Температура t (от 40 до 250 °C): "))
        if t < 40 or t > 250:
            print("Температура вне диапазона!")
    except ValueError:
        print("Введите число!")

# 6. Расчёты по формулам из задания
m_w = m * (w1 - w2) / (100 - w2)
tau = (1 / k) * math.log(w1 / w2)

# 7. Классификация времени
if tau < 2:
    group = "быстрая сушка"
elif tau <= 12:
    group = "нормальная"
else:
    group = "длительная"

# 8. Вывод
print("\n--- Результат ---")
print("Материал:", material)
print("Удалённая вода:", round(m_w, 2), "кг")
print("Время сушки:", round(tau, 2), "ч")
print("Класс сушки:", group)