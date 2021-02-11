from PIL import Image 
import numpy as np
from collections import defaultdict

import sys


_, input_file = sys.argv

img = Image.open(input_file)

pix = np.array(img)

clr_num = defaultdict(lambda: 0)

for pixel in pix.reshape(-1, 3):
    clr_num[tuple(pixel)] += 1
    
colors_by_freq = sorted(clr_num.items(), key=lambda item: -item[1]);


for c in colors_by_freq:
    
    rgb, freq = c
    r, g, b, *_ = rgb
    print(r, g, b, sep=', ', end=': ')
    print(freq)
