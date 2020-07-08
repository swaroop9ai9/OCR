import PIL
from PIL import Image
import pytesseract
pytesseract.pytesseract.tesseract_cmd = '/usr/local/Cellar/tesseract/4.1.1/bin/tesseract'
text = pytesseract.image_to_string(Image.open(input('Enter Proccessed Image Name ')))
print(text)



file = open("/Users/batman/desktop/sandy.txt","w+")
file.write(text)
file.close()
