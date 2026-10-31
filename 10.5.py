x = []
for i in range(15):
    print('Введите', i, 'элемент')
    x.append(int(input()))
y = x.copy()
for i in range(15):
    if y[i] < 10:
        y[i] = 0
    elif y[i] > 20:
        y[i] = 1
print('Первоначальный массив x:', x)
print('Преобразованный массив y:', y)
