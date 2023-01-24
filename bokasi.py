import tkinter as tk
import tkinter.filedialog as filelog
import PIL.Image
import PIL.ImageTk
root=tk.Tk()
root.geometry("800x600")
root.title("Photo")
root.configure(bg="black")
def openphoto(path):
    newimage=PIL.Image.open(path).resize((78,48)).resize((780,480))#open file and resize file(350x350)
    imagedata=PIL.ImageTk.PhotoImage(newimage)#imagedata=newimage
    label.configure(image=imagedata)#set image on tkinter root
    label.image=imagedata
def openfile():
    fpath=filelog.askopenfilename()
    if fpath:
        openphoto(fpath)

label=tk.Label(bg="black")
button=tk.Button(text="Open file")
button["command"]=lambda:openfile()
button.pack()
label.pack()
tk.mainloop()