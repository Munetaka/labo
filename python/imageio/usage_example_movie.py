import imageio
import os

reader = imageio.get_reader('imageio:cockatoo.mp4')
fps = reader.get_meta_data()['fps']

writer = imageio.get_writer(os.path.abspath(os.path.dirname(__file__)) + '/cockatoo_gray.mp4', fps=fps)

for im in reader:
    # gary scale
    writer.append_data(im[:, :, 1])
    # original color
    # writer.append_data(im)
print(reader.get_meta_data())

writer.close()
