import pytesseract
from PIL import Image

image = Image.open("data/train/bl_01")

text = pytesseract.image_to_string(image)
print(text)