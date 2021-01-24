import os

import skimage
from skimage import data

filename = os.path.join(skimage.data_dir, 'moon.png')

from skimage import io
maze = io.imread(filename)