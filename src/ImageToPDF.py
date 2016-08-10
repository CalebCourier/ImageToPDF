# __author__ = 'Caleb'
from PIL import Image
from Tkinter import Toplevel
from Tkinter import Button
from Tkinter import Label
from Tkinter import Tk
from tkFileDialog import askopenfilename

def messageWindow(title, message, self):
    win = Toplevel()
    win.title(title)
    win.geometry("500x100")
    Label(win, text=message).pack()
    Button(win, text='Thanks!', command=self.destroy).pack()
    win.protocol('WM_DELETE_WINDOW', self.destroy)
    return win

root = Tk()
root.withdraw()
fullFilePath = askopenfilename()
filePathName = fullFilePath.split(".")[0]
inputImage = Image.open(fullFilePath)
inputImage.save(filePathName + ".pdf", "PDF", quality=1000, optimize=True, progressive=True)
messageWindow('File Converted', 'Look for your new pdf at: ' + filePathName + '.pdf', root).mainloop()
