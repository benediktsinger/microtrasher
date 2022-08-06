import pickle
import numpy as np
import mrcfile.utils as utils
import mrcfile


def preload(path):
    file = mrcfile.open(path)
    object = np.array(file.data,dtype=utils.data_dtype_from_header(file.header))*4
    np.save(path.replace("mrc","npy"),object)


if __name__ == "__main__":
    path = "./example_data/8.mrc"
    preload(path)