import os
import shutil
import time

dirname=input("Введите название папки. В нее положим вновь созданный файл: ")
filename = input("Введите имя нового файла: ")

try:
    os.mkdir(dirname)
except OSError:
    print ("Создать директорию "+dirname+" не удалось")
else:
    print ("Директория "+dirname+" успешно создана")

try:
    f = open(dirname+'/'+filename, 'w')
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
f = open(dirname+'/'+filename)
for line in f:
    print(line)
f.close()

print("1 минута для проверки того, что в файл всё записано. После, файл и папка будут удалены")
time.sleep(60)

fi = os.path.join(os.path.abspath(os.path.dirname(__file__)), dirname)
try:
    shutil.rmtree(fi)
except:
    print("Удалить директорию " + dirname + " не удалось")
else:
    print("Директория " + dirname + " удалена")