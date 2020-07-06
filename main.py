from tkinter import *
from subprocess import call


def click_appoint():
    call(["python", "appoint.py"])
def click_getinfo():
    call(["python","getinfoui.py"])
def click_update():
    call(["python","update.py"])    


class HOSPITAL_MANAGEMENT:
    def __init__(self):
        root = Tk()
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#ffffff' # X11 color: 'white'
        _ana1color = '#ffffff' # X11 color: 'white'
        _ana2color = '#ffffff' # X11 color: 'white'
        font14 = "-family {Arial} -size 15 -weight bold -slant "  \
            "roman -underline 0 -overstrike 0"
        font16 = "-family {Arial} -size 40 -weight bold "  \
            "-slant roman -underline 0 -overstrike 0"
        font9 = "-family {Arial} -size 9 -weight normal -slant "  \
            "roman -underline 0 -overstrike 0"

        root.geometry("1366x768")
        root.title("HOSPITAL MANAGEMENT")
        root.configure(background="steelblue")
        root.configure(highlightbackground="steelblue")
        root.configure(highlightcolor="black")



        self.menubar = Menu(root,font="arial",bg='steelblue',fg='black')
        root.configure(menu = self.menubar)

        self.Frame1 = Frame(root)
        self.Frame1.place(relx=0.02, rely=0.03, relheight=0.94, relwidth=0.96)
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(background="steelblue")
        self.Frame1.configure(highlightbackground="steelblue")
        self.Frame1.configure(highlightcolor="black")
        self.Frame1.configure(width=925)

        self.Message6 = Message(self.Frame1)
        self.Message6.place(relx=0.09, rely=0.01, relheight=0.15, relwidth=0.86)
        self.Message6.configure(background="steelblue")
        self.Message6.configure(font=font16)
        self.Message6.configure(foreground="#000000")
        self.Message6.configure(highlightbackground="steelblue")
        self.Message6.configure(highlightcolor="black")
        self.Message6.configure(text='ABC HOSPITAL')
        self.Message6.configure(width=791)

        self.Button1 = Button(self.Frame1)
        self.Button1.place(relx=0.28, rely=0.26, height=63, width=566)
        self.Button1.configure(activebackground="GRAY85")
        self.Button1.configure(activeforeground="white")
        self.Button1.configure(background="gray85")
        self.Button1.configure(disabledforeground="#bfbfbf")
        self.Button1.configure(font=font14)
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''1.APPOINTMENT''')
        self.Button1.configure(width=566)
        self.Button1.configure(command=click_appoint)


        self.Button2 = Button(self.Frame1)
        self.Button2.place(relx=0.28, rely=0.41, height=63, width=566)
        self.Button2.configure(activebackground="#d9d9d9")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="#d9d9d9")
        self.Button2.configure(disabledforeground="#bfbfbf")
        self.Button2.configure(font=font14)
        self.Button2.configure(foreground="#000000")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(text='''2.UPDATE''')
        self.Button2.configure(width=566)
        self.Button2.configure(command=click_update)
        
        self.Button3 = Button(self.Frame1)
        self.Button3.place(relx=0.28, rely=0.56, height=63, width=566)
        self.Button3.configure(activebackground="#d9d9d9")
        self.Button3.configure(activeforeground="#000000")
        self.Button3.configure(background="#d9d9d9")
        self.Button3.configure(disabledforeground="#bfbfbf")
        self.Button3.configure(font=font14)
        self.Button3.configure(foreground="#000000")
        self.Button3.configure(highlightbackground="#d9d9d9")
        self.Button3.configure(highlightcolor="black")
        self.Button3.configure(pady="0")
        self.Button3.configure(text='''3.PATIENT LIST''')
        self.Button3.configure(width=566)
        self.Button3.configure(command=click_getinfo)


        self.Button4 = Button(self.Frame1)
        self.Button4.place(relx=0.28, rely=0.71, height=63, width=566)
        self.Button4.configure(activebackground="#d9d9d9")
        self.Button4.configure(activeforeground="#000000")
        self.Button4.configure(background="#d9d9d9")
        self.Button4.configure(disabledforeground="#bfbfbf")
        self.Button4.configure(font=font14)
        self.Button4.configure(foreground="#000000")
        self.Button4.configure(highlightbackground="#d9d9d9")
        self.Button4.configure(highlightcolor="black")
        self.Button4.configure(pady="0")
        self.Button4.configure(text='''4.EXIT''')
        self.Button4.configure(width=566)
        self.Button4.configure(command=quit)
        root.mainloop()


if __name__ == '__main__':
    GUUEST=HOSPITAL_MANAGEMENT()


