from tkinter import *
import tkinter.messagebox 
import sqlite3
import os
from subprocess import call
import sys
import time

conn = sqlite3.connect('form.db')
c = conn.cursor()

class Application:
    def __init__(self, master):
        self.master = master
        # heading label
        self.heading = Label(master, text="UPDATE/CANCEL",  bg='steelblue', font=('arial 18 bold'))
        self.heading.place(x=30, y=20)

        # search criteria -->name 
        self.name = Label(master, text="NAME", bg='steelblue', font=('arial 14 bold'))
        self.name.place(x=0, y=60)

        # entry for  the name
        self.namenet = Entry(master, width=60)
        self.namenet.place(x=120, y=60)

        # search button
        self.search = Button(master, text="Search", width=12, height=1, bg='white', command=self.search_db)
        self.search.place(x=120, y=100)
    # function to search
    def search_db(self):
        
        # execute sql 
        try:
            self.input = self.namenet.get()
            sql = "SELECT * FROM Appointment WHERE FullName LIKE ?"
            self.res = c.execute(sql, (self.input,))
            for self.row in self.res:
                self.name1 = self.row[0]
                self.email = self.row[1]
                self.gender = self.row[2]
                self.time = self.row[3]
                self.date = self.row[4]
            print(self.name1)   
        # creating the update form
            self.uname = Label(self.master, text="NAME",  bg='steelblue',font=('arial 14 bold'))
            self.uname.place(x=0, y=140)

            self.uemail = Label(self.master, text="EMAIL", bg='steelblue', font=('arial 14 bold'))
            self.uemail.place(x=0, y=180)

            self.ugender = Label(self.master, text="GENDER",  bg='steelblue',font=('arial 14 bold'))
            self.ugender.place(x=0, y=220)

            self.utime = Label(self.master, text="TIME",  bg='steelblue',font=('arial 14 bold'))
            self.utime.place(x=0, y=260)

            self.udate = Label(self.master, text="DATE", bg='steelblue', font=('arial 14 bold'))
            self.udate.place(x=0, y=300)

            # entries for each labels==========================================================
            # ===================filling the search result in the entry box to update
            self.ent1 = Entry(self.master, width=30)
            self.ent1.place(x=120, y=140)
            self.ent1.insert(END, str(self.name1))

            self.ent2 = Entry(self.master, width=30)
            self.ent2.place(x=120, y=180)
            self.ent2.insert(END, str(self.email))

            self.ent3 = Entry(self.master, width=30)
            self.ent3.place(x=120, y=220)
            self.ent3.insert(END, str(self.gender))

            self.ent4 = Entry(self.master, width=30)
            self.ent4.place(x=120, y=260)
            self.ent4.insert(END, str(self.time))

            self.ent5 = Entry(self.master, width=30)
            self.ent5.place(x=120, y=300)
            self.ent5.insert(END, str(self.date))

            # button to execute update
            self.update = Button(self.master, text="Update", width=20, height=2, bg='lightblue', command=self.update_db)
            self.update.place(x=320, y=340)

            # button to delete
            self.delete = Button(self.master, text="Delete", width=20, height=2, bg='red', command=self.delete_db)
            self.delete.place(x=120, y=340)
            #db_search1(self.res)
        except:
            tkinter.messagebox.showinfo("Error","No Such Appointments")
            sys.exit()        
            
    def update_db(self):
        
        # declaring the variables to update
        self.var1 = self.ent1.get() #updated name
        self.var2 = self.ent2.get() #updated email
        self.var3 = self.ent3.get() #updated gender
        self.var4 = self.ent4.get() #updated time
        self.var5 = self.ent5.get() #updated date

        query = "UPDATE Appointment SET FullName=?, Email=?, Gender=?, Time=?, Date=? WHERE FullName LIKE ?"
        c.execute(query, (self.var1, self.var2, self.var3, self.var4, self.var5, self.namenet.get(),))
        conn.commit()
        tkinter.messagebox.showinfo("Updated", "Successfully Updated.")
        sys.exit()
    def delete_db(self):
        # delete the appointment
        sql2 = "DELETE FROM Appointment WHERE FullName LIKE ?"
        c.execute(sql2, (self.namenet.get(),))
        conn.commit()
        tkinter.messagebox.showinfo("Success", "Deleted Successfully")
        self.ent1.destroy()
        self.ent2.destroy()
        self.ent3.destroy()
        self.ent5.destroy()
        self.ent6.destroy()
        sys.exit()
# creating the object
root = Tk()
b = Application(root)
root.geometry("550x550")
root.title("Hospital Management")
root.configure(background="steelblue")
root.resizable(False, False)
root.mainloop()
