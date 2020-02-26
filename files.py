
filename = input("Введите имя нового файла: ")
try:
    f = open(filename, 'w')
    print("Файл "+filename+" успешно создан")
except:
    print("При создании файла произошла ошибка")
    exit(0)

text = input("А теперь что-нибудь запишем в файл: ")
try:
    f.write(text + '\n')
    print('Текст \n'+text+'\nуспешно записан в файл')
except:
    print("При записи в файл произошла ошибка")
    exit(0)
f.close()

print("Читаем из файла...")
f = open(filename)
for line in f:
    print(line)
f.close()