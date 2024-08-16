from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox, Treeview
import pymysql
from PIL import Image,ImageTk

class UClass:
    def __init__(self,uwindow):
        self.save = None
        self.window = Toplevel(uwindow)
        self.window.title("Add Student")
        w = self.window.winfo_screenwidth()
        h = self.window.winfo_screenheight()
        # w=self.mw.winfo_screenwidth()
        # h=self.mw.winfo_screenheight()
        # self.mw.geometry("%dx%d+%d+%d"%(w,h,100,100))
        self.window.geometry("%dx%d+%d+%d" % (w - 150, h - 200, 70, 100))
        self.window.geometry("1200x700")
        self.window.minsize(1200, 700)
        self.window.maxsize(1200, 700)

        self.bimg1 = Image.open("projectimages//bg2.jpg")
        self.bimg1 = self.bimg1.resize((w, h))

        self.bimg2 = ImageTk.PhotoImage(self.bimg1)
        self.bimglbl = Label(self.window, image=self.bimg2)
        self.bimglbl.place(x=-2, y=0)
        self.head1 = Label(self.window, text="Add User", font=('Arial', 31, 'bold'), bg='#d7948c', relief='groove',
                           width=50)


        #-------------------------------------------------
        # ---------- Widgets ----------------------------
        mycolor1="white"
        myfont1 = ("Century",10,"bold")

        self.headlbl = Label(self.window,text="User",background="pink",font=("Century",20,"bold"),relief='groove',borderwidth=10)

        # self.window.config(background=mycolor1)
        self.L1 = Label(self.window,text="Username",background=mycolor1,font=myfont1)
        self.L2 = Label(self.window,text="Password",background=mycolor1,font=myfont1)
        self.L3 = Label(self.window,text="Usertype",background=mycolor1,font=myfont1)

        self.t1 = Entry(self.window,font=myfont1 )
        self.t2 = Entry(self.window,font=myfont1,show="*")
        self.v1 = StringVar()
        self.c1 = Combobox(self.window,values=["Admin","Employee","Teacher"], textvariable=self.v1, font=myfont1,width=17)


        # -------- Table ----------------------------------
        self.tablearea = Frame(self.window)
        self.mytable = Treeview(self.tablearea,
                        columns=['c1', 'c2'], height=12)
        self.mytable.heading("c1", text="Username")
        self.mytable.heading("c2", text="Usertype")
        self.mytable['show'] = 'headings'
        self.mytable.column("#1", width=200, anchor='center')
        self.mytable.column("#2", width=200, anchor='center')
        self.mytable.pack()
        self.mytable.bind("<ButtonRelease-1>",lambda e: self.getColumnData())
        #---------- buttons -------------------
        self.b1 = Button(self.window,text="Save",background="pink",command=self.saveData)
        self.b2 = Button(self.window,text="Update",background="pink" ,command=self.updateData)
        self.b3 = Button(self.window,text="Delete",background="pink",command=self.deleteData)
        self.b4 = Button(self.window,text="Fetch",background="pink",command=self.fetchData)
        self.b5 = Button(self.window,text="Search",background="pink",command=self.searchData)
        #-----------placements ----------------------

        self.window.config(bg='#697aa3')

        self.head1.place(x=-10, y=0)
        x1 = 10
        y1 = 100
        x_diff = 100
        y_diff = 50
        self.L1.place(x=x1,y=y1)
        self.t1.place(x=x1+x_diff,y=y1)
        self.b4.place(x=x1+x_diff+x_diff+75,y=y1,width=100,height=30)
        self.tablearea.place(x=x1+x_diff+x_diff+x_diff+100,y=y1)
        y1+=y_diff
        self.L2.place(x=x1,y=y1)
        self.t2.place(x=x1+x_diff,y=y1)
        y1+=y_diff
        self.L3.place(x=x1,y=y1)
        self.c1.place(x=x1+x_diff,y=y1)
        self.b5.place(x=x1+x_diff+x_diff+75,y=y1,width=100,height=30)

        y1+=y_diff
        self.b1.place(x=x1,y=y1,width=100,height=30)
        self.b2.place(x=x1+x_diff,y=y1,width=100,height=30)
        self.b3.place(x=x1+x_diff+x_diff,y=y1,width=100,height=30)

        self.clearPage()
        self.window.mainloop()


    def databaseConnection(self):
        myhost = "localhost"
        mydb = "pythongtbproject"
        myuser="root"
        mypassword=""
        try:
            self.conn = pymysql.connect(host=myhost,db=mydb,user=myuser,password=mypassword)
            self.curr = self.conn.cursor()
        except Exception as e:
            messagebox.showerror("Database Error","Error While connecting database : \n"+str(e),parent=self.window)

    def saveData(self):
        #saving text
        self.databaseConnection()
        try:
            myqry = "insert into user values(%s,%s,%s)"
            rowcount = self.curr.execute(myqry, (self.t1.get(),self.t2.get(),self.v1.get()))
            self.conn.commit()
            if rowcount==1:
                messagebox.showinfo("Success","User Record Saved successfully",parent=self.window)
                self.clearPage()
            else:
                messagebox.showwarning("Failure","Check all fields carefully",parent=self.window)
        except Exception as e:
            messagebox.showerror("Query Error", "Error While insertion : \n" + str(e), parent=self.window)

    def updateData(self):
        self.databaseConnection()
        try:
            myqry = "update user set Password=%s, Usertype=%s where Uname=%s  "
            rowcount = self.curr.execute(myqry, (self.t2.get(),self.v1.get(),self.t1.get()))
            self.conn.commit()
            if rowcount==1:
                messagebox.showinfo("Success","User Record Updated successfully",parent=self.window)
                self.clearPage()
            else:
                messagebox.showwarning("Failure","Check all fields carefully",parent=self.window)
        except Exception as e:
            messagebox.showerror("Query Error", "Error While updation : \n" + str(e), parent=self.window)

    def deleteData(self):
        ans = messagebox.askquestion("Confirmation","Are you sure to delete??",parent=self.window)
        if ans=="yes":
            self.databaseConnection()
            try:
                myqry = "delete from user where Uname=%s"
                rowcount = self.curr.execute(myqry, (self.t1.get()))
                self.conn.commit()
                if rowcount==1:
                    messagebox.showinfo("Success","User Record deleted successfully",parent=self.window)
                    self.clearPage()
                else:
                    messagebox.showwarning("Failure","Check all fields carefully",parent=self.window)
            except Exception as e:
                messagebox.showerror("Query Error", "Error While deletion : \n" + str(e), parent=self.window)

    def getColumnData(self):
        id = self.mytable.focus()
        content = self.mytable.item(id)
        data = content['values']
        col1 =data[0]
        self.fetchData(col1)

    def fetchData(self,col = None):
        if col==None:
            uname = self.t1.get()
        else:
            uname = col
        self.databaseConnection()
        try:
            myqry =  "select * from user where Uname=%s"
            rowcount = self.curr.execute(myqry,(uname))
            data = self.curr.fetchone()
            self.clearPage()
            if data:
                self.t1.insert(0,data[0])
                self.t2.insert(0,data[1])
                self.v1.set(data[2])

                self.b2['state'] = 'normal'
                self.b3['state'] = 'normal'


            else:
                messagebox.showwarning("Empty","No User Found",parent=self.window)
        except Exception as e:
            messagebox.showerror("Query Error", "Error While insertion : \n" + str(e), parent=self.window)

    def clearPage(self):
        self.t1.delete(0,END)
        self.t2.delete(0,END)
        self.v1.set("Choose Usertype")

        self.b2['state']='disabled'
        self.b3['state']='disabled'

    def searchData(self):
        self.databaseConnection()
        try:
            if self.v1.get()=='Choose Usertype':
                utype = ""
            else:
                utype=self.v1.get()
            myqry = "select * from user where Utype like %s"
            rowcount = self.curr.execute(myqry,(utype+"%"))
            data = self.curr.fetchall()
            self.mytable.delete(*self.mytable.get_children())
            if data:
                for row in data:
                    crow = [row[0],row[2]]
                    self.mytable.insert("", END, values=crow)
            else:
                messagebox.showwarning("Empty", "No User Found", parent=self.window)
        except Exception as e:
            messagebox.showerror("Query Error", "Error While insertion : \n" + str(e), parent=self.window)


if __name__ == '__main__':
    dummyHomepage =Tk()
    UClass(dummyHomepage)
    dummyHomepage.mainloop()