#!/usr/bin/env python3

from PIL import Image 
import numpy as np

import sys

_, input_file, output_file = sys.argv

img = Image.open(input_file)

pix = np.array(img)

tr_pix = pix.transpose((1, 0, 2))

tr_img = Image.fromarray(tr_pix)

tr_img.save(output_file)

