#########################################################
# Copying
with open('read_pic.jpg', 'rb') as rf:
    with open('copy_pic.jpg', 'wb') as wf:
        # for line in rf:
        #     wf.write(line)
        rf_chunk = rf.read(4096)
        while len(rf_chunk) > 0:
            wf.write(rf_chunk)
            rf_chunk = rf.read(4096)
#########################################################
# Writing
with open('test2.txt', 'w') as f:
    f.write('Test')
    f.write('Test')
    f.seek(0)
    f.write('Test')


#########################################################
# Reading
f = open('/home/jurgeon/fibonacci.py',  'r')
print(f.name)
print(f.mode)
f.close()
print(f.closed)  # >>> True
# print(f.read())  # >>> ValueError : I/O operations on closed file.

# При помощи контекстного менеджера with ... as ...:
with open('/home/jurgeon/fibonacci.py', 'r') as f:
    f_contents = f.read()  # >>> выводит весь файл
    # >>> каждый раз выводит указанное количество символов,начиная с предыдущего символа
    f_contents = f.read(100)
    f_contents = f.readline()  # >>> каждый раз выводит построчно по одной строке
    f_contents = f.readlines()  # >>> выводит построчно все строки
    for line in f:
        print(line)  # >>> выводит все строки
    while len(f_contents) > 0:
        print(f_contents)
        f_contents = f.read(100)  # >>> выводит все строки

    print(f.tell())  # >>> возвращает текущую позицию в файле
    f.seek(0)  # >>> переводит указатель на указаную позицию

print(f.closed)  # >>> True
# print(f.read())  # >>> ValueError : I/O operations on closed file.
