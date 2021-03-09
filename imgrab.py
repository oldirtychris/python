import requests # Allows us to use requests library
from io import BytesIO # Used for binary data streams
from PIL import Image # Image processing

r = requests.get("<image URL here>") # URL of image to save

print("Status code:", r.status_code) # Status code - hopefully 200

image = Image.open(BytesIO(r.content)) # Grab content


print(image.size, image.format, image.mode)

path = "./image" + image.format # Path to save the file as and grab image type

try: # Save the image or print error
    image.save(path, image.format)
except IOError:
    print("Cannot save image.")
