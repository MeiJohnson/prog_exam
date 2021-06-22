import pyqrcode
import png
import random

r = random.randrange(256)
g = random.randrange(256)
b = random.randrange(256)

data = pyqrcode.create(input('Введите текст:\n'))
data.png('code.png', scale=6, module_color=[r, g, b, 128], background=[r, g, b])
