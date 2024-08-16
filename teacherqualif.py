from cProfile import label
from cgitb import text
from doctest import master
from tkinter.ttk import Combobox

from optparse import Values

from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfilename
from tkinter.ttk import Treeview
from PIL import Image,ImageTk

import pymysql



class myquali:


    def __init__(self, qwindow) -> None:
        self.save = None
        self.mw = Toplevel(qwindow)
        self.mw.title("Add Teacher Qualification")
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

        self.head1 = Label(self.mw, text="Add Qualification", font=('Arial', 31, 'bold'), bg='#d7948c', relief='groove',
                           width=50)

        self.l1 = Label(self.mw, text="Subject")

        self.l2 = Label(self.mw, text="Qualification")

        self.l3 = Label(self.mw, text="Time Period")

        self.l4 = Label(self.mw, text="Charges")


        self.v1 = StringVar()
        self.c1 = Combobox(self.mw,values=('Maths', 'Science','Hindi','Punjabi'),textvariable=self.v1)
        self.t2 = Entry(self.mw)
        self.t3 = Entry(self.mw)
        self.t4 = Entry(self.mw)

        self.b1 = Button(self.mw, text="Save", background='#d7948c', command=self.saveData)
        self.b1.config(width=10)
        self.b2 = Button(self.mw, text="Update", background='#d7948c', command=self.updatePage)
        self.b2.config(width=10)
        self.b3 = Button(self.mw, text="Delete", background="#d7948c", command=self.deleteData)
        self.b3.config(width=10)
        self.b4 = Button(self.mw, text="Fetch", background="#d7948c", command=self.fetchData)
        self.b4.config(width=10)
        self.b5 = Button(self.mw, text="Search", background="#d7948c", command=self.searchData)
        self.b5.config(width=10)


        #------------------------Table-----------------
        self.tablearea = Frame(self.mw)
        self.mytable = Treeview(self.tablearea, columns=['c1', 'c2','c3','c4'], height=12)
        self.mytable.heading("c1", text='Subject')
        self.mytable.heading('c2', text='Qualification')
        self.mytable.heading("c3", text='Time Period')
        self.mytable.heading('c4', text='Charges')

        self.mytable['show'] = 'headings'
        self.mytable.column("#1", width=180, anchor='center')
        self.mytable.column("#2", width=180, anchor='center')
        self.mytable.column("#3", width=180, anchor='center')
        self.mytable.column("#4", width=180, anchor='center')
        self.mytable.bind("<ButtonRelease-1>", lambda e: self.getColumnData())

        self.mytable.pack()




        self.mw.config(bg='#697aa3')
        self.head1.place(x=-10, y=0)

        self.tablearea.place(x=420, y=100)

        self.l1.place(x=20,y=100)
        self.c1.place(x=120,y=100,width=130)

        self.l2.place(x=20,y=140)
        self.t2.place(x=120,y=140,width=130)

        self.l3.place(x=20, y=180)
        self.t3.place(x=120, y=180, width=130)

        self.l4.place(x=20, y=220)
        self.t4.place(x=120, y=220, width=130)


        self.b1.place(x=20, y=260)
        self.b2.place(x=120, y=260)
        self.b3.place(x=220, y=260)
        self.b4.place(x=280, y=140)
        self.b5.place(x=280, y=100)

        self.clearPage()
        self.getAllDepartments()

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
        self.v1.set(None)
        self.c1.set("Choose Subject")
        self.t2.delete(0, END)
        self.t3.delete(0,END)
        self.t4.delete(0,END)

        self.b2['state'] = 'disabled'
        self.b3['state'] = 'disabled'

    def saveData(self):
        self.databaseConnection()
        try:
            myqry = "insert into tquali values(%s,%s,%s,%s)"
            rowcount = self.curr.execute(myqry,(self.v1.get(), self.t2.get(),self.t3.get(),self.t4.get()))
            self.conn.commit()
            if rowcount == 1:
                messagebox.showinfo("Success", "Qualification Record Succesfully Updated", parent=self.mw)
                self.clearPage()
            else:
                messagebox.showwarning("Failure", "Check all Fields Carefully", parent=self.mw)
        except Exception as e:
            messagebox.showerror("Query Error", "Error While Inserting in Database : \n" + str(e), parent=self.mw)

    def updatePage(self):
        self.databaseConnection()
        try:
            myqry = "update tquali set Sname = %s,Tperiod = %s , Charges=%s where Qualification= %s"
            rowcount = self.curr.execute(myqry, (self.v1.get(),self.t3.get(),self.t4.get(),self.t2.get()))
            self.conn.commit()
            if rowcount == 1:
                messagebox.showinfo("Sucess", "Qualification Record Updated in DataBase Successfully", parent=self.mw)
                self.clearPage()
            else:
                messagebox.showerror("Failure", "Check all Fields Carefully",parent=self.mw)
        except Exception as e:
            messagebox.showerror("Failure", "Error while updating in DataBase :\n " + str(e), parent=self.mw)

    def deleteData(self):
        ans = messagebox.askquestion("Confirmation", "Are you sure to delete data??", parent=self.mw)
        if ans == "yes":
            self.databaseConnection()
            try:
                myqry = " delete from tquali where Qualification=%s"
                rowcount = self.curr.execute(myqry, (self.t2.get()))
                self.conn.commit()
                if rowcount == 1:
                    messagebox.showinfo("Success", "Qualification Record Deleted Successfully", parent=self.mw)
                    self.clearPage()
                else:
                    messagebox.showwarning("Failure", "Check all Fields Carefully", parent=self.mw)
            except Exception as e:
                messagebox.showerror("Failure", "Error While Deleting Data from DataBase :\n " + str(e), parent=self.mw)

    def getColumnData(self):
        id = self.mytable.focus()
        content = self.mytable.item(id)
        data = content['values']
        col1 = data[1]
        self.fetchData(col1)


    def fetchData(self, col=None):
        if col == None:
            quali = self.t2.get()
        else:
            quali = col
        self.databaseConnection()
        try:
            myqry = "select * from tquali  where Qualification=%s"
            rowcount = self.curr.execute(myqry, (quali))
            data = self.curr.fetchone()
            self.clearPage()
            if data:
                self.v1.set(data[0])
                self.t2.insert(0, data[1])
                self.t3.insert(0, data[2])
                self.t4.insert(0, data[3])


                self.b2['state'] = 'normal'
                self.b3['state'] = 'normal'

            else:
                messagebox.showwarning("Empty", "No Qualification Record Found for this Course", parent=self.mw)

        except Exception as e:
            messagebox.showerror("Query Error", "Error while insertion : \n" + str(e), parent=self.mw)

    def searchData(self):
        self.databaseConnection()
        try:
            if self.v1.get()=='Choose Subject':
                sub = ""
            else:
                sub=self.v1.get()
            myqry = "select * from tquali where Sname like %s"
            rowcount = self.curr.execute(myqry,(sub+"%"))
            data = self.curr.fetchall()
            self.mytable.delete(*self.mytable.get_children())
            if data:
                for row in data:
                    self.mytable.insert("", END, values=row)
            else:
                messagebox.showwarning("Empty", "No Subject Found", parent=self.mw)
        except Exception as e:
            messagebox.showerror("Query Error", "Error while Insertion : \n" + str(e), parent=self.mw)

    def getAllDepartments(self):
        self.databaseConnection()
        try:
            myqry = "select * from subject "
            rowcount = self.curr.execute(myqry)
            data = self.curr.fetchall()
            # self.mytable.delete(*self.mytable.get_children())
            mycombobox1=[]
            if data:
                self.v1.set("Choose Subject")
                for row in data:
                    mycombobox1.append(row[0])
            else:
                self.v1.set("No Subject")

            self.c1.config(values=mycombobox1)
        except Exception as e:
            messagebox.showerror("Query Error", "Error while Insertion : \n" + str(e), parent=self.mw)



if __name__ == "__main__":
    dummy = Tk()
    myquali(dummy)
    dummy.mainloop()

