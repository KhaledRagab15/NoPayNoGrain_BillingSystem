from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk, messagebox
import sqlite3

class Employee:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1100x500+220+130")
        self.root.title("Rice Retailing Billing System")
        self.root.config(bg = "white")
        self.root.focus_force()
        self.root.resizable(0,0)

        #==========Variables==========#
        self.var_searchby = StringVar()
        self.var_searchtxt = StringVar()

        self.var_emp_id = StringVar()
        self.var_gender = StringVar()
        self.var_contact = StringVar()
        self.var_name = StringVar()
        self.var_dob = StringVar()
        self.var_doj = StringVar()
        self.var_email = StringVar()
        self.var_pass = StringVar()
        self.var_usertype = StringVar()
        self.var_salary = StringVar()





        #==========Search_Frame==========#
        search_Frame = LabelFrame(self.root, text = "Search Employee", bg = "white",
                                  font=("Times New Roman", 12, "bold")
                                 , bd=2, relief=RIDGE)
        search_Frame.place(x = 250, y = 20, width = 600, height = 70)

        #==========Options==========#
        combo_Search = ttk.Combobox(search_Frame, textvariable = self.var_searchby, values = ("Select", "Email", "Name", "Contact"),
                                    state = "readonly", justify = CENTER,
                                    font=("Times New Roman", 13))
        combo_Search.place(x = 10, y = 10, width = 180)
        combo_Search.current(0)

        txt_Search = Entry(search_Frame, textvariable = self.var_searchtxt, font = ("Times New Roman", 13), bg = "lightyellow")
        txt_Search.place(x = 200, y = 10)

        btn_Search = Button(search_Frame, command = self.search_cmd,text = "Search", font=("Times New Roman", 13), bg="#4caf50",
                            cursor = "hand2", fg = "white")
        btn_Search.place(x=410, y=9, width = 150, height = 30)


        #==========Title==========#
        title = Label(self.root, text = "Employee Details", font = ("times new roman", 13),
                      bg = "#828c51", fg = "white")
        title.place(x = 50, y = 100, width = 1000)

        #==========Content==========#

        #==========Row1==========#
        lbl_emp_id = Label(self.root, text = "Employee ID", font = ("times new roman", 13),
                      bg = "white")
        lbl_emp_id.place(x = 50, y = 150)
        lbl_gender = Label(self.root, text="Gender", font=("times new roman", 13),
                           bg="white")
        lbl_gender.place(x=350, y=150)
        lbl_contact = Label(self.root, text = "Contact", font = ("times new roman", 13),
                      bg = "white")
        lbl_contact.place(x = 700, y = 150)

        txt_emp_id = Entry(self.root, textvariable = self.var_emp_id , font=("times new roman", 13),
                           bg="white")
        txt_emp_id.place(x=150, y=150, width=180)
        combo_Gender = ttk.Combobox(self.root, textvariable=self.var_gender,
                                    values=("Select", "Male", "Female", "Other"),
                                    state="readonly", justify=CENTER,
                                    font=("Times New Roman", 13))
        combo_Gender.place(x=500, y=150, width=180)
        combo_Gender.current(0)
        txt_contact = Entry(self.root, textvariable = self.var_contact, font=("times new roman", 13),
                            bg="white")
        txt_contact.place(x=850, y=150, width=180)


        #==========Row2==========#
        lbl_name = Label(self.root, text="Name", font=("times new roman", 13),
                         bg="white")
        lbl_name.place(x=50, y=190)
        lbl_dob = Label(self.root, text="Date of Birth", font=("times new roman", 13),
                        bg="white")
        lbl_dob.place(x=350, y=190)
        lbl_doj = Label(self.root, text="Date of Joining", font=("times new roman", 13),
                        bg="white")
        lbl_doj.place(x=700, y=190)

        txt_name = Entry(self.root, textvariable=self.var_name, font=("times new roman", 13),
                         bg="white")
        txt_name.place(x=150, y=190, width=180)
        txt_dob = Entry(self.root, textvariable=self.var_dob, font=("times new roman", 13),
                        bg="white")
        txt_dob.place(x=500, y=190, width=180)
        txt_doj = Entry(self.root, textvariable=self.var_doj, font=("times new roman", 13),
                        bg="white")
        txt_doj.place(x=850, y=190, width=180)

        #==========Row3==========#
        lbl_email = Label(self.root, text="Email", font=("times new roman", 13),
                          bg="white")
        lbl_email.place(x=50, y=230)
        lbl_pass = Label(self.root, text="Password", font=("times new roman", 13),
                         bg="white")
        lbl_pass.place(x=350, y=230)
        lbl_usertype = Label(self.root, text="User Type", font=("times new roman", 13),
                             bg="white")
        lbl_usertype.place(x=700, y=230)

        txt_email = Entry(self.root, textvariable=self.var_email, font=("times new roman", 13),
                         bg="white")
        txt_email.place(x=150, y=230, width=180)
        txt_pass = Entry(self.root,textvariable=self.var_pass, font=("times new roman", 13),
                        bg="white")
        txt_pass.place(x=500, y=230, width=180)
        combo_usertype = ttk.Combobox(self.root, textvariable=self.var_usertype,
                                    values=("Select", "Admin", "Employee"),
                                    state="readonly", justify=CENTER,
                                    font=("Times New Roman", 13))
        combo_usertype.place(x=850, y=230, width=180)
        combo_usertype.current(0)

        #==========Row4==========#
        lbl_address = Label(self.root, text="Address", font=("times new roman", 13),
                          bg="white")
        lbl_address.place(x=50, y=270)
        lbl_salary = Label(self.root, text="Salary", font=("times new roman", 13),
                         bg="white")
        lbl_salary.place(x=500, y=270)

        self.txt_address = Text(self.root, font=("times new roman", 13),
                          bg="white")
        self.txt_address.place(x=150, y=270, width=300, height=60)
        txt_salary = Entry(self.root, textvariable=self.var_salary, font=("times new roman", 13),
                         bg="white")
        txt_salary.place(x=580, y=270, width=180)

        #==========Buttons==========#
        btn_Save = Button(self.root, text="Save", font=("Times New Roman", 13), bg="#0D98BA",
                            cursor="hand2", fg="white", command = self.add)
        btn_Save.place(x=500, y=305, width=110, height=28)
        btn_Update = Button(self.root, text="Update", command = self.update, font=("Times New Roman", 13), bg="#335145",
                            cursor="hand2", fg="white")
        btn_Update.place(x=620, y=305, width=110, height=28)
        btn_Delete = Button(self.root, command = self.delete_cmd, text="Delete", font=("Times New Roman", 13), bg="#ff0000",
                            cursor="hand2", fg="white")
        btn_Delete.place(x=740, y=305, width=110, height=28)
        btn_Clear = Button(self.root, command = self.clear_cmd, text="Clear", font=("Times New Roman", 13), bg="#808080",
                            cursor="hand2", fg="white")
        btn_Clear.place(x=860, y=305, width=110, height=28)

        #=========Employee_Details==========#
        emp_frame = Frame(self.root, bd = 3, relief = RIDGE)
        emp_frame.place(x = 0, y = 350, relwidth = 1, height = 150)

        vertical_Scroll = Scrollbar(emp_frame, orient = VERTICAL)
        horizontal_Scroll = Scrollbar(emp_frame, orient = HORIZONTAL)

        self.employee_Table = ttk.Treeview(emp_frame, columns = ("Emp_ID", "Name", "Email",
                                                                 "Gender", "Contact", "DoB", "DoJ", "Pass",
                                                                 "UserType", "Address", "Salary"),
                                           yscrollcommand = vertical_Scroll.set, xscrollcommand = horizontal_Scroll.set)
        horizontal_Scroll.pack(side = BOTTOM, fill = X)
        horizontal_Scroll.config(command = self.employee_Table.xview)
        vertical_Scroll.pack(side = RIGHT, fill = Y)
        vertical_Scroll.config(command = self.employee_Table.yview)


        self.employee_Table.heading("Emp_ID", text = "EMPLOYEE ID")
        self.employee_Table.heading("Name", text="NAME")
        self.employee_Table.heading("Email", text="EMAIL")
        self.employee_Table.heading("Gender", text="GENDER")
        self.employee_Table.heading("Contact", text="CONTACT NUMBER")
        self.employee_Table.heading("DoB", text="DATE OF BIRTH")
        self.employee_Table.heading("DoJ", text="DATE OF JOINING")
        self.employee_Table.heading("Pass", text="PASS")
        self.employee_Table.heading("UserType", text="USER TYPE")
        self.employee_Table.heading("Address", text="ADDRESS")
        self.employee_Table.heading("Salary", text="SALARY")
        self.employee_Table["show"] = "headings"

        self.employee_Table.column("Emp_ID", width = 90)
        self.employee_Table.column("Name", width = 100)
        self.employee_Table.column("Email", width = 100)
        self.employee_Table.column("Gender", width = 100)
        self.employee_Table.column("Contact", width = 130)
        self.employee_Table.column("DoB", width = 100)
        self.employee_Table.column("DoJ", width = 105)
        self.employee_Table.column("Pass", width = 90)
        self.employee_Table.column("UserType", width = 100)
        self.employee_Table.column("Address", width = 100)
        self.employee_Table.column("Salary", width = 100)

        self.employee_Table.pack(fill = BOTH, expand = 1)
        self.employee_Table.bind("<ButtonRelease-1>", self.get_Data)

        self.show()

    #============================#
    def add(self):
        conn = sqlite3.connect(database = r"billsystem.db")
        cur = conn.cursor()
        try:
            if self.var_emp_id.get() == "":
                messagebox.showerror("Error", "Employee ID must be required", parent = self.root)
            else:
                cur.execute("Select * from employee where Emp_ID = ?", (self.var_emp_id.get(),))
                row = cur.fetchone()
                if row != None:
                    messagebox.showerror("Error", "This Employee ID is already inputted, try another", parent = self.root)
                else:
                    cur.execute("Insert into employee (Emp_ID, Name, Email, Gender, Contact, DoB, DoJ, Pass, UserType, Address, Salary) values(?,?,?,?,?,?,?,?,?,?,?)", (
                                self.var_emp_id.get(),
                                self.var_name.get(),
                                self.var_email.get(),
                                self.var_gender.get(),
                                self.var_contact.get(),

                                self.var_dob.get(),
                                self.var_doj.get(),

                                self.var_pass.get(),
                                self.var_usertype.get(),
                                self.txt_address.get("1.0", END),
                                self.var_salary.get(),
                    ))
                    conn.commit()
                    messagebox.showinfo("Success", "Employee Registered", parent = self.root)
                    self.show()

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent = self.root)

    def show(self):
        conn = sqlite3.connect(database = r"billsystem.db")
        cur = conn.cursor()
        try:
            cur.execute("select * from employee")
            rows = cur.fetchall()
            self.employee_Table.delete(*self.employee_Table.get_children())
            for row in rows:
                self.employee_Table.insert("", END, values = row)

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent = self.root)

    def get_Data(self,ev):
        click = self.employee_Table.focus()
        data_content = (self.employee_Table.item(click))
        row = data_content["values"]

        self.var_emp_id.set(row[0])
        self.var_name.set(row[1])
        self.var_email.set(row[2])
        self.var_gender.set(row[3])
        self.var_contact.set(row[4])

        self.var_dob.set(row[5])
        self.var_doj.set(row[6])

        self.var_pass.set(row[7])
        self.var_usertype.set(row[8])
        self.txt_address.delete("1.0", END)
        self.txt_address.insert(END, row[9])
        self.var_salary.set(row[10])

    def update(self):
        conn = sqlite3.connect(database = r"billsystem.db")
        cur = conn.cursor()
        try:
            if self.var_emp_id.get() == "":
                messagebox.showerror("Error", "Please select the Employee ID", parent = self.root)
            else:
                cur.execute("Select * from employee where Emp_ID = ?", (self.var_emp_id.get(),))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror("Error", "Invalid Employee ID", parent = self.root)
                else:
                    cur.execute("Update employee set Name = ?, Email = ?, Gender = ?, Contact = ?, DoB = ?, DoJ = ?, Pass = ?, UserType = ?, Address= ?, Salary = ? where Emp_ID = ?", (
                                self.var_name.get(),
                                self.var_email.get(),
                                self.var_gender.get(),
                                self.var_contact.get(),

                                self.var_dob.get(),
                                self.var_doj.get(),

                                self.var_pass.get(),
                                self.var_usertype.get(),
                                self.txt_address.get("1.0", END),
                                self.var_salary.get(),
                                self.var_emp_id.get(),
                    ))
                    conn.commit()
                    messagebox.showinfo("Success", "Employee Updated Succesfully", parent = self.root)
                    self.show()

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent = self.root)

    def clear_cmd(self):
        self.var_emp_id.set("")
        self.var_name.set("")
        self.var_email.set("")
        self.var_gender.set("Select")
        self.var_contact.set("")

        self.var_dob.set("")
        self.var_doj.set("")

        self.var_pass.set("")
        self.var_usertype.set("Admin")
        self.txt_address.delete("1.0", END)
        self.var_salary.set("")
        self.var_searchtxt.set("")
        self.var_searchby.set("Select")
        self.show()


    def search_cmd(self):
        conn = sqlite3.connect(database=r"billsystem.db")
        cur = conn.cursor()
        try:
            if self.var_searchby.get() == "Select":
                messagebox.showerror("Error", "Select Search by option", parent = self.root)
            elif self.var_searchtxt.get() == "":
                messagebox.showerror("Error", "Please input to search", parent=self.root)
            else:
                cur.execute("select * from employee where " +self.var_searchby.get()+" LIKE '%"+self.var_searchtxt.get()+"%'")
                rows = cur.fetchall()
                if len(rows) != 0:
                    self.employee_Table.delete(*self.employee_Table.get_children())
                    for row in rows:
                        self.employee_Table.insert("", END, values=row)
                else:
                    messagebox.showerror("Error", "No record found!", parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)

    def delete_cmd(self):
        conn = sqlite3.connect(database = r"billsystem.db")
        cur = conn.cursor()
        try:
            if self.var_emp_id.get() == "":
                messagebox.showerror("Error", "Please input the Employee ID", parent=self.root)
            else:
                cur.execute("Select * from employee where Emp_ID = ?", (self.var_emp_id.get(),))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror("Error", "Invalid Employee ID", parent=self.root)
                else:
                    option_ask = messagebox.askyesno("Confirmation", "Do you really want to delete the employee?", parent = self.root)
                    if option_ask == True:
                        cur.execute("delete from employee where Emp_ID = ?", (self.var_emp_id.get(),))
                        conn.commit()
                        messagebox.showinfo("Deleted", "Employee Deleted Successfully", parent = self.root)
                        self.clear_cmd()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)


if __name__ == "__main__":
    root = Tk()
    obj = Employee(root)
    root.mainloop()