from ImageUtils import ImageUtils as IU
from tqdm import tqdm
from PIL import Image
import os

symlink_path = os.path.abspath(os.getcwd())
before_path = "before"
after_path = "after"

if not os.path.isdir(before_path):
    os.mkdir(before_path)
if not os.path.isdir(after_path):
    os.mkdir(after_path)

for dir_path in os.listdir(before_path):
    if os.path.isdir(os.path.join(before_path, dir_path)):
        for im_path in tqdm(os.listdir(os.path.join(before_path, dir_path))):
            if not os.path.isdir(os.path.join(after_path, dir_path)):
                os.mkdir(os.path.join(after_path, dir_path))
            if not (im_path.endswith(".png") or im_path.endswith(".jpg")):
                continue
            IU(os.path.join(before_path, dir_path, im_path)).wash().save(
                os.path.join(after_path, dir_path, im_path)
            )
