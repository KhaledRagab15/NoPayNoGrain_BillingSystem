from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
import sqlite3
import os
import emailpass
import smtplib
import time

class Login:
    def __init__(self, root):
        self.root = root
        self.root.geometry("700x450")
        self.root.title("Login to No Pay No Grain Billing System")
        self.root.config(bg = "white")
        self.root.resizable(0,0)

        title = Label(self.root, text="Login to Enter Billing System",
                      font=("Times New Roman", 35, "bold")
                      , bg="#454B1B", fg="white")
        title.place(x=0, y=0, relwidth=1, height=70)

        #==========Variables==============#
        self.var_employee_id= StringVar()
        self.var_password = StringVar()
        self.var_otp = StringVar()
        self.var_newpassword = StringVar()
        self.var_confirmpassword = StringVar()

        # self.otp = ""

        # =======register_frame=======#
        register_Frame = Frame(self.root, bd=2,
                               relief=RIDGE, bg="white")
        register_Frame.place(x=390, y=378, width = 285, height = 60)
        dont_lbl = Label(register_Frame, text="   Please Enter Employee ID and Password\nto continue",
                             font=("Times New Roman", 11)
                             , bg="white", compound=LEFT)
        dont_lbl.place(x=5, y=12)

        #==========Image==============#
        self.image = Image.open("img/login.png")
        self.image = self.image.resize((300, 350), Image.LANCZOS)
        self.image = ImageTk.PhotoImage(self.image)

        self.label_image = Label(self.root, image=self.image,
                                  bd=4, relief=RAISED)
        self.label_image.place(x=40, y=80)

        # self.send_email("Hans")

        username_lbl = Label(self.root, text="Employee ID",
                                  font=("Times New Roman", 13, "bold")
                                  , bg="white", compound = LEFT)
        username_lbl.place(x=360, y=100)


        pass_lbl = Label(self.root, text="Password",
                             font=("Times New Roman", 13, "bold")
                             , bg="white", compound=LEFT)
        pass_lbl.place(x=360, y=170)

        username_txt = Entry(self.root, textvariable = self.var_employee_id,
                             font=("Times New Roman", 13)
                             , bg="white", relief = GROOVE)
        username_txt.place(x=480, y=100, width = 200)

        pass_txt = Entry(self.root, show = "*", textvariable = self.var_password,
                         font=("Times New Roman", 13)
                         , bg="white", relief = GROOVE)
        pass_txt.place(x=480, y=170, width = 200)

        login_btn = Button(self.root, text="Login", command = self.login, font=("times new roman", 14, "bold"),
                            bg="#98FB98", cursor="hand2")

        login_btn.place(x=460, y=220, width=150, height = 30)

        # or_lbl = Label(self.root, text="---------OR----------",
        #                  font=("Times New Roman", 12)
        #                  , bg="white", fg = "gray", compound=LEFT)
        # or_lbl.place(x=460, y=264)

        # forgot_btn = Button(self.root, text="Forgot Password?", command = self.forget_window, font=("times new roman", 13, "bold"),
        #                    bg="white", fg = "blue", cursor="hand2", bd = 0)
        # forgot_btn.place(x=460, y=300, width=150, height=30)


    def login(self):
        conn = sqlite3.connect(database=r"billsystem.db")
        cur = conn.cursor()
        try:
            if self.var_employee_id.get() == "" or self.var_password.get() == "":
                messagebox.showerror("Error", "All field are required", parent = self.root)
            else:
                cur.execute("select UserType from employee where Emp_ID = ? and Pass = ?",(
                    self.var_employee_id.get(), self.var_password.get()
                ))
                user = cur.fetchone()
                if user == None:
                    messagebox.showerror("Error", "Invalid Username/Password", parent=self.root)
                else:
                    if user[0] == "Admin":
                        self.root.destroy()
                        os.system("python dashboard.py")
                    else:
                        self.root.destroy()
                        os.system("python billing.py")

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)

    # def forget_window(self):
    #     conn = sqlite3.connect(database=r"billsystem.db")
    #     cur = conn.cursor()
    #     try:
    #         if self.var_employee_id.get() == "":
    #             messagebox.showerror("Error", "Employee ID must be required", parent=self.root)
    #         else:
    #             cur.execute("select Email from employee where Emp_ID = ?", (
    #                 self.var_employee_id.get(),
    #             ))
    #             email = cur.fetchone()
    #             if email == None:
    #                 messagebox.showerror("Error", "Invalid Employee ID, try again", parent=self.root)
    #             else:
    #                 self.forget_window = Toplevel(self.root)
    #                 self.forget_window.title("Reset Password")
    #                 self.forget_window.geometry("400x350+500+100")
    #                 self.forget_window.focus_force()
    #
    #
    #                 title = Label(self.forget_window, text = "Reset Password", font = ("times new roman", 13, "bold")
    #                               , bg = "#008080", fg = "white")
    #                 title.pack(side = TOP, fill = X)
    #
    #                 reset_lbl = Label(self.forget_window, text="Enter OTP Sent on Registered Email", font=("times new roman", 13, "bold"))
    #                 reset_lbl.place(x = 20, y = 60)
    #                 txt_reset = Entry(self.forget_window, textvariable = self.var_otp, font=("times new roman", 13),
    #                                   bg = "lightyellow")
    #                 txt_reset.place(x = 20, y = 100, width = 250, height = 30)
    #                 self.reset_Button = Button(self.forget_window, text = "SUBMIT", font=("times new roman", 13)
    #                                       , bg = "#00FF7F")
    #                 self.reset_Button.place(x = 280, y = 100, width = 100, height = 30)
    #
    #
    #                 newpass_lbl = Label(self.forget_window, text="New Password",
    #                                   font=("times new roman", 13, "bold"))
    #                 newpass_lbl.place(x=20, y=160)
    #                 txt_newpass = Entry(self.forget_window, textvariable = self.var_newpassword, font=("times new roman", 13),
    #                                   bg = "lightyellow")
    #                 txt_newpass.place(x = 20, y = 190, width = 250, height = 30)
    #
    #                 confirm_lbl = Label(self.forget_window, text="Confirm Password",
    #                                   font=("times new roman", 13, "bold"))
    #                 confirm_lbl.place(x=20, y=225)
    #                 txt_confirm = Entry(self.forget_window, textvariable=self.var_confirmpassword, font=("times new roman", 13),
    #                                   bg="lightyellow")
    #                 txt_confirm.place(x=20, y=255, width=250, height=30)
    #
    #                 self.update_Button = Button(self.forget_window, text="UPDATE", font=("times new roman", 13)
    #                                            , bg="#00FF7F")
    #                 self.update_Button.place(x=150, y=300, width=100, height=30)
    #
    #
    #
    #     except Exception as ex:
    #         messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)

    # def send_email(self, to_):
    #     s = smtplib.SMTP("smtp.gmail.com", 587)
    #     s.starttls()
    #     email_ = emailpass.email_
    #     pass_ = emailpass.pass_
    #
    #     s.login(email_,pass_)
    #
    #     self.otp = str(time.strftime("%H%M%S")) + str(time.strftime("%S"))
    #     print(self.otp)


if __name__ == "__main__":
    root = Tk()
    obj = Login(root)
    root.mainloop()