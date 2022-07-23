from PIL import Image
img = Image.open(r"C:\Users\nisha\Documents\SIH' 22\bgimage.png")
img2= Image.open(r"C:\Users\nisha\Documents\SIH' 22\myqr.png")
img.paste(img2, (1500, 445))
img.save("pastedimage.png")
img.show()