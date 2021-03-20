from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
root = Tk()
root.mainloop()
class login_system:

    def __init__(self,root):
        self.root=root
        self.root.title("Admin Login")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="white")



        #for image
        self.bg_icon=ImageTk.PhotoImage(Image.open("background.jpg.png"))

        #variables::::::
        self.yourname=StringVar()
        self.your_password=StringVar()

        title=Label(self.root,text="Admin Login",font=("times new roman",40,"bold"),bd=10,relief=GROOVE,bg="yellow",fg="red")
        title.place(x=0,y=0,relwidth=1)




        login_frame=Frame(self.root,bg="orange")
        login_frame.place(x=550,y=150)


        logo=Label(login_frame,image=self.bg_icon).grid(row=0,columnspan=2,pady=20)



        lbluser=Label(login_frame,text="Admin Name",compound=LEFT,font=("times new roman", 20,"bold"),bg="yellow",fg="red").grid(row=1,column=0,padx=20,pady=10)
        txtuser=Entry(login_frame,bd=5,textvariable=self.yourname, relief=GROOVE,font=("",15)).grid(row=1,column=1,padx=10)


        lbluser=Label(login_frame,text="Password",compound=LEFT,font=("times new roman", 20,"bold"),bg="yellow",fg="red").grid(row=2,column=0,padx=20,pady=10)
        txtpass=Entry(login_frame,bd=5,textvariable=self.your_password, relief=GROOVE,show="*",font=("",15)).grid(row=2,column=1,padx=10)



        btm_login=Button(login_frame,text="Login",width=15,font=("times new roman",14,"bold"),bg="red",command=self.login,fg="blue").grid(row=3,column=0,padx=12,pady=10)


        btm_login=Button(login_frame,text="Exit",command=self.Exit,width=15,font=("times new roman",14,"bold"),bg="red",fg="blue").grid(row=3,column=1,padx=16,pady=10)



root.mainloop()        

