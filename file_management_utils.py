import os


def retain_cr2_files(jpg_dir: str, cr2_dir: str, cr2_retain_dir='retain/', jpg_suffix='.JPG', cr2_suffix='.CR2'):
    """
    Retain CR2 images with suffix from files in jpg_dir.
    :param jpg_dir:
    :param cr2_dir:
    :param cr2_retain_dir:
    :param jpg_suffix:
    :param cr2_suffix:
    :return:
    """
    retain_list = [x.replace(".JPG", ".CR2") for x in os.listdir(jpg_dir) if x.endswith(".JPG")]
    print(retain_list)
    if not os.path.exists(cr2_dir + cr2_retain_dir):
        os.makedirs(cr2_dir + cr2_retain_dir)
    for retain_file in retain_list:
        print(f"retain_file = {retain_file}")
        try:
            os.replace(cr2_dir + retain_file, cr2_dir + cr2_retain_dir + retain_file)
        except:
            print(f"Cannot rename file {retain_file}.")



if __name__ == "__main__":
    jpg_dir = "/Users/claresyhuang/Pictures/20221230-GyuKaku-Lincoln-Park/jpg_files/"
    cr2_dir = "/Users/claresyhuang/Pictures/20221230-GyuKaku-Lincoln-Park/cr2_files/"
    cr2_retain_dir = "retain/"
    retain_cr2_files(jpg_dir=jpg_dir, cr2_dir=cr2_dir, cr2_retain_dir=cr2_retain_dir)
