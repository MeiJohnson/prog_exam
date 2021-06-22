import pyqrcode

img = pyqrcode.create(input('Введите текст:\n'))
img.svg('test.svg')
