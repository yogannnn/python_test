import sys
import os

def get_size(start_path):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(start_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            # skip if it is symbolic link
            if not os.path.islink(fp):
                total_size += os.path.getsize(fp)
    return total_size

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
        size = get_size(path + os.path.basename(files))
        print(os.path.basename(files)+" | Каталог | Размер: "+str(size)+" Байт")

    elif os.path.isfile(path+os.path.basename(files)):
        print(os.path.basename(files)+" | Файл | Размер: "+str(os.path.getsize(path+os.path.basename(files)))+" Байт")

