import tkinter as tk

#https://stackoverflow.com/questions/3085696/adding-a-scrollbar-to-a-group-of-widgets-in-tkinter/3092341#3092341

class ScrollbarFrame(tk.Frame):
    """
    Extends class tk.Frame to support a scrollable Frame 
    This class is independent from the widgets to be scrolled and 
    can be used to replace a standard tk.Frame
    """
    def __init__(self, parent, **kwargs):
        tk.Frame.__init__(self, parent, **kwargs)

        # The Scrollbar, layout to the right
        vsb = tk.Scrollbar(self, orient="vertical")
        vsb.pack(side="right", fill="y")

        # The Canvas which supports the Scrollbar Interface, layout to the left
        self.canvas = tk.Canvas(self, borderwidth=0, background="#ffffff")
        self.canvas.pack(side="left", fill="both", expand=True)

        # Bind the Scrollbar to the self.canvas Scrollbar Interface
        self.canvas.configure(yscrollcommand=vsb.set)
        vsb.configure(command=self.canvas.yview)

        # The Frame to be scrolled, layout into the canvas
        # All widgets to be scrolled have to use this Frame as parent
        self.scrolled_frame = tk.Frame(self.canvas, background=self.canvas.cget('bg'))
        self.canvas.create_window((4, 4), window=self.scrolled_frame, anchor="nw")

        # Configures the scrollregion of the Canvas dynamically
        self.scrolled_frame.bind("<Configure>", self.on_configure)

    def on_configure(self, event):
        """Set the scroll region to encompass the scrolled frame"""
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        sbf = ScrollbarFrame(self)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        sbf.grid(row=0, column=0, sticky='nsew')
        # sbf.pack(side="top", fill="both", expand=True)

        # Some data, layout into the sbf.scrolled_frame
        frame = sbf.scrolled_frame
        self.btn_pic = tk.PhotoImage(file="./example_data/8.png")
        self.button = tk.Button(
            frame, image=self.btn_pic, command=lambda: select_image("./example_data/8.png"), borderwidth=0
        )
        self.button.grid(row=0,column=0,padx=10,pady=10)

        self.btn_pic1 = tk.PhotoImage(file="./example_data/8_1.png")
        self.button1 = tk.Button(
            frame, image=self.btn_pic1, command=lambda: select_image("./example_data/8_1.png"), borderwidth=0
        )
        self.button1.grid(row=1,column=0,padx=10,pady=10)

    def map_image_to_frame(filelist):
        pass
    
def select_image(filename):
    print("Changed",filename)


if __name__ == "__main__":
    App().mainloop()