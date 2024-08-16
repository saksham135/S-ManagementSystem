from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox

import pymysql
from PIL import Image, ImageTk



class lpage():
    def __init__(self):
        self.mw=Tk()
        w = self.mw.winfo_screenwidth()
        h = self.mw.winfo_screenheight()
        w1=600
        h1=400

        self.mw.geometry("%dx%d+%d+%d" % (w,h,450,230))
        self.mw.geometry("600x600")
        self.mw.minsize(600, 400)
        self.mw.maxsize(600, 400)
        self.mw.title("Login Page")

        #adiing image in bg

        self.bimg1 = Image.open("projectimages//loginimage.jpg")
        self.bimg1 = self.bimg1.resize((w1, h1))

        self.bimg2 = ImageTk.PhotoImage(self.bimg1)
        self.bimglbl = Label(self.mw, image=self.bimg2)
        self.bimglbl.place(x=-2, y=0)

        self.head1 = Label(self.mw, text="Welcome to S++", font=('Arial', 31, 'bold'), bg='#d7948c', relief='groove',
                           width=25)

        self.l1 = Label(self.mw, text="UserName")
        self.l2 = Label(self.mw, text="Password")

        self.t1 = Entry(self.mw)
        self.t2 = Entry(self.mw, show='*')

        self.b1 = Button(self.mw, text="Login In!!",command=self.CheckData)
        self.b1.config(width=10)










        self.head1.place(x=0, y=2)
        self.l1.place(x=200, y=100)
        self.t1.place(x=280, y=100)
        self.l2.place(x=200, y=140)
        self.t2.place(x=280, y=140)
        self.b1.place(x=260, y=220)




        self.mw.mainloop()

    def databaseConnection(self):
        myhost ="localhost"
        mydb = "pythongtbproject"
        myuser = "root"
        mypassword = ""
        try :
            self.conn = pymysql.connect(host=myhost,db=mydb,user=myuser,password=mypassword)
            self.curr = self.conn.cursor()
        except Exception as e:
            messagebox.showerror("Error","Error While Connecting to Database :\n"+str(e),parent=self.mw)

    def CheckData(self):
        self.databaseConnection()
        try:
            myqry = "select * from user where Uname=%s and Password=%s"
            rowcount = self.curr.execute(myqry,(self.t1.get(),self.t2.get()))
            data=self.curr.fetchone()
            if data:
                uname=data[0]
                utype=data[2]
                messagebox.showinfo("Success", "Welcome" + utype, parent=self.mw)
                self.mw.destroy()
                from homepage import homepg
                homepg(uname, utype)
            else:
                messagebox.showwarning("Failure", "Wrong username or password", parent=self.mw)
        except Exception as e:
            messagebox.showerror("Query Error", "Error While insertion : \n" + str(e), parent=self.mw)

    def clearPage(self):
        self.t1.delete(0, END)
        self.t2.delete(0, END)














if __name__ == "__main__":
    lpage()