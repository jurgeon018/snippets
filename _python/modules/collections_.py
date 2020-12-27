from collections import namedtuple

Color = namedtuple('Color', ['red', 'green', 'blue'])

dict_color = {'red': 255, 'green': 255, 'blue': 250}

some_color = Color(55, 155, 255)

print(dict_color['blue'])
print(some_color.blue)
