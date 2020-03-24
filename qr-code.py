import qrcode
qr=qrcode.QRCode(version=1,box_size=10,border=5)

data="Thanks for Scanning this QR Code. Hi! this is Akashddeep Gupta."
qr.add_data(data)
qr.make(fit=True)
img=qr.make_image(fill="Black",back_color="White")
img.save("qrcode.png")
