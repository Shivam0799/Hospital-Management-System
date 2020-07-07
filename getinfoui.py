import tkinter
import subprocess
from tkinter import *
import sqlite3

def database():
   name1=Fullname.get()
   email=Email.get()
   gender=Gender.get()
   time1=Time.get()
   date=Date.get()
   label_1 = Label(Frame1, text="Full Name",bg="steelblue",width=20,font=("bold", 10)).grid(row=0,column=0)
   label2 = Label(Frame1, text="Email",bg="steelblue",width=20,font=("bold", 10)).grid(row=0,column=1)
   label_3 = Label(Frame1, text="Gender",bg="steelblue",width=20,font=("bold", 10)).grid(row=0,column=2)
   label_4 = Label(Frame1, text="Time",bg="steelblue",width=20,font=("bold", 10)).grid(row=0,column=3)
   label_5 = Label(Frame1, text="Date",bg="steelblue",width=20,font=("bold", 10)).grid(row=0,column=4)
   conn = sqlite3.connect('Form.db')
   cursor=conn.cursor()
   cursor.execute('SELECT * FROM Appointment ORDER BY Date,Time')
   for index,row in enumerate(cursor):
       Label(Frame1, text=row[0],bg="steelblue",font=("bold", 10)).grid(row=index+1,column=0)            
       Label(Frame1, text=row[1],bg="steelblue",font=("bold", 10)).grid(row=index+1,column=1)            
       Label(Frame1, text=row[2],bg="steelblue",font=("bold", 10)).grid(row=index+1,column=2)            
       Label(Frame1, text=row[3],bg="steelblue",font=("bold", 10)).grid(row=index+1,column=3)            
       Label(Frame1, text=row[4],bg="steelblue",font=("bold", 10)).grid(row=index+1,column=4)                        
   
   conn.commit()
   
root = Tk()
root.geometry('860x500')
root.title("Appointment")
root.configure(bg="steelblue")
Frame1 = Frame(root)
Frame1.place(relx=0.02, rely=0.03, relheight=0.94, relwidth=0.96)
Frame1.configure(relief=GROOVE)
Frame1.configure(borderwidth="2")
Frame1.configure(relief=GROOVE)
Frame1.configure(background="steelblue")
Frame1.configure(highlightbackground="steelblue")
Frame1.configure(highlightcolor="black")
Frame1.configure(width=925)

Fullname=StringVar()
Email=StringVar()
Gender = StringVar()
Time=StringVar()
Date= StringVar()
database()
root.mainloop()

   
