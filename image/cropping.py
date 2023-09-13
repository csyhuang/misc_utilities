"""
Utilities to do regular cropping over a group of files
"""
import re
import os
import glob
from PIL import Image


def resize_image(img_path, new_img_path, size):
    """

    :param img_path:
    :param size: a 2-tuple of (width, height)
    :return:
    """
    im = Image.open(img_path)
    im1 = im.resize(size)
    im1.save(new_img_path)
    return im1


def crop_image(img_path, left, top, right, bottom, show_cropped=False):

    # Opens a image in RGB mode
    im = Image.open(img_path)

    # Cropped image of above dimension
    im1 = im.crop((left, top, right, bottom))

    if show_cropped:
        # Shows the image in image viewer
        im1.show()
    return im1


def crop_images_in_a_directory(
        dir_path, left, top, right, bottom, prefix,
        suffix_format="{:03d}.png", new_dir='', png_to_jpg=True,
        show_cropped=False, filetype="*.png"):
    """
    Crop images that exist in a directory, and save them in the same directory in order.
    :param dir_path:
    :param left:
    :param top:
    :param right:
    :param bottom:
    :param prefix:
    :param suffix_format:
    :param show_cropped:
    :return:
    """
    list_of_files = sorted(glob.glob(dir_path + filetype))
    print("list_of_files: {}".format(list_of_files))
    for idx, file in enumerate(list_of_files):
        img = crop_image(file, left, top, right, bottom, show_cropped=show_cropped)
        if suffix_format is None:
            if len(new_dir) > 0:
                image_fname = file.split("/")[-1]
                new_fname = new_dir + image_fname
            else:
                raise ValueError("If suffix_format is None, new_dir should not be empty.")
        else:
            new_fname = prefix + suffix_format.format(idx)
        print("Check before img.save()... The path is: {}".format(dir_path + new_fname))
        # raise ValueError("Test")
        if png_to_jpg:
            img = img.convert('RGB')
            new_fname = new_fname.replace(".png", ".jpg")
        # *** Check if directory exists ***
        if not os.path.isdir(dir_path+new_dir):
            os.mkdir(dir_path+new_dir)
        img.save(dir_path + new_fname)
    return None

