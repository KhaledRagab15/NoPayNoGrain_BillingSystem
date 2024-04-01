from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk, messagebox
import sqlite3

class Supplier:
    def __init__(self, root):
            self.root = root
            self.root.geometry("1100x500+220+130")
            self.root.title("Rice Retailing Billing System")
            self.root.config(bg="white")
            self.root.focus_force()
            self.root.resizable(0, 0)

            # ==========Variables==========#
            self.var_searchby = StringVar()
            self.var_searchtxt = StringVar()

            self.var_supplier_invoice = StringVar()
            self.var_name = StringVar()
            self.var_contact = StringVar()


            # ==========Search_Frame==========#
            # ==========Options==========#
            lbl_Search = Label(self.root, text= "Invoice No.",
                                        font=("Times New Roman", 14), bg = "white")
            lbl_Search.place(x=700, y=80)

            txt_Search = Entry(self.root, textvariable=self.var_searchtxt, font=("Times New Roman", 13),
                               bg="lightyellow")
            txt_Search.place(x=800, y=80, width = 140)

            btn_Search = Button(self.root, command=self.search_cmd, text="Search", font=("Times New Roman", 13),
                                bg="#4caf50",
                                cursor="hand2", fg="white")
            btn_Search.place(x=950, y=79, width=100, height=25)

            #==========Title==========#
            title = Label(self.root, text="Supplier Details", font=("times new roman", 20, "bold"),
                          bg="#828c51", fg="white")
            title.place(x=50, y=10, width=1000, height = 40)

            # ==========Content==========#

            # ==========Row1==========#
            lbl_supplier_invoice = Label(self.root, text="Invoice No.", font=("times new roman", 13),
                               bg="white")
            lbl_supplier_invoice.place(x=50, y=80)
            txt_supplier_invoice = Entry(self.root, textvariable=self.var_supplier_invoice, font=("times new roman", 13),
                               bg="white")
            txt_supplier_invoice.place(x=180, y=80, width=180)

            # ==========Row2==========#
            lbl_name = Label(self.root, text="Name", font=("times new roman", 13),
                             bg="white")
            lbl_name.place(x=50, y=120)
            txt_name = Entry(self.root, textvariable=self.var_name, font=("times new roman", 13),
                             bg="white")
            txt_name.place(x=180, y=120, width=180)

            # ==========Row3==========#
            lbl_contact = Label(self.root, text="Contact", font=("times new roman", 13),
                              bg="white")
            lbl_contact.place(x=50, y=160)

            txt_contact = Entry(self.root, textvariable=self.var_contact, font=("times new roman", 13),
                              bg="white")
            txt_contact.place(x=180, y=160, width=180)

            # ==========Row4==========#
            lbl_description = Label(self.root, text="Description", font=("times new roman", 13),
                                bg="white")
            lbl_description.place(x=50, y=200)

            self.txt_description = Text(self.root, font=("times new roman", 13),
                                    bg="white")
            self.txt_description.place(x=180, y=200, width=500, height=90)

            #==========Buttons==========#
            btn_Save = Button(self.root, text="Save", font=("Times New Roman", 13), bg="#0D98BA",
                              cursor="hand2", fg="white", command=self.add)
            btn_Save.place(x=180, y=350, width=110, height=35)
            btn_Update = Button(self.root, text="Update", command=self.update, font=("Times New Roman", 13),
                                bg="#335145",
                                cursor="hand2", fg="white")
            btn_Update.place(x=300, y=350, width=110, height=35)
            btn_Delete = Button(self.root, command=self.delete_cmd, text="Delete", font=("Times New Roman", 13),
                                bg="#ff0000",
                                cursor="hand2", fg="white")
            btn_Delete.place(x=420, y=350, width=110, height=35)
            btn_Clear = Button(self.root, command=self.clear_cmd, text="Clear", font=("Times New Roman", 13),
                               bg="#808080",
                               cursor="hand2", fg="white")
            btn_Clear.place(x=540, y=350, width=110, height=35)

            #=========Supplier_Details==========#
            supplier_frame = Frame(self.root, bd=3, relief=RIDGE)
            supplier_frame.place(x=700, y=120, width=350, height=350)

            vertical_Scroll = Scrollbar(supplier_frame, orient=VERTICAL)
            horizontal_Scroll = Scrollbar(supplier_frame, orient=HORIZONTAL)

            self.supplier_Table = ttk.Treeview(supplier_frame, columns=("Invoice_No", "Name", "Contact",
                                                                   "Description"),
                                               yscrollcommand=vertical_Scroll.set, xscrollcommand=horizontal_Scroll.set)
            horizontal_Scroll.pack(side=BOTTOM, fill=X)
            horizontal_Scroll.config(command=self.supplier_Table.xview)
            vertical_Scroll.pack(side=RIGHT, fill=Y)
            vertical_Scroll.config(command=self.supplier_Table.yview)

            self.supplier_Table.heading("Invoice_No", text="INVOICE NO.")
            self.supplier_Table.heading("Name", text="NAME")
            self.supplier_Table.heading("Contact", text="CONTACT")
            self.supplier_Table.heading("Description", text="DESCRIPTION")
            self.supplier_Table["show"] = "headings"

            self.supplier_Table.column("Invoice_No", width=90)
            self.supplier_Table.column("Name", width=100)
            self.supplier_Table.column("Contact", width=130)
            self.supplier_Table.column("Description", width=100)
            self.supplier_Table.pack(fill=BOTH, expand=1)
            self.supplier_Table.bind("<ButtonRelease-1>", self.get_Data)

            self.show()

        #========Functions=================#
    def add(self):
            conn = sqlite3.connect(database=r"billsystem.db")
            cur = conn.cursor()
            try:
                if self.var_supplier_invoice.get() == "":
                    messagebox.showerror("Error", "Invoice No. must be required", parent=self.root)
                else:
                    cur.execute("Select * from supplier where Invoice_No = ?", (self.var_supplier_invoice.get(),))
                    row = cur.fetchone()
                    if row != None:
                        messagebox.showerror("Error", "Invoice No. is already inputted, try another",
                                             parent=self.root)
                    else:
                        cur.execute("Insert into supplier (Invoice_No, Name, Contact, Description) values(?,?,?,?)",(
                                self.var_supplier_invoice.get(),
                                self.var_name.get(),
                                self.var_contact.get(),
                                self.txt_description.get("1.0", END),
                            ))
                        conn.commit()
                        messagebox.showinfo("Success", "Supplier Registered", parent=self.root)
                        self.show()
            except Exception as ex:
                messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)

    def show(self):
            conn = sqlite3.connect(database=r"billsystem.db")
            cur = conn.cursor()
            try:
                cur.execute("select * from supplier")
                rows = cur.fetchall()
                self.supplier_Table.delete(*self.supplier_Table.get_children())
                for row in rows:
                    self.supplier_Table.insert("", END, values=row)

            except Exception as ex:
                messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)

    def get_Data(self, ev):
            click = self.supplier_Table.focus()
            data_content = (self.supplier_Table.item(click))
            row = data_content["values"]

            self.var_supplier_invoice.set(row[0])
            self.var_name.set(row[1])
            self.var_contact.set(row[2])
            self.txt_description.delete("1.0", END)
            self.txt_description.insert(END, row[3])

    def update(self):
            conn = sqlite3.connect(database=r"billsystem.db")
            cur = conn.cursor()
            try:
                if self.var_supplier_invoice.get() == "":
                    messagebox.showerror("Error", "Please input Invoice No.", parent=self.root)
                else:
                    cur.execute("Select * from supplier where Invoice_No = ?", (self.var_supplier_invoice.get(),))
                    row = cur.fetchone()
                    if row == None:
                        messagebox.showerror("Error", "Invalid Invoice No.", parent=self.root)
                    else:
                        cur.execute("Update supplier set Name = ?, Contact = ?,  Description = ? where Invoice_No = ?",
                            (
                                self.var_name.get(),
                                self.var_contact.get(),
                                self.txt_description.get("1.0", END),
                                self.var_supplier_invoice.get(),
                            ))
                        conn.commit()
                        messagebox.showinfo("Success", "Supplier Updated Succesfully", parent=self.root)
                        self.show()

            except Exception as ex:
                messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)

    def clear_cmd(self):
            self.var_supplier_invoice.set("")
            self.var_name.set("")
            self.var_contact.set("")
            self.txt_description.delete("1.0", END)
            self.var_searchtxt.set("")
            self.var_searchby.set("Select")
            self.show()

    def search_cmd(self):
            conn = sqlite3.connect(database=r"billsystem.db")
            cur = conn.cursor()
            try:
                if self.var_searchtxt.get() == "":
                    messagebox.showerror("Error", "Please input Invoice No.", parent=self.root)
                else:
                    cur.execute("select * from supplier where Invoice_No = ?", (self.var_searchtxt.get(),))
                    row = cur.fetchone()
                    if row != None:
                        self.supplier_Table.delete(*self.supplier_Table.get_children())
                        self.supplier_Table.insert("", END, values=row)
                    else:
                        messagebox.showerror("Error", "No record found!", parent=self.root)
            except Exception as ex:
                messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)

    def delete_cmd(self):
            conn = sqlite3.connect(database=r"billsystem.db")
            cur = conn.cursor()
            try:
                if self.var_supplier_invoice.get() == "":
                    messagebox.showerror("Error", "Please input Invoice No.", parent=self.root)
                else:
                    cur.execute("Select * from supplier where Invoice_No = ?", (self.var_supplier_invoice.get(),))
                    row = cur.fetchone()
                    if row == None:
                        messagebox.showerror("Error", "Invalid Invoice No.", parent=self.root)
                    else:
                        option_ask = messagebox.askyesno("Confirmation", "Do you really want to delete?",
                                                         parent=self.root)
                        if option_ask == True:
                            cur.execute("delete from supplier where Invoice_No = ?", (self.var_supplier_invoice.get(),))
                            conn.commit()
                            messagebox.showinfo("Deleted", "Supplier Deleted Successfully", parent=self.root)
                            self.clear()
            except Exception as ex:
                messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)

if __name__ == "__main__":
     root = Tk()
     obj = Supplier(root)
     root.mainloop()