from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox

import pymysql
from PIL import Image, ImageTk



class ppage():
    def __init__(self,pwindow,uname):
        self.uname=uname
        self.mw=Toplevel(pwindow)
        # self.mw=Tk()
        w = self.mw.winfo_screenwidth()
        h = self.mw.winfo_screenheight()
        w1=600
        h1=400

        self.mw.geometry("%dx%d+%d+%d" % (w,h,450,230))
        self.mw.geometry("600x600")
        self.mw.minsize(600, 400)
        self.mw.maxsize(600, 400)
        self.mw.title("Change Password")

        #adiing image in bg

        self.bimg1 = Image.open("projectimages//loginimage.jpg")
        self.bimg1 = self.bimg1.resize((w1, h1))

        self.bimg2 = ImageTk.PhotoImage(self.bimg1)
        self.bimglbl = Label(self.mw, image=self.bimg2)
        self.bimglbl.place(x=-2, y=0)

        self.head1 = Label(self.mw, text="Change Password", font=('Arial', 31, 'bold'), bg='#d7948c', relief='groove',
                           width=25)

        self.l1 = Label(self.mw, text="Current Password")
        self.l2 = Label(self.mw, text="New Password")
        self.l3 = Label(self.mw, text="Confirm Password")


        self.t1 = Entry(self.mw,show="*")
        self.t2 = Entry(self.mw, show='*')
        self.t3 = Entry(self.mw, show='*')

        self.b1 = Button(self.mw, text="Login In!!",command=self.updateData)
        self.b1.config(width=10)










        self.head1.place(x=0, y=2)
        self.l1.place(x=200, y=100)
        self.t1.place(x=320, y=100)
        self.l2.place(x=200, y=140)
        self.t2.place(x=320, y=140)
        self.l3.place(x=200, y=180)
        self.t3.place(x=320, y=180)
        self.b1.place(x=260, y=300)




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

    def updateData(self):
        if self.t2.get()==self.t3.get():
            self.databaseConnection()
            try:
                myqry = "update user set Password =%s where Uname=%s and Password=%s"
                rowcount = self.curr.execute(myqry,(self.t2.get(),self.uname,self.t1.get()))
                self.conn.commit()
                if rowcount ==1:
                    messagebox.showinfo("Success","Changed Password Sucessfully",parent=self.mw)
                    self.clearPage()
                else:
                    messagebox.showwarning("Error","Current Password doesn't match",parent=self.mw)
            except Exception as e:
                messagebox.showerror("Error","Error While updation :\n"+str(e),parent=self.mw)

        else:
            messagebox.showwarning("Failure", "Confirm Passwords carefully", parent=self.mw)







    def clearPage(self):
        self.t1.delete(0, END)
        self.t2.delete(0, END)
        self.t3.delete(0, END)















