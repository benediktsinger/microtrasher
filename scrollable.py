import tkinter as tk
import sys
import os

#https://stackoverflow.com/questions/3085696/adding-a-scrollbar-to-a-group-of-widgets-in-tkinter/3092341#3092341
#https://stackoverflow.com/questions/67319035/scroll-through-multiple-images-in-tkinter

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
        self.canvas.bind_all("<MouseWheel>", self.on_mousewheel, add=True)
        self.canvas.bind_all("<Button-4>", self.on_mousewheel, add=True)
        self.canvas.bind_all("<Button-5>", self.on_mousewheel, add=True)

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

    def on_mousewheel(self,event):
        y_steps = 2
        if sys.platform == "windows":
            y_steps = int(-event.delta/abs(event.delta))
            self.canvas.yview_scroll(y_steps, "units")    
        elif sys.platform == "linux":
            if event.num == 4:
                y_steps *= -1
            self.canvas.yview_scroll(y_steps, "units")
        elif sys.platform == "darwin": 
            y_steps = int(event.delta)
            self.canvas.yview_scroll(y_steps, "units")


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
        iamge_container = []
        integer = []
        for row in range(7):
                    iamge_container.append(tk.PhotoImage(file="./example_data/preload/8_" + str(row) + ".png"))
                    tk.Button(frame, image=iamge_container[row],
                         borderwidth="1", relief="solid",command=lambda: select_image(iamge_container)) \
                        .grid(row=row, column=0, padx=10,pady=10)
        print(iamge_container)

    
def select_image(list,index):
    print(index)
    print(list[index])
    

if __name__ == "__main__":
    filelist = "./example_data/preload"
    App().mainloop()