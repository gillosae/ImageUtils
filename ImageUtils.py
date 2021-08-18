from PIL import Image


class ImageUtils:
    def __init__(self, input_path: str):
        self.im = Image.open(input_path)
        # print("Input image : " + input_path)
        # print("Input size : " + str(self.im.size))

    def crop_bbox(self, box=None):
        if box is None:
            cropped = self.im.crop(self.im.getbbox())
            print("Cropped size : " + str(cropped.size))
            return self.im.crop(self.im.getbbox())
        else:
            return self.im.crop(box)


if __name__ == "__main__":
    pass
