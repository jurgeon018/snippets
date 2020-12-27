import re


list_of_re_methods = '''

r = re.finditer(pattern, string) - возвращает итератор из всех найденных совпадений

r = re.findall(pattern, string) - возвращает список всех найденных совпадений

r = re.match(patters, string) - ищет совпадения по заданному шаблону в начале строки
r.group() -  возвращает найденную строку
r.start() - возвращает начальную позицию найденной строки
r.end() - возвращает конечную позицию найденной строки

r = re.search(pattern, string): - ищет по заданному шаблону по всей строке, возвращает первое найденное совпадение
r.group() - возвращает найденную строку
r.start() - возвращает начальную позицию найденной строки
r.end() - возвращает конечную позицию найденной строки

re.split(pattern, string[, maxsplit=0]) - разделяет строку по заданому шаблону, возвращает разделенные участки

re.sub(pattern, repl, string) - ищет шаблон в строке(string) и заменяет его на указанную подстроку(repl)

re.compile(pattern, repl, string, re.IGNORECASE) - собирает регулярное выражение в отдельный обьект,который может быть использован для поиска, что избавляет от переписывания одного и того же выражения
'''


list_of_regular_expressions = '''
    .   - Any character except new line
    \   - Экранирование специальных символов
    \d  - Digit (0-9)
    \D  - Not a Digit(0-9)
    \w  - Word Character(a-z, A-Z, 0-9, _)
    \W  - Not a Word Character
    \s  - Whitespace (space, tab, newline)
    \S  - Not Whitespace(space, tag, newline)

    \b  - Word Boundary
    \B  - Not a Word Boundary
    ^   - Beginning of a String
    $   - End of a String

    []  - Matches characters in brackets
    [^ ]- Matching characters not in brackets
    a|b - а или b
    ()  - группирует выражение и возвращает найденный текст

    \t  - символ табуляции
    \n  - символ новой строки
    \r  - символ возврата каретки
    # Квантификаторы
    ?   - 0 или 1 вхождение шаблона слева
    *   - 0 и более вхождений шаблона слева
    +   - 1 и более вхождений шаблона слева
    +   - неограниченное количество вхождений
    {x} - Количество вхождений
    {n,m} От n до m вхождений
    {,m}- От 0 до m вхождений
'''


text_to_search = '''
Start a sentence and then bring it to an end
abcdefghijkmnopqurtuvwxyz
ABCDEFGHIJKMNOPQURTUBVWXY
1234567890

Ha HaHa

MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )

coreyms.com

322-555-4321
151.555.1234
222*238*2356

Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T

cat
mat
pat
bat

CoreyMSchafer@gmail.com
corey.schafer@university.edu
corey-321-schafer@my-work.net

https://www.google.com
http://coreyms.com
https://youtube.com
https://www.nasa.gov
'''
sentence = 'Start a sentence and then bring it to an end'


