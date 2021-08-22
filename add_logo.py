from ImageUtils import ImageUtils as IU
from tqdm import tqdm
from PIL import Image
import os

symlink_path = os.path.abspath(os.getcwd())
before_path = "before"
after_path = "after"
logo_path = "logo"

if not os.path.isdir(before_path):
    os.mkdir(before_path)
if not os.path.isdir(after_path):
    os.mkdir(after_path)
if not os.path.isdir(logo_path):
    os.mkdir(logo_path)

logo_name = "kj_logo.png"
logo = Image.open(os.path.join(logo_path, logo_name))


for im_path in tqdm(os.listdir(before_path)):
    if not (im_path.endswith(".png") or im_path.endswith(".jpg")):
        continue
    IU(os.path.join(before_path, im_path)).add_logo(logo).save(
        os.path.join(after_path, im_path)
    )
