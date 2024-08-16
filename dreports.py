from cProfile import label
from cgitb import text
from doctest import master
from msilib.schema import ComboBox

from optparse import Values

from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox, Treeview
import pymysql
from PIL import Image,ImageTk

from PrintingPage import my_cust_PDF




class Report7Class:
    def __init__(self, sdwindow) -> None:
        # importing file
        # self.sw=pwindow
        # self.sw=Tk()


        self.mw = Toplevel(sdwindow)
        self.mw.title("Student Reports")
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

        self.head1 = Label(self.mw, text="Student Doubt's Reports", font=('Arial', 31, 'bold'), bg='#d7948c', relief='groove',
                           width=50)

        self.v1=StringVar()
        self.c1=Combobox(self.mw,textvariable=self.v1)
        self.c1.bind("<<ComboboxSelected>>",lambda e :self.fetchalldata())


        self.mw.config(bg='#697aa3')

        #-------------------Table----------------------
        self.tablearea = Frame(self.mw)
        self.mytable = Treeview(self.tablearea,columns=['c1','c2','c3','c4'],height=20)
        self.mytable.heading("c1",text='RollNo')
        self.mytable.heading('c2',text='Name')
        self.mytable.heading('c3', text='Subject')
        self.mytable.heading('c4', text='Queries')

        self.mytable['show']='headings'
        self.mytable.column("#1",width=200,anchor='center')
        self.mytable.column("#2", width=200, anchor='center')
        self.mytable.column("#3", width=200, anchor='center')
        self.mytable.column("#4", width=400, anchor='center')

        self.mytable.pack()

        self.head1.place(x=-10, y=0)
        self.tablearea.place(x=70,y=150)
        self.c1.place(x=70,y=90)

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



    def fetchalldata(self):
        self.databaseConnection()
        try:
            self.mytable.delete(*self.mytable.get_children())
            myqry = "select * from sdoubt where Sname =%s"
            rowcount = self.curr.execute(myqry,(self.v1.get()))
            data = self.curr.fetchall()
            if data:
                for row in data:
                    self.mytable.insert("",END,values=row)
            else:
                messagebox.showwarning("Empty", "No student Found ", parent=self.mw)
        except Exception as e:
            messagebox.showerror("Query Error", "Error While insertion : \n" + str(e), parent=self.mw)


    def getAllDepartments(self):
        self.databaseConnection()
        try:
            myqry= "select * from tquali"
            rowcount= self.curr.execute(myqry)
            data = self.curr.fetchall()
            mycombobox1=[]
            if data:
                self.v1.set("Choose Subject")
                for row in data:
                    mycombobox1.append(row[0])
            else:
                self.v1.set("No Subject")

            self.c1.config(values=mycombobox1)
        except Exception as e:
            messagebox.showerror("Query Error","Error while fecthing data from Database: \n"+str(e),parent=self.mw)


















if __name__ == "__main__":
    dummy = Tk()
    Report7Class(dummy)
    dummy.mainloop()

