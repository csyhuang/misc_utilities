"""
Utilities to do regular cropping over a group of files
"""
import glob
from PIL import Image


def crop_image(img_path, left, top, right, bottom, show_cropped=False):

    # Opens a image in RGB mode
    im = Image.open(img_path)

    # Cropped image of above dimension
    im1 = im.crop((left, top, right, bottom))

    if show_cropped:
        # Shows the image in image viewer
        im1.show()
    return im1


def crop_images_in_a_directory(dir_path, left, top, right, bottom, prefix, show_cropped=False):
    """
    Crop images that exist in a directory, and save them in the same directory in order.
    :param dir_path:
    :param left:
    :param top:
    :param right:
    :param bottom:
    :param prefix:
    :param show_cropped:
    :return:
    """
    list_of_files = sorted(glob.glob(dir_path + '*.png'))
    print("list_of_files: {}".format(list_of_files))
    for idx, file in enumerate(list_of_files):
        img = crop_image(file, left, top, right, bottom, show_cropped=show_cropped)
        new_fname = prefix + "{:03d}.png".format(idx)
        img.save(dir_path + new_fname)
    return None

