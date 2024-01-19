from rembg import remove
from PIL import Image
input_path = ".jpg"
ouput_path = " .png"
inp = Image.open(input_path)
output = remove(inp)
output.save(ouput_path) 