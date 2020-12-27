import os
from datetime import datetime

print(os.getcwd())
# выводит текущую директорию
os.chdir('/home/jurgeon/testdir')
# меняет директорию
print(os.getcwd())
# выводит список папок в директории
print(os.listdir())
# выводит текущую директорию
os.mkdir('OS_Demo')
# может создать одну папку
os.makedirs('OS_dir/sub_dir')
# может создавать папки и подпапки
os.rmdir('OS_Demo')
# может удалить одну папку
os.removedirs('OS_dir/sub_dir')
# может удалить папку и подпапки рекурсивно
os.rename('folder1', 'folder1')
# меняет название файла или папки
print(os.stat('file.txt'))
# показывает свойства файла
print(datetime.fromtimestamp(os.stat('file.txt').st_mtime))
# st_mtime показывает время редактирвоания
for dirpath, dirnames, filenames in os.walk('/home/jurgeon/testdir'):
    print('Current Path:', dirpath)
    print('Directories:', dirnames)
    print('Files:', filenames)
# выводит дерево всех директорий и файлов
HOME = os.environ.get('HOME')
# переменная окружения, которая содержит пусть к домашней папке
os.path.join(HOME, 'test.txt')
# соединяет пути
os.path.basename('/tmp/test.txt')
# >>> test.txt
os.path.dirname('/tmp/test.txt')
# >>> /tmp
os.path.split('/tmp/test.txt')
# >>> ('/tmp', 'test.txt')
os.path.exists('/tmp/test.txt')
# >>> False
os.path.isdir('/tmp/test.txt')
# >>> False
os.path.isfile('/tmp/test.txt')
# >>> True
os.path.splitext('/tmp/test.txt')
# >>> ('/tmp/test', '.txt')

###################################################
# renaming multiple files
os.chdir('.')
for f in os.listdir():
    file_name, file_ext = os.path.splitext(f)
    f_title, f_course, f_num = file_name.split('-')
    f_title = f_title.strip()
    f_course = f_course.strip()
    f_num = f_num.strip().zfill(2)
    new_name = f'{f_num}-{f_course}-{f_title}{file_ext}'
    os.rename(f, new_name)
