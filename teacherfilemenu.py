import time
from cProfile import label
from cgitb import text
from doctest import master
from msilib.schema import ComboBox

from optparse import Values

from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfilename
from tkinter.ttk import Combobox, Treeview
from PIL import Image, ImageTk
import pymysql
from tkcalendar import DateEntry


class teach:
    default_img_name = "default_user.png"

    def __init__(self, twindow) -> None:
        # importing file
        # self.sw=pwindow
        # self.sw=Tk()

        self.save = None
        self.mw = Toplevel(twindow)
        self.mw.title("Add Teacher")
        w = self.mw.winfo_screenwidth()
        h = self.mw.winfo_screenheight()
        # w=self.mw.winfo_screenwidth()
        # h=self.mw.winfo_screenheight()
        # self.mw.geometry("%dx%d+%d+%d"%(w,h,100,100))
        self.mw.geometry("%dx%d+%d+%d" % (w - 150, h - 200, 70, 100))
        self.mw.geometry("1200x700")
        self.mw.minsize(1200, 700)
        self.mw.maxsize(1200, 700)



        self.bimg1 = Image.open("projectimages//tpage.jpg")
        self.bimg1 = self.bimg1.resize((w, h))

        self.bimg2 = ImageTk.PhotoImage(self.bimg1)
        self.bimglbl = Label(self.mw, image=self.bimg2)
        self.bimglbl.place(x=-2, y=0)

        self.head1 = Label(self.mw, text="Add Teacher", font=('Arial', 31, 'bold'), bg='#d7948c', relief='groove',
                           width=50)

        # creating labels
        self.l1 = Label(self.mw, text="Teacher-Id")
        self.t1 = Entry(self.mw)

        self.l2 = Label(self.mw, text="Name")
        self.t2 = Entry(self.mw)

        self.l3 = Label(self.mw, text="Phone")
        self.t3 = Entry(self.mw)

        self.v1 = StringVar()
        self.l4 = Label(self.mw, text="Gender")
        self.r1 = Radiobutton(self.mw, text="Male", value='male', variable=self.v1)
        self.r2 = Radiobutton(self.mw, text="Female", value='female', variable=self.v1)

        self.l5 = Label(self.mw, text="DOB")
        self.t5 = DateEntry(self.mw,width=16,background='darkblue',
                            foreground='white',borderwidth=2,year=2010,date_pattern="yy-mm-dd")

        self.l6 = Label(self.mw, text='Address')
        self.t6 = Text(self.mw, width=15, height=3)

        # self.courselist=['Cse','Ece','EE']
        self.v2 = StringVar()
        self.l7 = Label(self.mw, text="Subject")
        # self.c1 = ttk.Combobox(self.mw,values=self.courselist,textvariable=self.v2,state='readonly')
        # self.c1.set("choose your course")
        self.c1 = Combobox(self.mw,textvariable=self.v2)
        self.c1.bind("<<ComboboxSelected>>",lambda e : self.getallQuali())

        self.v3 = StringVar()
        self.l8 = Label(self.mw, text="Qualification")
        self.c2 = Combobox(self.mw,textvariable=self.v3)

        # adding buttons
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
        self.b6 = Button(self.mw, text="Upload", background="#d7948c", command=self.selectImage)
        self.b6.config(width=17)
        self.imglbl = Label(self.mw, relief="groove", borderwidth=2)

        # --------------------Tables -------------------
        self.tablearea = Frame(self.mw)
        self.mytable = Treeview(self.tablearea, columns=['c1', 'c2', 'c3', 'c4', 'c5', 'c6', 'c7', 'c8'], height=20)
        self.mytable.heading("c1", text='Teacher-Id')
        self.mytable.heading('c2', text='Name')
        self.mytable.heading('c3', text='Phone')
        self.mytable.heading('c4', text='Gender')
        self.mytable.heading('c5', text='DOB')
        self.mytable.heading('c6', text='Address')
        self.mytable.heading('c7', text='Subjects')
        self.mytable.heading('c8', text='Qualification')
        self.mytable['show'] = 'headings'
        self.mytable.column("#1", width=50, anchor='center')
        self.mytable.column("#2", width=100, anchor='center')
        self.mytable.column("#3", width=100, anchor='center')
        self.mytable.column("#4", width=70, anchor='center')
        self.mytable.column("#5", width=80, anchor='center')
        self.mytable.column("#6", width=200, anchor='center')
        self.mytable.column("#7", width=80, anchor='center')
        self.mytable.column("#8", width=80, anchor='center')
        self.mytable.pack()
        self.mytable.bind("<ButtonRelease-1>", lambda e: self.getColumnData())

        # changing size and title
        # self.mw.geometry("800x500")
        # self.mw.minsize(800,500)
        # self.mw.maxsize(800,500)
        # self.mw.title('Add Student')

        self.mw.config(bg='#697aa3')

        self.head1.place(x=-10, y=0)

        # placing labels and widgets
        self.l1.place(x=100, y=100)
        self.t1.place(x=180, y=100)

        self.l2.place(x=100, y=140)
        self.t2.place(x=180, y=140)

        self.l3.place(x=100, y=180)
        self.t3.place(x=180, y=180)

        self.l4.place(x=100, y=220)
        self.r1.place(x=180, y=220)
        self.r2.place(x=240, y=220)

        self.tablearea.place(x=400, y=100)

        self.l5.place(x=100, y=260)
        self.t5.place(x=180, y=260)

        self.l6.place(x=100, y=300)
        self.t6.place(x=180, y=300)

        self.l7.place(x=100, y=380)
        self.c1.place(x=180, y=380)

        self.l8.place(x=100, y=420)
        self.c2.place(x=180, y=420)

        self.b1.place(x=100, y=480)
        self.b2.place(x=180, y=480)
        self.b3.place(x=260, y=480)
        self.b4.place(x=310, y=100)
        self.b5.place(x=310, y=140)

        self.imglbl.place(x=400, y=535,height=130,width=130)
        self.b6.place(x=400, y=670)
        self.clearPage()
        self.getallsubjects()

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

    def selectImage(self):
        self.filename = askopenfilename(file=[("All Pictures", "*.jpg;*.png;*.jpeg"),
                                              ("PNG Images", "*.png"), ("JPG images", "*.jpg;")])
        print("filename = ", self.filename)
        if self.filename != "":
            # open and resizing image
            self.img1 = Image.open(self.filename)
            self.img1 = self.img1.resize((130,130))

            # making it photoimage , so we can put it in label
            self.img2 = ImageTk.PhotoImage(self.img1)
            self.imglbl.config(image=self.img2)

            # getting filename from path
            path = self.filename.split("/")
            # print("Path = ",path)
            name = path[-1]
            # print("name = ",name)
            uniqness = str(int(time.time()))
            # print("uniqness = ",uniqness)
            self.actualname = uniqness + name
            # print("actual name = ",self.actualname)

    def saveData(self):
        if self.actualname == self.default_img_name:
            pass
        else:
            self.img1.save("student_img//" + self.actualname)
        self.databaseConnection()
        try:
            myqry = "insert into teacher values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            rowcount = self.curr.execute(myqry,
                                         (self.t1.get(), self.t2.get(), self.t3.get(), self.v1.get(),
                                          self.t5.get(), self.t6.get("1.0", END), self.v2.get(), self.v3.get(),self.actualname))
            self.conn.commit()
            if rowcount == 1:
                messagebox.showinfo("Success", "Teacher Record Succesfully Updated", parent=self.mw)
                self.clearPage()
            else:
                messagebox.showwarning("Failure", "Check all Fields Carefully", parent=self.mw)
        except Exception as e:
            messagebox.showerror("Query Error", "Error While Inserting in Database : \n" + str(e), parent=self.mw)

    def fetchData(self, col=None):
        if col == None:
            TeacherId = self.t1.get()
        else:
            TeacherId = col
        self.databaseConnection()
        try:
            myqry = "select * from teacher where TeacherId=%s"
            rowcount = self.curr.execute(myqry, (TeacherId))
            data = self.curr.fetchone()
            self.clearPage()
            if data:
                self.t1.insert(0, data[0])
                self.t2.insert(0, data[1])
                self.t3.insert(0, data[2])
                self.v1.set(data[3])
                self.t5.set_date(data[4])
                self.t6.insert('1.0', data[5])
                self.v2.set(data[6])
                self.v3.set(data[7])
                self.actualname=data[8]
                self.oldname=data[8]
                self.b2['state'] = 'normal'
                self.b3['state'] = 'normal'

                self.img1= Image.open("teacher_img//" + self.actualname)
                self.img1 = self.img1.resize((130,130))
                self.img2 = ImageTk.PhotoImage(self.img1)
                self.imglbl.config(image=self.img2)



            else:
                messagebox.showwarning("Empty", "No Teacher  Found for this Teacherid", parent=self.mw)
        except Exception as e:
            messagebox.showerror("Query Error", "Error while insertion : \n" + str(e), parent=self.mw)

    def clearPage(self):
        self.t1.delete(0, END)
        self.t2.delete(0, END)
        self.t3.delete(0, END)
        self.v1.set(None)
        self.t5.delete(0, END)
        self.t6.delete('1.0', END)
        self.c1.set("Choose Subject")
        self.c2.set("Choose Qualification")
        self.b2['state'] = 'disabled'
        self.b3['state'] = 'disabled'
        self.actualname = self.default_img_name
        self.img1 = Image.open("teacher_img//" + self.actualname)
        self.img1 = self.img1.resize((130, 130))

        # making it photoimage , so we can put it in label
        self.img2 = ImageTk.PhotoImage(self.img1)
        self.imglbl.config(image=self.img2)

    def updatePage(self):

        if self.actualname == self.oldname:
            pass
        else:
            self.img1.save("teacher_img//"+self.actualname)
            if self.oldname==self.default_img_name:
                pass
            else:
                import os
                os.remove("teacher_img//"+self.oldname)

        self.databaseConnection()
        try:
            myqry = "update teacher set Name = %s,Phone = %s,Gender = %s," \
                    "DOB = %s, Address = %s,Subject = %s,Qualification = %s,Pic = %s where TeacherId=%s"
            rowcount = self.curr.execute(myqry, (self.t2.get(), self.t3.get(), self.v1.get(), self.t5.get_date(),
                                                 self.t6.get("1.0", END), self.v2.get(), self.v3.get(), self.actualname,
                                                 self.t1.get()))
            self.conn.commit()

            self.conn.commit()
            if rowcount == 1:
                messagebox.showinfo("Sucess", "Data Updated in DataBase Successfully", parent=self.mw)
                self.clearPage()
            else:
                messagebox.showerror("Failure", "Check all Fields Carefully")
        except Exception as e:
            messagebox.showerror("Failure", "Error while updating in DataBase :\n " + str(e), parent=self.mw)

    def getColumnData(self):
        id = self.mytable.focus()
        content = self.mytable.item(id)
        data = content['values']
        col1 = data[0]
        self.fetchData(col1)

    def deleteData(self):
        ans = messagebox.askquestion("Confirmation", "Are you sure to delete data??", parent=self.mw)
        if ans == "yes":

            if self.oldname==self.default_img_name:
                pass
            else:
                import os
                os.remove("teacher_img//"+self.oldname)

            self.databaseConnection()
            try:
                myqry = " delete from teacher where TeacherId=%s"
                rowcount = self.curr.execute(myqry, (self.t1.get()))
                self.conn.commit()
                if rowcount == 1:
                    messagebox.showinfo("Success", "Teacher Data Deleted Successfully", parent=self.mw)
                    self.clearPage()
                else:
                    messagebox.showwarning("Failure", "Check all Fields Carefully", parent=self.mw)
            except Exception as e:
                messagebox.showerror("Failure", "Error While Deleting Data from DataBase :\n " + str(e), parent=self.mw)

    def searchData(self):
        self.databaseConnection()
        try:
            myqry = "select * from teacher where Name like %s"
            rowcount = self.curr.execute(myqry, (self.t2.get() + "%"))
            data = self.curr.fetchall()
            self.mytable.delete(*self.mytable.get_children())
            if data:
                for row in data:
                    self.mytable.insert("", END, values=row)
            else:
                messagebox.showwarning("Empty", "No Teacher Found", parent=self.mw)
        except Exception as e:
            messagebox.showerror("Query Error", "Error while Insertion : \n" + str(e), parent=self.mw)

    def getallsubjects(self):
        self.databaseConnection()
        try:
            myqry = "select * from subject "
            rowcount = self.curr.execute(myqry)
            data = self.curr.fetchall()
            # self.mytable.delete(*self.mytable.get_children())
            mycombobox1 = []
            if data:
                self.v2.set("Choose Subject")
                for row in data:
                    mycombobox1.append(row[0])
            else:
                self.v2.set("No Subject")

            self.c1.config(values=mycombobox1)
        except Exception as e:
            messagebox.showerror("Query Error", "Error while Insertion : \n" + str(e), parent=self.mw)

    def getallQuali(self):
        self.databaseConnection()
        try:
            myqry = "select *  from tquali where Sname=%s "
            rowcount = self.curr.execute(myqry,(self.v2.get()))
            data = self.curr.fetchall()
            # self.mytable.delete(*self.mytable.get_children())
            mycombobox1 = []
            if data:
                self.v3.set("Choose Qualfication")
                for row in data:
                    mycombobox1.append(row[1])
            else:
                self.v3.set("No Qualification")

            self.c2.config(values=mycombobox1)
        except Exception as e:
            messagebox.showerror("Query Error", "Error while Insertion : \n" + str(e), parent=self.mw)




if __name__ == "__main__":
    dummy = Tk()
    teach(dummy)
    dummy.mainloop()
