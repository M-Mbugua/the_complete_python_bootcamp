# Your task is to use the mask.png image to reveal the
# hidden message inside the word_matrix.png.
from PIL import Image

word_matrix = Image.open('word_matrix.png')
print(word_matrix.size)

mask = Image.open('mask.png')
print(mask.size)

new_mask = mask.resize((1015, 559))
print(new_mask.size)

word_matrix.putalpha(180)
new_mask.putalpha(120)

word_matrix.paste(im=new_mask, box=(0,0), mask=new_mask)
word_matrix.show()

