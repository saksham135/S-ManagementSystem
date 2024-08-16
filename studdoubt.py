from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfilename
from tkinter.ttk import Combobox, Treeview
from PIL import Image, ImageTk
import pymysql
from tkcalendar import DateEntry


class doubt():
    def __init__(self,dwindow):
        self.mw = Toplevel(dwindow)
        w = self.mw.winfo_screenwidth()
        h = self.mw.winfo_screenheight()
        w1=600
        h1=400

        self.mw.geometry("%dx%d+%d+%d" % (w,h,450,230))
        self.mw.geometry("600x600")
        self.mw.minsize(600, 400)
        self.mw.maxsize(600, 400)
        self.mw.title("Doubt Page")

        self.bimg1 = Image.open("projectimages//bg2.jpg")
        self.bimg1 = self.bimg1.resize((w, h))

        self.bimg2 = ImageTk.PhotoImage(self.bimg1)
        self.bimglbl = Label(self.mw, image=self.bimg2)
        self.bimglbl.place(x=-2, y=0)

        self.head1 = Label(self.mw, text="Add Doubts", font=('Arial', 31, 'bold'), bg='#d7948c', relief='groove',
                           width=25)

        self.l1 = Label(self.mw, text="Rollno")
        self.l2 = Label(self.mw, text="Name")
        self.l3 = Label(self.mw, text="Subject")
        self.l4 = Label(self.mw, text="Queries")

        self.t1 = Entry(self.mw,width=23)
        self.t2 = Entry(self.mw,width=23)

        self.v2 = StringVar()
        self.c1 = Combobox(self.mw, textvariable=self.v2)
        # self.c1.bind("<<ComboboxSelected>>", lambda e: self.getallQuali())

        self.t3 = Text(self.mw,height=3,width=20)
        self.b1 = Button(self.mw, text="Done!!",command=self.saveData)
        self.b1.config(width=10)




        self.mw.config(bg='#697aa3')

        self.head1.place(x=0, y=2)
        self.l1.place(x=180,y=100)
        self.t1.place(x=240,y=100)

        self.l2.place(x=180, y=140)
        self.t2.place(x=240, y=140)

        self.l3.place(x=180, y=180)

        self.c1.place(x=240, y=180)
        self.l4.place(x=180, y=220)
        self.t3.place(x=240, y=220)



        self.b1.place(x=240,y=280)
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


    def saveData(self):

        self.databaseConnection()
        try:
            myqry = "insert into sdoubt values(%s,%s,%s,%s)"
            rowcount = self.curr.execute(myqry,
                                         (self.t1.get(),self.t2.get(),self.v2.get(),self.t3.get("1.0", END)))
            self.conn.commit()
            if rowcount == 1:
                messagebox.showinfo("Success", "Student Doubts Succesfully Updated", parent=self.mw)
                self.clearPage()
            else:
                messagebox.showwarning("Failure", "Check all Fields Carefully", parent=self.mw)
        except Exception as e:
            messagebox.showerror("Query Error", "Error While Inserting in Database : \n" + str(e), parent=self.mw)

    def clearPage(self):
        self.t1.delete(0, END)
        self.t2.delete(0, END)

        self.t3.delete('1.0', END)
        self.c1.set("Choose Subject")

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


if __name__ == "__main__":
    dummy = Tk()
    doubt(dummy)
    dummy.mainloop()

