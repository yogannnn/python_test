import sys
import os

path = ""

while len(path) == 0:
    if len(sys.argv) > 1:
        path = (sys.argv[1]) # Если путь был указан, то ложим его в переменную иначе просим ввести
    else:
        try:
            path = input("Необходимо указать путь к папке: ") # Если просто ввести Enter, то скрипт падает, поэтому оберну в try
        except:
            path = ""

if not (path[-1] == "/"): # Ведь путь к каталогу должен оканчиваиться слешем
    path=path+"/"

if not (os.path.isdir(path)): # Существует ли каталог?
    print ("Указанный путь не найден")
    exit(0)

for files in sorted(os.listdir(path)):
    if os.path.islink(path+os.path.basename(files)):
        print(os.path.basename(files)+" | Ссылка")

    elif os.path.isdir(path+os.path.basename(files)):
        print(os.path.basename(files)+" | Каталог")

    elif os.path.isfile(path+os.path.basename(files)):
        print(os.path.basename(files)+" | Файл")
