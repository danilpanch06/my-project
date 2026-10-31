a = float(input("Введите число А (больше 1): "))
summ = 0
k = 0
while summ + (1 / (k + 1)) < a:
    k = k + 1
    summ = summ + (1 / k)
print (f"Наибольшее целое число k: {k}")
print (f"Сумма: {summ} ")