from tkinter import *
import sqlite3

def database():
   name1=Fullname.get()
   email=Email.get()
   gender=Gender.get()
   time1=Time.get()
   date=Date.get()
   conn = sqlite3.connect('Form.db')
   with conn:
      cursor=conn.cursor()
   cursor.execute('CREATE TABLE IF NOT EXISTS Appoinment (Fullname TEXT,Email TEXT,Gender TEXT,Time TEXT,Date TEXT)')
   cursor.execute('INSERT INTO Appointment (FullName,Email,Gender,Time,Date) VALUES(?,?,?,?,?)',(name1,email,gender,time1,date,))
   conn.commit()
   Reset()
def Reset():
   Fullname.set("")
   Email.set("")
   Gender.set("")
   Time.set("")
   Date.set("")   
   
   
root = Tk()
root.geometry('500x500')
root.title("Appointment Form")
root.configure(bg="steelblue")

Fullname=StringVar()
Email=StringVar()
Gender = StringVar()
Time=StringVar()
Date= StringVar()   

Frame1 = Frame(root)
Frame1.place(relx=0.02, rely=0.03, relheight=0.94, relwidth=0.96)
Frame1.configure(relief=GROOVE)
Frame1.configure(borderwidth="2")
Frame1.configure(relief=GROOVE)
Frame1.configure(background="steelblue")
Frame1.configure(highlightbackground="steelblue")
Frame1.configure(highlightcolor="black")
Frame1.configure(width=925)
             
Message6 = Message(Frame1)
Message6.place(relx=0.09, rely=0.01, relheight=0.15, relwidth=0.86)
Message6.configure(background="steelblue")
Message6.configure(font="Arial")
Message6.configure(foreground="#000000")
Message6.configure(highlightbackground="steelblue")
Message6.configure(highlightcolor="black")
Message6.configure(text='ABC HOSPITAL APPOINTMENT FORM')
Message6.configure(width=791)




label_1 = Label(root, text="Full Name",bg="steelblue",width=20,font=("bold", 10))
label_1.place(x=80,y=130)

entry_1 = Entry(root,textvar=Fullname)
entry_1.place(x=240,y=130)

label_2 = Label(root, text="Email",bg="steelblue",width=20,font=("bold", 10))
label_2.place(x=68,y=180)

entry_2 = Entry(root,textvar=Email)
entry_2.place(x=240,y=180)

label_3 = Label(root, text="Gender",bg="steelblue",width=20,font=("bold", 10))
label_3.place(x=70,y=230)

entry_3 = Entry(root,textvar=Gender)
entry_3.place(x=240,y=230)

label_4 = Label(root, text="Time",bg="steelblue",width=20,font=("bold", 10))
label_4.place(x=66,y=280)

entry_4 = Entry(root,textvar=Time)
entry_4.place(x=240,y=280)

label_5 = Label(root, text="Date",bg="steelblue",width=20,font=("bold", 10))
label_5.place(x=66,y=330)

entry_5 = Entry(root,textvar=Date)
entry_5.place(x=240,y=330)

var2= IntVar()
Button(root, text='Submit',width=15,bg='gray85',fg='black',command=database).place(x=180,y=380)
#Button(root, text='Reset',width=15,bg='gray85',fg='black',command=Reset).place(x=300,y=380)


root.mainloop()
