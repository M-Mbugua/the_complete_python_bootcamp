from PIL import Image

computer = Image.open('example.jpg')

# computer.show()

print(computer.size)
print(computer.filename)
print(computer.format_description)

# CROPPING IMAGES

pencils = Image.open('pencils.jpg')
print(pencils.size)

# Top left pencils
x = 0
y = 0

w = 1950 / 3
h = 1300 / 10

# pencils.crop((x, y, w, h)).show()

# Bottom left pencils
x = 0
y = 1100

w = 1950 / 3
h = 1300

# pencils.crop((x, y, w, h)).show()


# Cropping out the computer and pasting the
# cropped out version onto the original.

halfway = 1993 / 2

x = halfway - 200
w = halfway + 200

y = 800
h = 1257

# computer.crop((x, y, w, h)).show()

comp = computer.crop((x, y, w, h))
computer.paste(comp, box=(0,0))

# computer.show()

# Resizing
# computer.resize((3000,500)).show()

# Rotating
# computer.rotate(90).show()

# Colour Transparency

red = Image.open('red_color.jpg')
blue = Image.open('blue_color.png')

# blue.putalpha(0) # No colour

# Combine red and blue to form purple

blue.putalpha(128)
red.putalpha(128)

blue.paste(im=red, box=(0,0), mask=red)
blue.show()

# blue.save("new_purple.png")













