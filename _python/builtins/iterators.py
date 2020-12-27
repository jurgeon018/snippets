# Итератор - интерфейс, предоставляющий доступ к элементам коллекции и навигацию по ним.
# iter() - создает итераторы
# Проктокол итераций - идея, которая подразумевает наличие в памяти последовательности или обьекта, который генерирует по одному элементу за раз в контексте выполнения итерации.  Объект попадает в категорию итерируемых, если в ответ на вызов встроенной функции iter (с этим объектом в качестве аргумента) возвращается объект, который позволяет перемещаться по его элементам с помощью функции next.
# любой инструмент языка Python, сканирующий объект слева направо, использует протокол итераций.
# Итетируемые обьекты: строка, список, словарь, множество, файл
# Итерируемые - обьекты которые поддерживают возможность итерации и релизуют метод iter()
# Итераторы - обьекты которые поддерживают функцию next() и возвращаются функцией iter()


L = [1, 2, 3]
I = iter(range(1, 4))


print(I)
print(L)
for x in range(1, 4):
    print(x*2)
# Реализация цикла for при помощи while
while True:
    try:
        x = next(I)
        print(x*2)
    except StopIteration:
        break


class MyRange:
    def __init__(self, start, end):
        self.value = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.value >= self.end:
            raise StopIteration
        current = self.value
        self.value += 1
        return current


def my_range(start, end, step=1):
    while start < end:
        yield start
        start += step


# nums = MyRange(1, 10)
nums = my_range(1, 10)
for num in nums:
    print(num, end=' ')


class Sentence:
    def __init__(self, sentence):
        self.sentence = sentence
        self.index = 0
        self.words = self.sentence.split()

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.words):
            raise StopIteration
        else:
            index = self.index
            self.index += 1
            return self.words[index]


def sentence(sentence):
    for word in sentence.split():
        yield word


# my_sentence = Sentence('This is a test')
my_sentence = sentence('This is a test')

for word in my_sentence:
    print(word)
