from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
import os

root = Tk()
root.title('check')
root.geometry('{}x{}'.format(720, 480))
root.resizable(width=False, height=False)
#top frame
frame = Frame(root, width=720, height=480)
frame.grid()

root.mainloop()