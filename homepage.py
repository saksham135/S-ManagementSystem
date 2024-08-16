from doctest import master
from logging import root
from tkinter import *
from tkinter import messagebox

from PIL import Image, ImageTk

from studentfilemenu import stud
from reportstud import Report1Class
from Department import Dept
from Courses import Cour
from Reports2 import Report2Class
from teacherfilemenu import teach
from mysubjcts import Sub
from teacherqualif import myquali
from admincreation import cadmin
from manageuser import UClass
from reportteach import Report3Class
from reportteach2 import Report4Class
from changepassword import ppage
from studdoubt import doubt
from dreports import Report7Class



class homepg:
    def __init__(self,uname,utype) -> None:
        self.uname = uname
        self.utype = utype
        self.mw = Tk()
        w =self.mw.winfo_screenwidth()
        h = self.mw.winfo_screenheight()

        # w=self.mw.winfo_screenwidth()
        # h=self.mw.winfo_screenheight()
        # self.mw.geometry("%dx%d+%d+%d"%(w,h,100,100))
        self.mw.geometry("%dx%d+%d+%d" % (w - 150, h - 200, 70, 100))
        self.mw.geometry("1400x700")
        self.mw.minsize(1400, 700)
        self.mw.maxsize(1400, 700)
        # self.mw.state("zoomed")

        self.bimg1 = Image.open("projectimages//cg.jpg")
        self.bimg1 = self.bimg1.resize((w,h))

        self.bimg2 = ImageTk.PhotoImage(self.bimg1)
        self.bimglbl = Label(self.mw, image=self.bimg2)
        self.bimglbl.place(x=-2, y=0)
        self.mw.title("S++ College Management")
        
        
        #adding menus
        self.mw.option_add("*TearOff", False)
        self.my_menu=Menu(self.mw)
        self.mw.config(menu=self.my_menu)

        #adding file menu
        self.file_menu=Menu(self.my_menu)
        self.my_menu.add_cascade(label="Manage",menu=self.file_menu)
        self.file_menu.add_command(label="Student....",command=lambda : stud(self.mw))
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Teacher....",command=lambda : teach(self.mw))

        self.file_menu1=Menu(self.my_menu)
        self.my_menu.add_cascade(label="Student Reports",menu=self.file_menu1)
        self.file_menu1.add_command(label="Reports....", command=lambda: Report1Class(self.mw))
        self.file_menu1.add_command(label="Student Department Reports....", command=lambda: Report2Class(self.mw))



        self.file_menu2 = Menu(self.my_menu)
        self.my_menu.add_cascade(label="Manage  Student Departments and Courses", menu=self.file_menu2)
        self.file_menu2.add_command(label="Departments....", command=lambda: Dept(self.mw))
        self.file_menu2.add_command(label="Courses....", command=lambda: Cour(self.mw))

        self.file_menu3 = Menu(self.my_menu)
        self.my_menu.add_cascade(label="Manage Teacher's Subject and Qualification", menu=self.file_menu3)
        self.file_menu3.add_command(label="Subjects....", command=lambda: Sub(self.mw))
        self.file_menu3.add_command(label="Qualification....", command=lambda: myquali(self.mw))

        self.file_menu4 = Menu(self.my_menu)
        self.my_menu.add_cascade(label=" Manage Account", menu=self.file_menu4)

        self.icon1_bimg1 = Image.open("projectimages//login2.png")
        self.icon1_bimg1 = self.icon1_bimg1.resize((30, 30))
        self.icon1_bimg2 = ImageTk.PhotoImage(self.icon1_bimg1)
        self.file_menu4.add_command(label="Manage User", command=lambda: UClass(self.mw),
                               image=self.icon1_bimg2, compound=LEFT)

        self.file_menu4.add_command(label="ChangePassword", command=lambda: ppage(self.mw, self.uname),
                               image=self.icon1_bimg2, compound=LEFT)
        self.file_menu4.add_command(label="Logout", command=lambda: self.quitter(),
                               image=self.icon1_bimg2, compound=LEFT)

        self.file_menu5 = Menu(self.my_menu)
        self.my_menu.add_cascade(label="Teacher Reports", menu=self.file_menu5)
        self.file_menu5.add_command(label="Teacher Reports....", command=lambda: Report3Class(self.mw))
        self.file_menu5.add_command(label="Teacher Subject Reports....", command=lambda: Report4Class(self.mw))

        self.file_menu6 = Menu(self.my_menu)
        self.my_menu.add_cascade(label="Student Help", menu=self.file_menu6)
        self.file_menu6.add_command(label="Add Your Lesson Doubts....", command=lambda: doubt(self.mw))
        self.file_menu6.add_command(label="Doubts Reports....", command=lambda: Report7Class(self.mw))


        if utype == "Employee":
            self.my_menu.entryconfig(0, state='disable')
            # self.my_menu.delete(2)
            self.my_menu.entryconfig(1, state="disable")

            self.my_menu.entryconfig(3, state='disable')

            self.my_menu.entryconfig(2, state='disable')
            self.my_menu.entryconfig(3, state='disable')
            self.my_menu.entryconfig(4, state='disable')
            self.my_menu.entryconfig(5, state='disable')

        if utype == "Teacher":
            self.my_menu.entryconfig(0,state='disable')
            self.my_menu.entryconfig(5, state='disable')
            self.my_menu.entryconfig(3, state='disable')





        self.mw.mainloop()

    def quitter(self):
        ans = messagebox.askquestion("Confirmation", "Are you sure to Logout??", parent=self.mw)
        if ans == "yes":
            self.mw.destroy()
            from loginpage import lpage
            lpage()



        

if __name__ == '__main__':
    homepg("Saksham","Admin")
