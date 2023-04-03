"""
3
Sukurkite programą, kuri, gavusi nuorodą į katalogą,
praiteruos visus jame esančius failus,
išrinks nuotraukas,
pakeis dydį pagal jūsų nurodytą aukštį išlaikant proporcijas,
ir kiekvienos nuotraukos apatiniame dešiniajame kampe įdės logotipą,
tą kurį išsisaugojote pirmoje užduotyje.
 Naudokite .resize, kadangi nuotrauką galbūt reikės padidinti, nebūtinai tik sumažinti.
 Programa pakeistas nuotraukas turi išsaugoti į tame pačiame kataloge sukurtą 'optimized' katalogą."""
import os
from PIL import Image


def katalogo_paveiksliukai(directory='C:\\Users\\Gytis V\\OneDrive\\Desktop\\PYTHON\\Darbas_su_nuotraukomis'):
    paveiksliukai = []
    for images in os.listdir(directory):
        # check if the image ends with png, jpg
        if (images.endswith(".png") or images.endswith(".jpg")):
            paveiksliukai.append(images)
    return paveiksliukai


# print(katalogo_paveiksliukai())


def pav_resize(im, aukstis):
    plotis = round(im.size[1] / im.size[0] * aukstis)
    pakeistas = im.resize((aukstis, plotis))
    return pakeistas


# kiekvienos nuotraukos apatiniame dešiniajame kampe įdės logotipą,

def pav_su_logo(im):
    logo = Image.open('logo_cropped.png')
    logo_location = (im.size[0] - logo.size[0], im.size[1] - logo.size[1], im.size[0], im.size[1])
    im.paste(logo, logo_location, logo)
    return im


# pav_su_logo("dogg_modified.png")

def optimize_dir(directory, aukstis):
    try:
        os.mkdir(f'{directory}/optimized')
        im_num = 0
        for im in katalogo_paveiksliukai(directory):
            ima = Image.open(im)
            imb = pav_resize(ima, aukstis)
            iml = pav_su_logo(imb)
            im_num += 1
            iml.save(f'{directory}/optimized/pic_{im_num}.png')
    except:
        print("Folder already exist.")


optimize_dir('C:\\Users\\Gytis V\\OneDrive\\Desktop\\PYTHON\\Darbas_su_nuotraukomis', 1000)
