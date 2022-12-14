import tkinter as tk
import sys
import numpy as np
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
        """Determine the operating system and give appropriate reaction to scrolling"""
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
    def __init__(self,classname,filepath,img_per_row,width):
        super().__init__(className=classname)

        self.geometry(str(width*img_per_row+30*img_per_row)+"x"+str(250*4))
        self.title("MICRO TRASH ???????????")

        sbf = ScrollbarFrame(self)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        sbf.grid(row=0, column=0, sticky='nsew')
        frame = sbf.scrolled_frame

        filepath = os.path.join(filepath,"preload")
        filelist = os.listdir(filepath)
        if not os.path.isdir(filepath.replace("preload","discarded")):    
            os.mkdir(filepath.replace("preload","discarded"))
        lst = [(i,j) for i in range(int(np.ceil(len(filelist) / img_per_row))) for j in range(img_per_row)]
        for i in range(len(filelist)):
            img = tk.PhotoImage(file=os.path.join(filepath,filelist[i]))
            tk.Button(frame, image=img, borderwidth="1", relief="solid",command=lambda j=(img,i): self.select_image(j[0],os.path.join(filepath,filelist[j[1]]))). \
                grid(row=lst[i][0], column=lst[i][1], padx=10,pady=10)

    
    def select_image(self,img,filename):
        """Move the clicked on mrc file to the discarded folder"""
        if os.path.isfile(filename):
            os.remove(filename)
        else:
            print(filename.replace("png","mrc"),'already discarded!')
            return
        mrc_file = filename.replace("png","mrc")
        print("Discarding " + mrc_file)
        os.rename(os.path.join(os.path.split(filename)[0].replace('preload','')+os.path.basename(mrc_file)),mrc_file.replace("preload","discarded"))

