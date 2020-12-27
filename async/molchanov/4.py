
from time import time 



def gen(s):
    for i in s:
        yield i


g = gen('oleg')

def gen_filename():
    while True:
        t = str(int(time() * 1000))
        yield f'file-{t}.jpeg'

