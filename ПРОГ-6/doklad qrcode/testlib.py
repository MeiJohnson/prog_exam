import qrcode

img0 = qrcode.make('Кто прочитал - тот отчислен.')
img0.save('test.png')
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data('https://sun9-22.userapi.com/impg/dMaBR2IML7sdjG3vz8i25ZpKx-GpzWvcNg3Vwg/6ApK69J4t2A.jpg?size=1366x728&quality=96&sign=4058f3b8926343df80b280ca3f455503&type=album')
qr.make(fit=True)

img = qr.make_image(fill_color="pink", back_color="white")
img2 = qr.make_image(fill_color="black", back_color="white")
img.save('testCode.png')
img2.save('testCode2.png')