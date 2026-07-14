#To make this work we need to download python libraries like "qrcode" and "pillow"

import qrcode as qr

img = qr.make("https://github.com/prakhar-bansal-itsme")
img.save("my_github.png")