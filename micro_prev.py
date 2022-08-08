from textwrap import fill
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

        self.canvas = tk.Canvas(self.root)

        # scrollbar
        self.sb = tk.Scrollbar(self.root,orient=tk.VERTICAL,command=self.canvas.yview)
        self.sb.grid(row=0, column=1, sticky=tk.N+tk.S,rowspan=1)
        self.canvas['yscrollcommand'] = self.sb.set

        self.btn_pic = tk.PhotoImage(file="./example_data/8.png")
        self.button = tk.Button(
            self.root, image=self.btn_pic, command=self.select_image, borderwidth=0
        )
        self.button.grid(row=0,column=0,padx=10,pady=10)

        self.btn_pic1 = tk.PhotoImage(file="./example_data/8_1.png")
        self.button1 = tk.Button(
            self.root, image=self.btn_pic1, command=self.select_image, borderwidth=0
        )
        self.button1.grid(row=1,column=0,padx=10,pady=10)

        self.root.mainloop()

    def select_image(self):
        print("Clicked me!")


if __name__ == "__main__":
    gui(path="./example_data/8.npy")
