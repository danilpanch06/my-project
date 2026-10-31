print ("Введите оценки по очереди :")
sum = 0
for a in range(20):
    ocenka = int(input(f"Ученик  {a + 1}: "))
    sum = sum + ocenka
sred = sum/20 
print (sred)
