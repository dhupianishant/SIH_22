import pyqrcode
import png
from pyqrcode import QRCode
a=input("Enter Name: ")
url=pyqrcode.create(s)
url.png('myqr.png', scale=6)
