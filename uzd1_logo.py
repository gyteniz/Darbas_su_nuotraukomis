"""
1
Turime logo su peršviečiamu fonu, dydis 128*128. Atsisiųskite, ir perdarykite taip,
kad nuo viršaus ir apačios nusiimtų po 28 eilutes pikselių.
Išsisaugokite, nes naudosime sekančioms užduotims.
"""

from PIL import Image

im = Image.open("logo.png")
box = (0, 28, 128, 100)
logo_cropped = im.crop(box)
logo_cropped.show()
logo_cropped.save('logo_cropped.png')
print(logo_cropped.format, logo_cropped.size, logo_cropped.mode)
