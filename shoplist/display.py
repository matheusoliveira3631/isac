from tkinter import *
from PIL import Image, ImageTk 

class image_viewer:
    
    def __init__(self, path_to_image):
        self.path=path_to_image
    
    def show(self):
        app=Tk()
        app.title('Lista de compras')
        tkimage = ImageTk.PhotoImage(Image.open(self.path))
        Label(app, image=tkimage).pack()
        app.mainloop()