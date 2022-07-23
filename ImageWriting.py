from PIL import Image, ImageDraw, ImageFont
img = Image.open(r"C:\Users\nisha\Documents\SIH' 22\pastedimage.png")
d1= ImageDraw.Draw(img)
d1.text((200,445), "Nishant Dhupia", fill=(0, 0, 0))
img.save("FinalTicket.png")
img.show()