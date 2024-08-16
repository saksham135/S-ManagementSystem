from cProfile import label
from cgitb import text
from doctest import master
from msilib.schema import ComboBox

from optparse import Values

from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfilename
from tkinter.ttk import Treeview

import pymysql
from PIL import Image,ImageTk




class Sub:
    def __init__(self,swindow):
        self.save = None
        self.mw = Toplevel(swindow)
        self.mw.title("Add Department")
        w = self.mw.winfo_screenwidth()
        h = self.mw.winfo_screenheight()
        # w=self.mw.winfo_screenwidth()
        # h=self.mw.winfo_screenheight()
        # self.mw.geometry("%dx%d+%d+%d"%(w,h,100,100))
        self.mw.geometry("%dx%d+%d+%d" % (w - 150, h - 200, 70, 100))
        self.mw.geometry("1200x700")
        self.mw.minsize(1200, 700)
        self.mw.maxsize(1200, 700)

        self.bimg1 = Image.open("projectimages//bg2.jpg")
        self.bimg1 = self.bimg1.resize((w, h))

        self.bimg2 = ImageTk.PhotoImage(self.bimg1)
        self.bimglbl = Label(self.mw, image=self.bimg2)
        self.bimglbl.place(x=-2, y=0)

        self.head1 = Label(self.mw, text="Add Subject", font=('Arial', 31, 'bold'), bg='#d7948c', relief='groove',
                           width=50)
        self.l1 = Label(self.mw, text="Subject Name")
        self.t1 = Entry(self.mw)
        self.l2 = Label(self.mw, text="Subject Incharge")
        self.t2 = Entry(self.mw)

        self.b1 = Button(self.mw, text="Save", background='#d7948c', command=self.saveData)
        self.b1.config(width=10)
        self.b2 = Button(self.mw, text="Update", background='#d7948c', command=self.updateData)
        self.b2.config(width=10)
        self.b3 = Button(self.mw, text="Delete", background="#d7948c", command=self.deleteData)
        self.b3.config(width=10)
        self.b4 = Button(self.mw, text="Fetch", background="#d7948c", command=self.fetchData)
        self.b4.config(width=10)
        self.b5 = Button(self.mw, text="Search", background="#d7948c", command=self.searchData)
        self.b5.config(width=10)

        #---------table area------------
        # --------------------Table Area---------------------------
        self.tablearea = Frame(self.mw)
        self.mytable = Treeview(self.tablearea, columns=['c1', 'c2'], height=20)
        self.mytable.heading("c1", text='Subject Name')
        self.mytable.heading('c2', text='Subject Incharge')

        self.mytable['show'] = 'headings'
        self.mytable.column("#1", width=300, anchor='center')
        self.mytable.column("#2", width=300, anchor='center')

        self.mytable.pack()
        self.mytable.bind("<ButtonRelease-1>", lambda e: self.getColumnData())



        self.mw.config(bg='#697aa3')

        self.head1.place(x=-10, y=0)

        self.l1.place(x=100, y=100)
        self.t1.place(x=240, y=100)

        self.l2.place(x=100, y=140)
        self.t2.place(x=240, y=140)
        self.tablearea.place(x=500, y=100)

        self.b1.place(x=100, y=200)
        self.b2.place(x=200, y=200)
        self.b3.place(x=300, y=200)
        self.b4.place(x=380, y=100)
        self.b5.place(x=380, y=140)



        self.mw.mainloop()

    def databaseConnection(self):
        myhost = "localhost"
        mydb = "pythongtbproject"
        myuser = "root"
        mypassword = ""
        try:
            self.conn = pymysql.connect(host=myhost, db=mydb, user=myuser, password=mypassword)
            self.curr = self.conn.cursor()
        except Exception as e:
            messagebox.showerror("Database Error", "Error while connection to Database : \n" + str(e),
                                 parent=self.mw)

    def clearPage(self):
        self.t1.delete(0, END)
        self.t2.delete(0, END)

        self.b2['state'] = 'disabled'
        self.b3['state'] = 'disabled'

    def saveData(self):
        try:
            myqry = "insert into subject values(%s,%s)"
            rowcount = self.curr.execute(myqry,
                                         (self.t1.get(), self.t2.get()))
            self.conn.commit()
            if rowcount == 1:
                messagebox.showinfo("Success", "Subject Record Succesfully Updated", parent=self.mw)
                self.clearPage()
            else:
                messagebox.showwarning("Failure", "Check all Fields Carefully", parent=self.mw)
        except Exception as e:
            messagebox.showerror("Query Error", "Error While Inserting in Database : \n" + str(e), parent=self.mw)

    def updateData(self):
        self.databaseConnection()
        try:
            myqry = "update subject set Sincharge = %s where Sname =%s"
            rowcount = self.curr.execute(myqry,(self.t2.get(),self.t1.get()))
            self.conn.commit()
            if rowcount == 1:
                messagebox.showinfo("Success","Data Updates Successfully",parent=self.mw)
                self.clearPage()
            else:
                messagebox.showerror("Error","Check all Fields Carefully",parent=self.mw)
        except Exception as e:
            messagebox.showerror("Error","Error while updating Record in Database :\n"+str(e),parent=self.mw)


    def deleteData(self):
        ans = messagebox.askquestion("Confirmation", "Are you sure to delete data??", parent=self.mw)
        if ans == "yes":
            self.databaseConnection()
            try:
                myqry = "delete from subject where Sname =%s"
                rowcount = self.curr.execute(myqry,(self.t1.get()))
                self.conn.commit()
                if rowcount == 1:
                    messagebox.showinfo("Success","Data Deleted Successfully",parent=self.mw)
                    self.clearPage()
                else:
                    messagebox.showerror("Error","Check all fields carefully",parent=self.mw)
            except Exception as e:
                messagebox.showerror("Error","Error while deleting data from Database :\n"+str(e))

    def getColumnData(self):
        id = self.mytable.focus()
        content = self.mytable.item(id)
        data = content['values']
        col1 = data[0]
        self.fetchData(col1)

    def fetchData(self,col=None):
        if col == None:
            subn = self.t1.get()
        else:
            subn = col
        self.databaseConnection()
        try:
            myqry = "select * from subject where Sname =%s"
            rowcount = self.curr.execute(myqry,(subn))
            data = self.curr.fetchone()
            self.clearPage()
            if data:
                self.t1.insert(0, data[0])
                self.t2.insert(0, data[1])

                self.b2['state'] = 'normal'
                self.b3['state'] = 'normal'
            else:
                messagebox.showwarning("Empty", "No Department Record Found for this Department", parent=self.mw)
        except Exception as e:
            messagebox.showerror("Query Error", "Error while insertion : \n" + str(e), parent=self.mw)



    def searchData(self):
        self.databaseConnection()
        try:
            myqry = "select * from subject where Sincharge like %s"
            rowcount = self.curr.execute(myqry, (self.t2.get() + "%"))
            data = self.curr.fetchall()
            self.mytable.delete(*self.mytable.get_children())
            if data:
                for row in data:
                    self.mytable.insert("", END, values=row)
            else:
                messagebox.showwarning("Empty", "No Department Found", parent=self.mw)
        except Exception as e:
            messagebox.showerror("Query Error", "Error while Insertion : \n" + str(e), parent=self.mw)


if __name__ == "__main__":
    dummy = Tk()
    Sub(dummy)
    dummy.mainloop()

