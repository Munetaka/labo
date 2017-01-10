import imageio
import numpy as np
# imageio.plugins.ffmpeg.download()

movie_file = 'sample.mp4'
print(movie_file)
vid = imageio.get_reader(movie_file, "ffmpeg")

print('vid')
print(vid)

image = vid.get_data(10)

array = np.array(image)
print(array.shape())
