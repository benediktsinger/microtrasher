
import tkinter as tk
from PIL import ImageTk, Image, ImageEnhance
from io import BytesIO
import numpy as np
import mrcfile
import pickle


class gui(object):
    """Takes a numpy array and maps it as an PIL-image to a tkinter canvas, where the leading edge can drawn via the mouse.
    Additionally the user can select from a variety of geometric attributes, which will be used for the classification of the provided filaments
    The return_array and return_dict objects contain the information being accessed from cpp and are assigned, if the 'Start' Button is pressed."""

    def __init__(self,path):
        self.arr = np.load(path)

        self.root = tk.Tk()

        self.image = Image.fromarray(self.arr,mode="I;16")
        #print(np.array(self.file.data,dtype=utils.data_dtype_from_header(self.file.header)).min())
        #self.image = ImageEnhance.Contrast(self.raw)
        #self.image.show()
        self.image=self.image.resize((500,500))
        self.btn_pic = ImageTk.PhotoImage(image=self.image)

        #self.img_btn  = tk.Button(self.root, image=self.btn_pic, command=self.select_image)
        #self.img_btn.pack()   

        self.canvas = tk.Canvas(self.root, height=500, width=500)
        self.canvas.pack()
        self.canvas.create_image(0,0,image=self.btn_pic)

        self.root.title("MicroPrev")
        #self.root.geometry(450)
        self.root.mainloop()

    def select_image(self):
        print("Clicked me!")



if __name__ == "__main__":
    gui(path="./example_data/8.npy")
