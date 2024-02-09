# Program to convert an image to a colored ASCII representation.
# © 2024, Hayden Feeney
# Photo credit: Grit City Magazine

# Potential improvements to be made: find brightest, darkest pixels
# in the image, then use those as interpolation bounds

from PIL import Image
from colortrans import rgb2short

chars = 'Ñ@#W$9876543210?!abc;:+=-,._ '

def px_to_char(px):
  r, g, b = px
  avg = (r + g + b) / 3.0
  scale = len(chars) / 255
  res = len(chars) - round(scale * avg)
  if (res == len(chars)):
    res = res - 1
  return chars[res]

def px_to_ansi_col(px):
  res, _ = rgb2short('#%02x%02x%02x' % px)
  return '\u001b[38;5;' + res + 'm'

def px_to_ascii(px):
  return px_to_ansi_col(px) + px_to_char(px)

def img_to_ascii(img):
  res = ''
  pixels = img.load()

  for i in range(img.size[1]):
    for j in range(img.size[0]):
      px = pixels[j,i]
      res += px_to_ascii(px)
    res += '\n'

  return res


img = Image.open('Tacoma.jpeg')

w = img.size[0]
h = img.size[1]

scale = 0.2

# supposedly, the ratio of width to height in fonts is 0.5
img = img.resize((int(w * scale), int(h * scale * 0.5)))

print(img_to_ascii(img))