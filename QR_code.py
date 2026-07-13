import qrcode as qr

img = qr.make("https://github.com/prakhar-bansal-itsme")
img.save("my_github.png")