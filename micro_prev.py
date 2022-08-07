import tkinter as tk
from io import BytesIO
import numpy as np
import mrcfile
import pickle


class gui(object):
    """
    Creates a scrollable display of PNG files. By clicking on the individual files it gets moved into another folder
    """

    def __init__(self, path):
        # image loading
        self.root = tk.Tk()
        self.root.geometry("800x800")
        self.btn_pic = tk.PhotoImage(file="preload.png")
        self.img_label = tk.Label(image=self.btn_pic)
        self.button = tk.Button(
            self.root, image=self.btn_pic, command=self.select_image, borderwidth=0
        )
        self.button.pack(pady=30)

        self.root.mainloop()

    def select_image(self):
        print("Clicked me!")


if __name__ == "__main__":
    gui(path="./example_data/8.npy")
