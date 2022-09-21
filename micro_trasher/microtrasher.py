#!/usr/bin/python3
from micro_trasher import scrollable

from PIL import Image
import numpy as np
import mrcfile.utils as utils
import mrcfile
import argparse
import os

parser = argparse.ArgumentParser(description="Micrograph Selection Pipeline")
parser.add_argument("--images_per_row", default=4, type=int, help="Number of images displayed per row")
parser.add_argument("--directory", default="./example_data", type=str, help="Directory of the MRC files")
parser.add_argument("--contrast", default=2, type=int, help="Contrast for the MRC files")
parser.add_argument("--brightness", default=0, type=int, help="Value to add for the brightness")
parser.add_argument("--image_width", default=250, type=int, help="Width of each image to be displayed")


def main():
    args = parser.parse_args()
    # iterate over files of given directory and preload each file
    iterate_over_dir(args.directory, args.contrast,args.brightness,args.image_width)
    scrollable.App("MICRO TRASH",args.directory,args.images_per_row,args.image_width).mainloop()
    cleanup(args.directory)


def mrc_to_png(path, contrast,offset,width):
    """
    Reads the MRC file data according to the data type as provided in the header as numpy array. Then a PIL image object is created, appropriatly resized and stored as png file
    """
    if os.path.isfile(os.path.join(os.path.dirname(path),"preload",os.path.basename(path).replace("mrc","png"))):
        return
    file = mrcfile.open(path)
    object = (
        np.array(file.data, dtype=utils.data_dtype_from_header(file.header))
    )
    image = Image.fromarray(np.uint8(object)).convert('RGB')
    aspect_ratio = image.size[0]/image.size[1]
    image = image.resize((int(width*aspect_ratio), width))
    print("Converting: ",path)
    image.save(os.path.join(os.path.dirname(path),"preload",os.path.basename(path).replace("mrc","png")))


def iterate_over_dir(input_dir,contrast,offset,width):
    """Iterates over the given input directory and calls for every MRC file in the folder the mrc to png function and stores it in a subfolder with the name "preloaded_micrographs" """
    if "preload" not in os.listdir(input_dir):
        os.mkdir(os.path.join(input_dir,"preload"))
    for file in os.listdir(input_dir):
        if file.endswith("mrc"):
            mrc_to_png(os.path.join(input_dir,file), contrast, offset,width)

def cleanup(input_dir):
    """Delets the created folder with the preloaded png files"""
    os.rmdir(os.path.join(input_dir,"preload"))

if __name__ == "microtrasher":
    main()
