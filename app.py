from tkinter import *
from PIL import ImageTk
from PIL import *
from PIL import Image 
import tkinter.messagebox
import gmplot
from tkinter.ttk import Notebook,Progressbar,Combobox


class Gmapdownload():
    def __init__(self,root):
        self.root=root
        self.root.title("GOOGLE MAP")
        self.root.geometry("500x300")
        self.root.iconbitmap("logo55.ico")
        self.root.resizable(0,0)


        lat=StringVar()
        lng=StringVar()
        save=StringVar()
        size=StringVar()



#=================buttton by command==========================================================#


        def clear():
            lat.set("")
            lng.set("")
            save.set("")
            size.set("Select Size")
            lab_done.config(text="")



        def create():
            if lat.get()!="":
                if lng.get()!="":
                    if size.get()!="Select Size":
                        if save.get()!="":

                            g = gmplot.GoogleMapPlotter(lat.get(),lng.get(),size.get())
                            g.draw("{}.html".format(save.get()))
                            lab_done.config(text="Map Created Succesfully")
                        else:
                            tkinter.messagebox.showerror("Error","Please Enter Saved Name")
                    else:
                        tkinter.messagebox.showerror("Error","Please Select Size of Map")
                else:
                    tkinter.messagebox.showerror("Error","Please Enter the Longitude city")
            else:
                tkinter.messagebox.showerror("Error","Please Enter Latitude of city ")


#====================hover on button========================================================================#


        def on_enter1(e):
            but_create['background']="black"
            but_create['foreground']="cyan"  
        def on_leave1(e):
            but_create['background']="SystemButtonFace"
            but_create['foreground']="SystemButtonText"
                           

        def on_enter2(e):
            but_clear['background']="black"
            but_clear['foreground']="cyan"  
        def on_leave2(e):
            but_clear['background']="SystemButtonFace"
            but_clear['foreground']="SystemButtonText"



        


#=============================frame===============================================#
        mainframe=Frame(self.root,width=500,height=300,relief="ridge",bd=2)
        mainframe.place(x=0,y=0)

        firstframe=Frame(mainframe,width=495,height=250,relief="ridge",bd=3)
        firstframe.place(x=0,y=0)

        secondframe=Frame(mainframe,width=495,height=45,relief="ridge",bd=3,bg="darkblue")
        secondframe.place(x=0,y=250)

#=================================firstframe===============================================#

        self.original9 = Image.open("C:/Users/SHREYAS/Desktop/shreyas python/py_maps/Gmaps/google.jpg")
        image_file = self.original9.convert('L')
        resized9 = image_file.resize((484, 240),Image.ANTIALIAS)
        self.image9 = ImageTk.PhotoImage(resized9) # Keep a reference, prevent GC
        bglab9=Label(firstframe,image=self.image9).place(x=0,y=0)


        lab_latitude=Label(firstframe,text="Enter Latitude",font=('times new roman',12))
        lab_latitude.place(x=30,y=20)

        ent_latitude=Entry(firstframe,width=23,font=('times new roman',12),relief="ridge",bd=3,textvariable=lat)
        ent_latitude.place(x=10,y=60)

        lab_logitude=Label(firstframe,text="Enter Longitude",font=('times new roman',12))
        lab_logitude.place(x=350,y=20)

        ent_logitude=Entry(firstframe,width=23,font=('times new roman',12),relief="ridge",bd=3,textvariable=lng)
        ent_logitude.place(x=290,y=60)


        lab_zoomsize=Label(firstframe,text="Select Zoom Size",font=('times new roman',12))
        lab_zoomsize.place(x=30,y=120)

        list_size=list(range(13,20))
        list_size_combo=Combobox(firstframe,values=list_size,font=('arial',12),width=10,state="readonly",textvariable=size)
        list_size_combo.set("Select Size")
        list_size_combo.place(x=30,y=160)


        lab_save=Label(firstframe,text="Save Name",font=('times new roman',12))
        lab_save.place(x=350,y=120)

        ent_save=Entry(firstframe,width=23,font=('times new roman',12),relief="ridge",bd=3,textvariable=save)
        ent_save.place(x=290,y=160)

        lab_done=Label(firstframe,text="",font=('times new roman',12))
        lab_done.place(x=150,y=210)

        

#==================================secondframe==================================================================#

        but_create=Button(secondframe,text="Create Map",width=14,font=('times new roman',12),cursor="hand2",command=create)
        but_create.place(x=70,y=3)
        but_create.bind("<Enter>",on_enter1)
        but_create.bind("<Leave>",on_leave1)

        but_clear=Button(secondframe,text="Clear",width=14,font=('times new roman',12),cursor="hand2",command=clear)
        but_clear.place(x=270,y=3)
        but_clear.bind("<Enter>",on_enter2)
        but_clear.bind("<Leave>",on_leave2)

        


if __name__ == "__main__":
    root=Tk()
    app=Gmapdownload(root)
    root.mainloop()
