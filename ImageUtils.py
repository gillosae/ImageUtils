from PIL import Image, ExifTags


class ImageUtils:
    def __init__(self, input_path: str):
        self.im = Image.open(input_path)
        self.im_width, self.im_height = self.im.size
        # print("Input image : " + input_path)
        # print("Input size : " + str(self.im.size))

    def crop_bbox(self, box=None):
        if box is None:
            cropped = self.im.crop(self.im.getbbox())
            print("Cropped size : " + str(cropped.size))
            return self.im.crop(self.im.getbbox())
        else:
            return self.im.crop(box)

    def add_logo(self, logo):
        logo_width, logo_height = logo.size

        # Set logo size, logo width = image width * 80%
        if logo_width > logo_height:  # landscape
            new_logo_width = self.im_width * 7 / 10
        else:  # portrait
            new_logo_width = self.im_width * 5 / 10
        new_logo_height = logo_height * new_logo_width / logo_width

        # Set logo pos
        logo_xpos = int(self.im_width / 2 - new_logo_width / 2)
        logo_ypos = int(self.im_height - new_logo_height)

        # Resize logo
        logo = logo.resize((int(new_logo_width), int(new_logo_height)))

        # Add logo to Image
        self.im.paste(logo, (logo_xpos, logo_ypos), logo)
        return self.im


if __name__ == "__main__":
    pass


# TO DO
## orientation problem
## multiple folders
