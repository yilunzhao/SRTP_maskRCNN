
from PIL import Image
import numpy as np
import shutil
import os

src_dir = "orig_mask"
dest_dir = "cv2_mask"

for label_name in os.listdir(src_dir):
    old_mask = src_dir + "/" + label_name
    img = Image.open(old_mask)
    img = Image.fromarray(np.uint8(np.array(img)))
    new_mask = os.path.join(dest_dir, label_name)
    img.save(new_mask)



