from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk, messagebox
import sqlite3

class Types:
    def __init__(self, root):
            self.root = root
            self.root.geometry("1100x500+220+130")
            self.root.title("Rice Retailing Billing System")
            self.root.config(bg="white")
            self.root.focus_force()
            self.root.resizable(0, 0)

            # ==========Variables==========#
            self.var_category_id = StringVar()
            self.var_name = StringVar()

            #========Title========#
            lbl_title = Label(self.root, text="Manage the Types of Rice", font=("times new roman", 25, "bold"),
                  bg="#828c51", fg="white", bd = 3, relief = RIDGE)
            lbl_title.pack(side = TOP, padx = 10, pady = 20, fill = X)

            lbl_name = Label(self.root, text="Enter Type of Rice", font=("times new roman", 25, "bold"),
                      bg="white")
            lbl_name.place(x = 50, y = 100)

            txt_name = Entry(self.root, textvariable=self.var_name, font=("times new roman", 20),
                     bg="white")
            txt_name.place(x=50, y=170, width =300)

            #==========Buttons==========#
            add_btn = Button(self.root, command = self.add, text = "ADD" , font=("times new roman", 14, "bold"),
                     bg="#335145", fg = "white", cursor = "hand2")
            add_btn.place(x=360, y=170, height=30, width = 150)
            delete_btn = Button(self.root, command = self.delete_cmd, text="DELETE", font=("times new roman", 14, "bold"),
                     bg="#ff0000", fg="white", cursor="hand2")
            delete_btn.place(x=520, y=170, height=30, width = 150)

            #=========Category_Details==========#
            category_frame = Frame(self.root, bd=3, relief=RIDGE)
            category_frame.place(x=700, y=100, width=350, height=100)

            vertical_Scroll = Scrollbar(category_frame, orient=VERTICAL)
            horizontal_Scroll = Scrollbar(category_frame, orient=HORIZONTAL)

            self.category_Table = ttk.Treeview(category_frame, columns=("Category_ID", "Name"),
                                               yscrollcommand=vertical_Scroll.set, xscrollcommand=horizontal_Scroll.set)
            horizontal_Scroll.pack(side=BOTTOM, fill=X)
            horizontal_Scroll.config(command=self.category_Table.xview)
            vertical_Scroll.pack(side=RIGHT, fill=Y)
            vertical_Scroll.config(command=self.category_Table.yview)

            self.category_Table.heading("Category_ID", text="CATEGORY NO.")
            self.category_Table.heading("Name", text="TYPE OF RICE")
            self.category_Table["show"] = "headings"

            self.category_Table.column("Category_ID", width=90)
            self.category_Table.column("Name", width=100)
            self.category_Table.pack(fill=BOTH, expand=1)
            self.category_Table.bind("<ButtonRelease-1>", self.get_Data)

            self.show()
            #=========Image==========#
            self.image1 = Image.open("img/types.png")
            self.image1 = self.image1.resize((500,250), Image.LANCZOS)
            self.image1 = ImageTk.PhotoImage(self.image1)

            self.label_image1 = Label(self.root, image = self.image1,
                                      bd = 2, relief = RAISED)
            self.label_image1.place(x = 50, y = 220)

            self.image2 = Image.open("img/pngegg.png")
            self.image2 = self.image2.resize((500, 250), Image.LANCZOS)
            self.image2 = ImageTk.PhotoImage(self.image2)

            self.label_image2 = Label(self.root, image=self.image2,
                                      bd=2, relief=RAISED)
            self.label_image2.place(x=520, y=220)

            self.show()

            #=========Functions==========#

    def add(self):
        conn = sqlite3.connect(database=r"billsystem.db")
        cur = conn.cursor()
        try:
            if self.var_name.get() == "":
                messagebox.showerror("Error", "Type of Rice must be required", parent=self.root)
            else:
                cur.execute("Select * from types where Name = ?", (self.var_name.get(),))
                row = cur.fetchone()
                if row != None:
                    messagebox.showerror("Error", "Type of Rice already present, try another",
                                         parent=self.root)
                else:
                    cur.execute("Insert into types (Name) values(?)", (self.var_name.get(),))
                    conn.commit()
                    messagebox.showinfo("Success", "Type of Rice Added", parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)

    def show(self):
            conn = sqlite3.connect(database=r"billsystem.db")
            cur = conn.cursor()
            try:
                cur.execute("select * from types")
                rows = cur.fetchall()
                self.category_Table.delete(*self.category_Table.get_children())
                for row in rows:
                    self.category_Table.insert("", END, values=row)

            except Exception as ex:
                messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)

    def get_Data(self, ev):
        click = self.category_Table.focus()
        data_content = (self.category_Table.item(click))
        row = data_content["values"]

        self.var_category_id.set(row[0])
        self.var_name.set(row[1])

    def delete_cmd(self):
            conn = sqlite3.connect(database=r"billsystem.db")
            cur = conn.cursor()
            try:
                if self.var_name.get() == "":
                    messagebox.showerror("Error", "Please select or input type of rice.", parent=self.root)
                else:
                    cur.execute("Select * from types where Name = ?", (self.var_name.get(),))
                    row = cur.fetchone()
                    if row == None:
                        messagebox.showerror("Error", "Please Select or Input type of rice", parent=self.root)
                    else:
                        option_ask = messagebox.askyesno("Confirmation", "Do you really want to delete?",
                                                         parent=self.root)
                        if option_ask == True:
                            cur.execute("delete from types where Name = ?", (self.var_name.get(),))
                            conn.commit()
                            messagebox.showinfo("Deleted", "Type of Rice Deleted Successfully", parent=self.root)
                            self.show()
                            self.var_category_id.set("")
                            self.var_name.set("")
            except Exception as ex:
                messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)


if __name__ == "__main__":
     root = Tk()
     obj = Types(root)
     root.mainloop()