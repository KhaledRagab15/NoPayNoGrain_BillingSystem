from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk, messagebox
import sqlite3

class Product:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1100x500+220+130")
        self.root.title("Rice Retailing Billing System")
        self.root.config(bg = "white")
        self.root.focus_force()
        self.root.resizable(0,0)

        #========Variables========#
        self.var_searchby = StringVar()
        self.var_searchtxt = StringVar()

        self.var_productid = StringVar()
        self.var_type = StringVar()
        self.var_supplier = StringVar()
        self.type_list = []
        self.supplier_list = []
        self.fetch_type_supplier()

        self.var_name = StringVar()
        self.var_price = StringVar()
        self.var_kilos = StringVar()
        self.var_status = StringVar()



        #=========Frame=============#
        product_Frame = Frame(self.root, bd = 3, relief = RIDGE, bg = "white")
        product_Frame.place(x = 10, y = 10, width = 450, height = 480)


        #==========Search_Frame==========#
        search_Frame = LabelFrame(self.root, text = "Search Product", bg = "white",
                                  font=("Times New Roman", 12, "bold")
                                 , bd=2, relief=RIDGE)
        search_Frame.place(x = 480, y = 10, width = 600, height = 70)

        combo_Search = ttk.Combobox(search_Frame, textvariable=self.var_searchby,
                                    values=("Select", "Type", "Supplier", "Name"),
                                    state="readonly", justify=CENTER,
                                    font=("Times New Roman", 13))
        combo_Search.place(x=10, y=10, width=180)
        combo_Search.current(0)
        txt_Search = Entry(search_Frame, textvariable=self.var_searchtxt, font=("Times New Roman", 13),
                           bg="lightyellow")
        txt_Search.place(x=200, y=10)
        btn_Search = Button(search_Frame, command = self.search_cmd, text="Search", font=("Times New Roman", 13),
                            bg="#4caf50",
                            cursor="hand2", fg="white")
        btn_Search.place(x=410, y=9, width=150, height=30)

        #========Label/Title========#
        lbl_title = Label(product_Frame, text="Manage Product Details", font=("times new roman", 18, "bold"),
                    bg="#828c51", fg="white", bd = 3, relief = RIDGE)
        lbl_title.pack(side = TOP, fill = X)

        #==========Column1==========#
        lbl_type = Label(product_Frame, text="Type", font=("times new roman", 15),
                    bg="white")
        lbl_type.place(x = 30, y =60)
        lbl_supplier = Label(product_Frame, text="Supplier", font=("times new roman", 15),
                             bg="white")
        lbl_supplier.place(x=30, y=110)
        lbl_product_name = Label(product_Frame, text="Brand Name", font=("times new roman", 15),
                             bg="white")
        lbl_product_name.place(x=30, y=160)
        lbl_price = Label(product_Frame, text="Price", font=("times new roman", 15),
                             bg="white")
        lbl_price.place(x=30, y=210)
        lbl_kilos = Label(product_Frame, text="Kg/s", font=("times new roman", 15),
                             bg="white")
        lbl_kilos.place(x=30, y=260)
        lbl_status = Label(product_Frame, text="Status", font=("times new roman", 15),
                             bg="white")
        lbl_status.place(x=30, y=310)

        #==========Column2==========#
        combo_Type = ttk.Combobox(product_Frame, textvariable=self.var_type,
                                    values= self.type_list, state="readonly", justify=CENTER,
                                    font=("Times New Roman", 13))
        combo_Type.place(x=150, y=60, width=200)
        combo_Type.current(0)

        combo_Supplier = ttk.Combobox(product_Frame, textvariable=self.var_supplier,
                                      values= self.supplier_list, state="readonly", justify=CENTER,
                                      font=("Times New Roman", 13))
        combo_Supplier.place(x=150, y=110, width=200)
        combo_Supplier.current(0)

        txt_Name = Entry(product_Frame, textvariable=self.var_name,
                                      font=("Times New Roman", 13), bg = "lightyellow")
        txt_Name.place(x=170, y=160, width=200)
        txt_Price = Entry(product_Frame, textvariable=self.var_price,
                         font=("Times New Roman", 13), bg="lightyellow")
        txt_Price.place(x=150, y=210, width=200)
        txt_Kilos = Entry(product_Frame, textvariable=self.var_kilos,
                         font=("Times New Roman", 13), bg="lightyellow")
        txt_Kilos.place(x=150, y=260, width=200)

        combo_Status = ttk.Combobox(product_Frame, textvariable=self.var_status,
                                      values=("Active", "Inactive"), state="readonly", justify=CENTER,
                                      font=("Times New Roman", 13))
        combo_Status.place(x=150, y=310, width=200)
        combo_Status.current(0)

        #==========Buttons==========#
        btn_Save = Button(product_Frame, command = self.add, text="Save", font=("Times New Roman", 13), bg="#0D98BA",
                          cursor="hand2", fg="white")
        btn_Save.place(x=10, y=400, width = 90, height=40)
        btn_Update = Button(product_Frame, command = self.update, text="Update", font=("Times New Roman", 13), bg="#335145",
                            cursor="hand2", fg="white")
        btn_Update.place(x=120, y=400, width = 90, height=40)
        btn_Delete = Button(product_Frame,  command = self.delete_cmd, text="Delete", font=("Times New Roman", 13),
                            bg="#ff0000",
                            cursor="hand2", fg="white")
        btn_Delete.place(x=230, y=400, height=40, width = 90)
        btn_Clear = Button(product_Frame, command = self.clear_cmd, text="Clear", font=("Times New Roman", 13), bg="#808080",
                           cursor="hand2", fg="white")
        btn_Clear.place(x=340, y=400, height=40, width = 90)

        #=========Product_Details==========#
        product_details_Frame = Frame(self.root, bd=3, relief=RIDGE)
        product_details_Frame.place(x=480, y=100, width=600, height=390)

        vertical_Scroll = Scrollbar(product_details_Frame, orient=VERTICAL)
        horizontal_Scroll = Scrollbar(product_details_Frame, orient=HORIZONTAL)

        self.product_Table = ttk.Treeview(product_details_Frame, columns=("Product_ID", "Supplier", "Type",
                                                                          "Name", "Price", "Kilos", "Status"),
                                          yscrollcommand=vertical_Scroll.set,
                                          xscrollcommand=horizontal_Scroll.set)
        horizontal_Scroll.pack(side=BOTTOM, fill=X)
        horizontal_Scroll.config(command=self.product_Table.xview)
        vertical_Scroll.pack(side=RIGHT, fill=Y)
        vertical_Scroll.config(command=self.product_Table.yview)

        self.product_Table.heading("Product_ID", text="PRODUCT ID")
        self.product_Table.heading("Supplier", text="SUPPLIER")
        self.product_Table.heading("Type", text="TYPE OF RICE")
        self.product_Table.heading("Name", text="BRAND NAME")
        self.product_Table.heading("Price", text="PRICE")
        self.product_Table.heading("Kilos", text="Kg/s")
        self.product_Table.heading("Status", text="STATUS")
        self.product_Table["show"] = "headings"

        self.product_Table.column("Product_ID", width=90)
        self.product_Table.column("Supplier", width=100)
        self.product_Table.column("Type", width=100)
        self.product_Table.column("Name", width=100)
        self.product_Table.column("Price", width=100)
        self.product_Table.column("Kilos", width=100)
        self.product_Table.column("Status", width=100)
        self.product_Table.pack(fill=BOTH, expand=1)
        self.product_Table.bind("<ButtonRelease-1>", self.get_Data)

        self.show()


        # ============================#
    def fetch_type_supplier(self):
        self.type_list.append("Empty")
        self.supplier_list.append("Empty")
        conn = sqlite3.connect(database=r"billsystem.db")
        cur = conn.cursor()
        try:
            cur.execute("Select name from types")
            type = cur.fetchall()
            if len(type) > 0:
                del self.type_list[:]
                self.type_list.append("Select")
                for i in type:
                    self.type_list.append(i[0])


            cur.execute("Select name from supplier")
            supplier = cur.fetchall()
            if len(supplier) > 0:
                del self.supplier_list[:]
                self.supplier_list.append("Select")
                for i in supplier:
                    self.supplier_list.append(i[0])
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)


    def add(self):
        conn = sqlite3.connect(database=r"billsystem.db")
        cur = conn.cursor()
        try:
            if self.var_type.get() == "Select" or self.var_type.get() == "Empty" or self.var_supplier.get() == "Select" or self.var_supplier.get() == "Empty" or self.var_name.get() == "":
                messagebox.showerror("Error", "All field are required", parent=self.root)
            else:
                cur.execute("Select * from product where Name = ?", (self.var_name.get(),))
                row = cur.fetchone()
                # if row != None:
                #     messagebox.showerror("Error", "Product already present, try another",
                #                              parent=self.root)
                if row != None:
                    cur.execute("Insert into product (Supplier, Type, Name, Price, Kilos, Status) values(?,?,?,?,?,?)",
                            (
                                self.var_supplier.get(),
                                self.var_type.get(),
                                self.var_name.get(),
                                self.var_price.get(),
                                self.var_kilos.get(),
                                self.var_status.get(),
                            ))
                    conn.commit()
                    messagebox.showinfo("Success", "Product Added Successfully ", parent=self.root)
                    self.show()

        except Exception as ex:
                messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)


    def show(self):
        conn = sqlite3.connect(database=r"billsystem.db")
        cur = conn.cursor()
        try:
            cur.execute("select * from product")
            rows = cur.fetchall()
            self.product_Table.delete(*self.product_Table.get_children())
            for row in rows:
                self.product_Table.insert("", END, values=row)

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)

    def get_Data(self, ev):
            click = self.product_Table.focus()
            data_content = (self.product_Table.item(click))
            row = data_content["values"]
            self.var_productid.set(row[0]),
            self.var_supplier.set(row[1]),
            self.var_type.set(row[2]),
            self.var_name.set(row[3]),
            self.var_price.set(row[4]),
            self.var_kilos.set(row[5]),
            self.var_status.set(row[6])

    def update(self):
        conn = sqlite3.connect(database=r"billsystem.db")
        cur = conn.cursor()
        try:
            if self.var_productid.get() == "":
                messagebox.showerror("Error", "Please select Product from the list", parent=self.root)
            else:
                cur.execute("Select * from product where Product_ID = ?", (self.var_productid.get(),))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror("Error", "Invalid Product", parent=self.root)
                else:
                    cur.execute("Update product set Supplier = ?, Type = ?, Name = ?, Price = ?, Kilos = ?, Status = ?  where Product_ID = ?",
                            (
                                self.var_supplier.get(),
                                self.var_type.get(),
                                self.var_name.get(),
                                self.var_price.get(),
                                self.var_kilos.get(),
                                self.var_status.get(),
                                self.var_productid.get()
                            ))
                    conn.commit()
                    messagebox.showinfo("Success", "Product Updated Succesfully", parent=self.root)
                    self.show()

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)

    def clear_cmd(self):
        self.var_supplier.set("Select"),
        self.var_type.set("Select"),
        self.var_name.set(""),
        self.var_price.set(""),
        self.var_kilos.set(""),
        self.var_status.set("Active")
        self.var_productid.set("")
        self.var_searchtxt.set("")
        self.var_searchby.set("Select")
        self.show()

    def search_cmd(self):
        conn = sqlite3.connect(database=r"billsystem.db")
        cur = conn.cursor()
        try:
            if self.var_searchby.get() == "Select":
                messagebox.showerror("Error", "Select Search by option", parent=self.root)
            elif self.var_searchtxt.get() == "":
                messagebox.showerror("Error", "Please input to search", parent=self.root)
            else:
                cur.execute("select * from product where " + self.var_searchby.get() + " LIKE '%" + self.var_searchtxt.get() + "%'")
                rows = cur.fetchall()
                if len(rows) != 0:
                    self.product_Table.delete(*self.product_Table.get_children())
                    for row in rows:
                        self.product_Table.insert("", END, values=row)
                else:
                        messagebox.showerror("Error", "No record found!", parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)

    def delete_cmd(self):
        conn = sqlite3.connect(database=r"billsystem.db")
        cur = conn.cursor()
        try:
            if self.var_productid.get() == "":
                messagebox.showerror("Error", "Please select product from list", parent=self.root)
            else:
                cur.execute("Select * from product where Product_ID = ?", (self.var_productid.get(),))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror("Error", "Invalid Product", parent=self.root)
                else:
                    option_ask = messagebox.askyesno("Confirmation", "Do you really want to delete the product?",
                                                         parent=self.root)
                    if option_ask == True:
                        cur.execute("delete from product where Product_ID = ?", (self.var_productid.get(),))
                        conn.commit()
                        messagebox.showinfo("Deleted", "Product Deleted Successfully", parent=self.root)
                        self.clear_cmd()
        except Exception as ex:
                messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)


if __name__ == "__main__":
    root = Tk()
    obj = Product(root)
    root.mainloop()