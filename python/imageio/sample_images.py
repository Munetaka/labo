import imageio
import os

# todo: get sample from original site.
# import urllib2
# from bs4 import BeautifulSoup
# html = urllib2.urlopen("http://imageio.readthedocs.io/en/latest/standardimages.html")
# soup = BeautifulSoup(html, "lxml")
# print(soup.select(".simple"))

sample_list = {
    "newtonscradle.gif": "Animated GIF of a newton's cradle",
    "cockatoo.mp4": "Video file of a cockatoo",
    "stent.npz": "Volumetric image showing a stented abdominal aorta",
    "astronaut.png": "Image of the astronaut Eileen Collins",
    "camera.png": "Classic grayscale image of a photographer",
    "checkerboard.png": "Black and white image of a chekerboard",
    "chelsea.png": "Image of Stefan's cat",
    "clock.png": "Photo of a clock with motion blur (Stefan van der Walt)",
    "coffee.png": "Image of a cup of coffee (Rachel Michetti)",
    "coins.png": "Image showing greek coins from Pompeii",
    "horse.png": "Image showing the silhouette of a horse (Andreas Preuss)",
    "hubble_deep_field.png": "Photograph taken by Hubble telescope (NASA)",
    "immunohistochemistry.png": "Immunohistochemical (IHC) staining",
    "moon.png": "Image showing a portion of the surface of the moon",
    "page.png": "A scanned page of text",
    "text.png": "A photograph of handdrawn text",
    "wikkie.png": "Image of Almar's cat",
    "chelsea.zip": "The chelsea.png in a zipfile (for testing)"
    }

print('we have %d samples' % len(sample_list))
for sample_name, desc in sample_list.items():
    root, ext = os.path.splitext(sample_name)
    if ext in ('.png', '.gif'):
        im = imageio.imread('imageio:' + sample_name)
        print('img: ' + sample_name + ', size: ' + str(im.shape))
    elif ext == '.mp4':
        print('movie: ' + sample_name)
    elif ext == '.zip':
        print('zip: ' + sample_name)
    elif ext == '.npz':
        print('npz: ' + sample_name)
    else:
        print('unknown: ' + sample_name)
