"""
4
Parašykite programą, kuriai padavus nuotrauką ir R G B reikšmes, ji pakoreguotų kiekvieną
pikselį atitinkamai. T.y. jeigu reikšmė teigiama - pridėtų, jeigu neigiama - atimtų.
Neleiskite galutinėms reikšmėms būti mažesnėmis už nulį ir didesnėmis už 255!
"""
from PIL import Image

def ribos(sk):
    if sk < 0:
        return 0
    elif sk > 255:
        return 255
    return sk


def adjust_colors(img, r, g, b):
    img = Image.open(img)
    data = img.getdata()
    new_data = []
    for pixel in data:
        red = ribos(pixel[0] + r)
        green = ribos(pixel[1] + g)
        blue = ribos(pixel[2] + b)
        new_pixel = (red, green, blue)
        new_data.append(new_pixel)

    img.putdata(new_data)
    return img


new_img = adjust_colors('dogg.png', -50, +20, +80)
new_img.show()