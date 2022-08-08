from PIL import Image
import numpy as np
import mrcfile.utils as utils
import mrcfile
import os


def mrc_to_png(path, contrast):
    """
    Reads the MRC file data according to the data type as provided in the header as numpy array. Then a PIL image object is created, appropriatly resized and stored as png file
    """
    file = mrcfile.open(path)
    object = (
        np.array(file.data, dtype=utils.data_dtype_from_header(file.header)) * contrast
    )
    image = Image.fromarray(object, mode="I;16")
    image = image.resize((400, 400))
    image.save("/".join(path.split("/")[:-1])+"/preload/"+path.split("/")[-1].replace("mrc","png"))


def iterate_over_dir(input_dir,contrast):
    """Iterates over the given input directory and calls for every MRC file in the folder the mrc to png function and stores it in a subfolder with the name "preloaded_micrographs" """
    if "preload" not in os.listdir(input_dir): os.mkdir(input_dir + "preload")
    for file in os.listdir(input_dir):
        if file.endswith("mrc"):
            mrc_to_png(input_dir + file, contrast)


if __name__ == "__main__":
    path = "./example_data/"
    # iterate over files of given directory and preload each file
    iterate_over_dir(path, 4)
