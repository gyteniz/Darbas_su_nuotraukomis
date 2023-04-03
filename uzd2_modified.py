"""
2

sukurkite funkciją, kuri priimtų :
paveikslėlį
kontrasto,
spalvingumo,
aštrumo ir
ryškumo reikšmes
išsaugoti ar ne reikšmę
ir atitinkamai pakoreguotų paveikslėlio nustatymus. Parodytų nuotrauką ekrane. Priklausomai nuo pasirinkimo, išsaugotų arba ne. Išsaugokite faile, prie originalaus pavadinimo pridėję pvz. '_modified', tarkime dog_modified.jpg.

"""
import os
from PIL import Image, ImageEnhance


# .Contrast kontrastas
# .Color reguliuoja spalvingumą
# .Sharpness - aštrumą
# .Brightness - ryškumą


def image_modified(pav, kontrastas=1.0, spalvingumas=1.0, astrumas=1.0, ryskumas=1.0, save=False):
    im = Image.open(pav)
    enh = ImageEnhance.Contrast(im)
    im=enh.enhance(kontrastas)
    enh =ImageEnhance.Color(im)
    im=enh.enhance(spalvingumas)
    enh =ImageEnhance.Sharpness(im)
    im=enh.enhance(astrumas)
    enh =ImageEnhance.Brightness(im)
    im=enh.enhance(ryskumas)
    if save:
        print(os.path.splitext(pav))
        te = os.path.splitext(pav)[0]
        print(te)
        xt = os.path.splitext(pav)[1]
        print(xt)
        im.save(f'{te}_modified{xt}')
    im.show()

image_modified("dogg.png", 2, 0, 5, 1, True)

