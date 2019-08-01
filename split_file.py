"""
Somtimes we are have the problem with copying file 
from computer on Mac to flash drive with size 4Gb and more. 
This script split file on some files with step 3 GB, with help zip commandline archivator. 
Run script, drag and drop folder with files to commandline and write "all" for all files. 
Or drag and drop one file to commandline for split one file. 

Autor: Andrew Lihasenko
"""


import subprocess
import os


path_from = input('Перетяниите папку в окно терминала или введите /путь/к/файлам вручную: \n')
if path_from.endswith(' '):
    path_from = path_from[:-1].replace('\\', '')
else:
    path_from = path_from.replace('\\', '')
file_name = input('Перетяниите файл в окно терминала или введите имя.файла вручную, или введите "all" для всех файлов: \n')
if '/' in file_name:
    if file_name.endswith(' '):
        file_name = file_name[:-1].replace('\\', '')
    else:
        file_name = file_name.replace('\\', '')
    file_name = os.path.split(file_name)
    file_name = file_name[1]


def split_file(path_from, file_name):
    name = os.path.splitext(file_name) # получаем имя файла и расширение
    size = os.path.getsize(os.path.join(path_from, file_name))
    if size >= 3900000000:  # 3,9 Gb
                os.chdir(path_from)  # изменить текущую папку 
                if not os.path.isfile(file_name + '.zip'):  # если файл '.zip' не существует
                    print('Выполняю разделение файла:', file_name)
                    subprocess.run(['zip', '-s', '3g', '%s.zip' %name[0], file_name, path_from])
    else:
        print('Файл:', file_name, 'меньше 4Gb - разделение не требуется')


def main(path_from, file_name):
    if file_name == 'all':
        for fl in os.listdir(path_from):
            if not fl.startswith('.'):  # если файл не скрытый
                split_file(path_from, fl)
    else:
        split_file(path_from, file_name)


if __name__ == '__main__':
    main(path_from, file_name)