import imageio
import matplotlib.pyplot as plt


def plt_img(im):
    plt.imshow(im)
    plt.show()

###
# Read an image of a cat
###

im = imageio.imread('imageio:chelsea.png')
print(im.shape)
print(im.mean())
# plt_img(img)


###
# Read from fancy sources
###

# can't get image from url
# im = imageio.imread('http://upload.wikimedia.org/wikipedia/commons/d/de/Wikipedia_Logo_1.0.png')
# doesn't work visvis.imshow
# import visvis as vv
# vv.imshow(im)


###
# Iterate over frames in a movie
###

# reader = imageio.get_reader('imageio:cockatoo.mp4')
# for i, im in enumerate(reader):
#     print(type(im))
#     exit()
#     print('Mean of frame %i is %1.1f' % (i, im.mean()))


###
# Volume data
###

# doesn't work visvis.volshow
# import visvis as vv
# vol = imageio.volread('imageio:stent.npz')
# vv.volshow(vol)
