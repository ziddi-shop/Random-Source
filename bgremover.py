from rembg import remove
from PIL import Image

input_path = "in.png"
output_path = "out.png"

input = Image.open(input_path)
output = remove(input)
output.save(output_path)