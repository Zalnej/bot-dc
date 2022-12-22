# Importing the PIL library
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

# Open an Image
img = Image.open('cytat.jpg')

# Call draw Method to add 2D graphics in an image
I1 = ImageDraw.Draw(img)

# Custom font style and font size
#myFont = ImageFont.truetype('FreeMono.ttf', 65)
#myFont = ImageFont.load_default()
myFont = ImageFont.truetype(r'C:\Users\System-Pc\Desktop\arial.ttf', 65)
# Add Text to an image
x="- Dobrze że się skończyło, \nbo to by się dobrze nie skończyło"
I1.text((200, 300), x, font=myFont, fill=(255, 0, 0))

# Display edited image
img.show()

# Save the edited image
img.save("car2.png")