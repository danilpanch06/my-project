s = input("Введите предложение на английском: ")
string = ""
for i in range(len(s)):
    if i == 0:
        string = string + s[0].upper()
    elif s[i-1]== "":
        string = string + s[i].upper()
    else:
        string = string + s[i]
print("Результат")
print(string)