re.compile(r'.')
# >>> все символы
re.compile(r'\.')
# >>> все точки
re.compile(r'\d')
# >>> все цифры 0-9
re.compile(r'\D')
# >>> все кроме цифр
re.compile(r'\w')
# >>> все a-z, A-Z, 0-0, _
re.compile(r'\W')
# >>> все . ^ $ * + ? { } [ ] \ | ( ) \n
re.compile(r'\s')
# >>> все \n \t
re.compile(r'\S')
# >>> все кроме \n \t
re.compile(r'\bHa')
# >>> <_sre.SRE_Match object; span=(65, 67), match='Ha'>
# >>> <_sre.SRE_Match object; span=(68, 70), match='Ha'>
re.compile(r'\BHa')
# >>> <_sre.SRE_Match object; span=(70, 72), match='Ha'>
re.compile(r'^Start')
# >>> <_sre.SRE_Match object; span=(0, 4), match='Star'>
re.compile(r'end$')
# >>> <_sre.SRE_Match object; span=(0, 4), match='Star'>
re.compile(r'\d\d\d.\d\d\d.\d\d\d\d')
re.compile(r'\d\{3}.\d\{3}.\d\{4}')
# >>> <_sre.SRE_Match object; span=(198, 210), match='321-555-4321'>
# >>> <_sre.SRE_Match object; span=(211, 223), match='123.555.1234'>
# >>> <_sre.SRE_Match object; span=(224, 236), match='234*238*2356'>
re.compile(r'\d\d\d[-.]\d\d\d[-.]\d\d\d\d')
# >>> <_sre.SRE_Match object; span=(198, 210), match='321-555-4321'>
# >>> <_sre.SRE_Match object; span=(211, 223), match='123.555.1234'>
re.compile(r'[a-zA-z]')
# список всех символов от a до z и от А до Z
re.compile(r'[^a-zA-z]')
# список всех символов кроме a-z, A-Z
re.compile(r'[^b]at')
# mat, cat, pat
re.compile(r'Mr\.')
# >>> <_sre.SRE_Match object; span=(238, 241), match='Mr.'>
# >>> <_sre.SRE_Match object; span=(282, 285), match='Mr.'>
re.compile(r'Mr\.?')
# >>> <_sre.SRE_Match object; span=(238, 241), match='Mr.'>
# >>> <_sre.SRE_Match object; span=(250, 252), match='Mr'>
# >>> <_sre.SRE_Match object; span=(268, 270), match='Mr'>
# >>> <_sre.SRE_Match object; span=(282, 285), match='Mr.'>
re.compile(r'Mr\.?\s[A-Z]')
# >>> <_sre.SRE_Match object; span=(238, 243), match='Mr. S'>
# >>> <_sre.SRE_Match object; span=(250, 254), match='Mr S'>
# >>> <_sre.SRE_Match object; span=(282, 287), match='Mr. T'>
re.compile(r'Mr\.?\s[A-Z]\w+')
# >>> <_sre.SRE_Match object; span=(238, 249), match='Mr. Schafer'>
# >>> <_sre.SRE_Match object; span=(250, 258), match='Mr Smith'>
re.compile(r'Mr\.?\s[A-Z]\w*')
# >>> <_sre.SRE_Match object; span=(238, 249), match='Mr. Schafer'>
# >>> <_sre.SRE_Match object; span=(250, 258), match='Mr Smith'>
# >>> <_sre.SRE_Match object; span=(282, 287), match='Mr. T'>
re.compile(r'M(r|s|rs)\.?\s[A-Z]\w*')
re.compile(r'(Mr|Ms|Mrs)\.?\s[A-Z]\w*')
# >>> <_sre.SRE_Match object; span=(238, 249), match='Mr. Schafer'>
# >>> <_sre.SRE_Match object; span=(250, 258), match='Mr Smith'>
# >>> <_sre.SRE_Match object; span=(259, 267), match='Ms Davis'>
# >>> <_sre.SRE_Match object; span=(268, 281), match='Mrs. Robinson'>
# >>> <_sre.SRE_Match object; span=(282, 287), match='Mr. T'>
re.compile(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+')
# >>> <_sre.SRE_Match object; span=(306, 329), match='CoreyMSchafer@gmail.com'>
# >>> <_sre.SRE_Match object; span=(330, 358), match='corey.schafer@university.edu'>
# >>> <_sre.SRE_Match object; span=(359, 388), match='corey-321-schafer@my-work.net'>
pattern = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')
# match.group(0) - целый урл
# match.group(1) - www., None, None, www.
# match.group(2) - google, coreyms, youtube, nasa
# match.group(3) - .com или .gov

subbed_urls = pattern.sub(r'\2\3', text_to_search)
# print(subbed_urls) >>> google.com, coreyms.com, youtube.com, nasa.gov

pattern.findall(text_to_search)
for match in pattern.finditer(text_to_search):
    print(match.group(1))

# with open('data.txt', 'r') as f:
#     content = f.read()
#     matches = pattern.finditer(content)
#     for match in matches:
#         print(match)
