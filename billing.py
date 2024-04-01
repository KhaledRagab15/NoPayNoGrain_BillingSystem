from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import sqlite3
from tkinter import ttk, messagebox
import time
import os
import tempfile

class Billing:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root.title("Rice Retailing Billing System")
        self.root.config(bg = "#A6C36F")

        self.cart_List = []
        self.check_print = 0

        #=======Variables==========#
        self.var_search = StringVar()
        self.var_productid = StringVar()
        self.var_bname = StringVar()
        self.var_type = StringVar()
        self.var_price = StringVar()
        self.var_kilos = StringVar()
        self.var_stock = StringVar()
        self.var_cname = StringVar()
        self.var_cal_input = StringVar()
        self.var_contact = StringVar()




        #==========Icon==========#
        self.icon_title = PhotoImage(file="img/ricewhite.png")

        #==========Title==========#
        title = Label(self.root, text="No Pay No Grain Billing System",
                  font=("Times New Roman", 35, "bold"), image = self.icon_title,
                  bg="#1E352F", fg="white", anchor="w",
                  padx=20, compound=LEFT)
        title.place(x=0, y=0, relwidth=1, height=70)

    #==========Logout_Button==========#
        logout_btn = Button(self.root, text="Logout", command = self.logout
                        , font=("times new roman", 15, "bold"),
                        bg="lightgray", cursor="hand2")
        logout_btn.place(x=1180, y=10, width=150)

    #==========Clock==========#
        self.clock_lbl = Label(self.root, text="Date: DD-MM-YYYY\t\t Time: HH:MM:SS",
                           font=("Times New Roman", 15)
                           , bg="#828C51", fg="white", anchor="w")
        self.clock_lbl.place(x=0, y=70, relwidth=1, height=30)

    #========Product_Frame==========#
        product_Frame1 = Frame(self.root, bd = 4, relief = RIDGE, bg = "white")
        product_Frame1.place(x = 6, y = 110, width = 410, height = 550)

        product_Title = Label(product_Frame1, text = "All Products", font = ("times new roman", 18, "bold"),
                              bg = "#335145", fg = "white")
        product_Title.pack(side = TOP, fill = X)

        #========Product_search_Frame==========#
        product_Frame2 = Frame(product_Frame1, bd=2, relief=RIDGE, bg="white")
        product_Frame2.place(x=2, y=42, width=398, height=90)

        lbl_Search = Label(product_Frame2, text = "Search brand by name", font = ("times new roman", 13, "bold"),
                           bg = "white", fg = "green")
        lbl_Search.place(x = 2, y = 5)

        lbl_name = Label(product_Frame2, text = "Brand Name", font = ("times new roman", 13, "bold"),
                           bg = "white")
        lbl_name.place(x=5, y=45)
        txt_name = Entry(product_Frame2, textvariable = self.var_search, font=("times new roman", 13, "bold"),
                         bg="lightyellow")
        txt_name.place(x=125, y=47, width = 160, height = 22)

        #==========Button==========#
        btn_Search = Button(product_Frame2, command = self.search_cmd, text = "Search", font = ("times new roman", 13), bg="#4caf50",
                            cursor = "hand2", fg = "white")
        btn_Search.place(x = 290, y = 47, height = 22, width = 90)
        btn_Showall = Button(product_Frame2, text="Show All", font=("times new roman", 13), bg="silver",
                            cursor="hand2")
        btn_Showall.place(x=290, y=10, width=90 , height = 25)

        product_Frame3 = Frame(product_Frame1, bd=3, relief=RIDGE)
        product_Frame3.place(x=2, y=138, width=396, height=375)

        vertical_Scroll = Scrollbar(product_Frame3, orient=VERTICAL)
        horizontal_Scroll = Scrollbar(product_Frame3, orient=HORIZONTAL)

        self.product_Table = ttk.Treeview(product_Frame3, columns=("Product_ID", "Type", "Name", "Price",
                                                                    "Kilos", "Status"),
                                           yscrollcommand=vertical_Scroll.set, xscrollcommand=horizontal_Scroll.set)
        horizontal_Scroll.pack(side=BOTTOM, fill=X)
        horizontal_Scroll.config(command=self.product_Table.xview)
        vertical_Scroll.pack(side=RIGHT, fill=Y)
        vertical_Scroll.config(command=self.product_Table.yview)

        self.product_Table.heading("Product_ID", text="PRODUCT ID")
        self.product_Table.heading("Type", text="TYPE")
        self.product_Table.heading("Name", text="BRAND NAME")
        self.product_Table.heading("Price", text="PRICE")
        self.product_Table.heading("Kilos", text="Kg/s")
        self.product_Table.heading("Status", text="STATUS")
        self.product_Table["show"] = "headings"

        self.product_Table.column("Product_ID", width=90)
        self.product_Table.column("Type", width=100)
        self.product_Table.column("Name", width=120)
        self.product_Table.column("Price", width=85)
        self.product_Table.column("Kilos", width=85)
        self.product_Table.column("Status", width=75)
        self.product_Table.pack(fill=BOTH, expand=1)
        self.product_Table.bind("<ButtonRelease-1>", self.get_Data)

        lbl_note = Label(product_Frame1, text = "Note: Enter 0 Kilo to remove product from billing", font = ("times new roman", 11),
                         bg = "white", fg = "red")
        lbl_note.pack(side = BOTTOM, fill = X)

    #========Customer_Frame==========#
        customer_Frame = Frame(self.root, bd=4, relief=RIDGE, bg="white")
        customer_Frame.place(x=420, y=110, width=550, height=70)

        customer_Title = Label(customer_Frame, text="Customer Details", font=("times new roman", 13),
                              bg="#BEEF9E")
        customer_Title.pack(side=TOP, fill=X)

        lbl_name = Label(customer_Frame, text = "Name", font = ("times new roman", 13, "bold"),
                           bg = "white")
        lbl_name.place(x=3, y=35)
        txt_name = Entry(customer_Frame, textvariable = self.var_cname, font=("times new roman", 13, "bold"),
                         bg="lightyellow")
        txt_name.place(x=70, y=35, width = 170, height = 22)

        lbl_contact = Label(customer_Frame, text="Contact", font=("times new roman", 13, "bold"),
                         bg="white")
        lbl_contact.place(x=290, y=35)
        txt_contact = Entry(customer_Frame, textvariable=self.var_contact, font=("times new roman", 13, "bold"),
                         bg="lightyellow")
        txt_contact.place(x=380, y=35, width=140, height= 22)

        #========cal_cart_Frame==========#
        cal_cart_Frame = Frame(self.root, bd=2, relief=RIDGE, bg="white")
        cal_cart_Frame.place(x=420, y=190, width=550, height=360)

        #========calculator_Frame==========#
        cal_Frame = Frame(cal_cart_Frame, bd=2, relief=RIDGE, bg="white")
        cal_Frame.place(x=5, y=10, width=270, height=300)

        self.txt_cal_input = Entry(cal_Frame, textvariable = self.var_cal_input, font = ("arial", 13, "bold"),
                                   width = 27, bd = 7, relief = GROOVE, state = "readonly", justify = RIGHT)
        self.txt_cal_input.grid(row = 0, columnspan = 4)
        btn_7 = Button(cal_Frame, text = 7, command = lambda:self.get_Input(7), font = ("arial", 15, "bold"), bd = 4,
                       width = 4, pady = 10)
        btn_7.grid(row = 1, column = 0)
        btn_8 = Button(cal_Frame, text=8, command = lambda:self.get_Input(8), font=("arial", 15, "bold"), bd=4,
                       width=4, pady=10)
        btn_8.grid(row=1, column=1)
        btn_9 = Button(cal_Frame, text=9, command = lambda:self.get_Input(9), font=("arial", 15, "bold"), bd=4,
                       width=4, pady=10)
        btn_9.grid(row=1, column=2)
        btn_Sum = Button(cal_Frame, text="+", command = lambda:self.get_Input("+"), font=("arial", 15, "bold"), bd=4,
                       width=4, pady=10)
        btn_Sum.grid(row=1, column=3)

        btn_4 = Button(cal_Frame, text=4, command = lambda:self.get_Input(4), font=("arial", 15, "bold"), bd=4,
                       width=4, pady=10)
        btn_4.grid(row=2, column=0)
        btn_5 = Button(cal_Frame, text=5, command = lambda:self.get_Input(5), font=("arial", 15, "bold"), bd=4,
                       width=4, pady=10)
        btn_5.grid(row=2, column=1)
        btn_6 = Button(cal_Frame, text=6, command = lambda:self.get_Input(6), font=("arial", 15, "bold"), bd=4,
                       width=4, pady=10)
        btn_6.grid(row=2, column=2)
        btn_subtract = Button(cal_Frame, text="-", command = lambda:self.get_Input("-"), font=("arial", 15, "bold"), bd=4,
                         width=4, pady=10)
        btn_subtract.grid(row=2, column=3)

        btn_1 = Button(cal_Frame, text=1,command = lambda:self.get_Input(1),  font=("arial", 15, "bold"), bd=4,
                       width=4, pady=10)
        btn_1.grid(row=3, column=0)
        btn_2 = Button(cal_Frame, text=2, command = lambda:self.get_Input(2), font=("arial", 15, "bold"), bd=4,
                       width=4, pady=10)
        btn_2.grid(row=3, column=1)
        btn_3 = Button(cal_Frame, text=3, command = lambda:self.get_Input(3), font=("arial", 15, "bold"), bd=4,
                       width=4, pady=10)
        btn_3.grid(row=3, column=2)
        btn_multiply = Button(cal_Frame, text="*", command = lambda:self.get_Input("*"), font=("arial", 15, "bold"), bd=4,
                              width=4, pady=10)
        btn_multiply.grid(row=3, column=3)

        btn_0 = Button(cal_Frame, text=0, command=lambda: self.get_Input(0), font=("arial", 15, "bold"), bd=4,
                       width=4, pady=10)
        btn_0.grid(row=4, column=0)
        btn_c = Button(cal_Frame, text="C", command = self.clear_cal_cmd, font=("arial", 15, "bold"), bd=4,
                       width=4, pady=10)
        btn_c.grid(row=4, column=1)
        btn_equal = Button(cal_Frame, text="=", command = self.perform_cal, font=("arial", 15, "bold"), bd=4,
                       width=4, pady=10)
        btn_equal.grid(row=4, column=2)
        btn_divide = Button(cal_Frame, text="/", command=lambda: self.get_Input("/"), font=("arial", 15, "bold"),
                              bd=4,
                              width=4, pady=10)
        btn_divide.grid(row=4, column=3)

        #========cart_Frame==========#
        cart_Frame = Frame(cal_cart_Frame, bd=3, relief=RIDGE)
        cart_Frame.place(x=290, y=8, width=248, height=342)
        self.cart_Title = Label(cart_Frame, text="Cart \t Total Product: 0", font=("times new roman", 13),
                               bg="#BEEF9E")
        self.cart_Title.pack(side=TOP, fill=X)

        vertical_Scroll = Scrollbar(cart_Frame, orient=VERTICAL)
        horizontal_Scroll = Scrollbar(cart_Frame, orient=HORIZONTAL)

        self.cart_Table = ttk.Treeview(cart_Frame, columns=("Product_ID", "Type", "Name", "Price",
                                                                   "Kilos"),
                                          yscrollcommand=vertical_Scroll.set, xscrollcommand=horizontal_Scroll.set)
        horizontal_Scroll.pack(side=BOTTOM, fill=X)
        horizontal_Scroll.config(command=self.cart_Table.xview)
        vertical_Scroll.pack(side=RIGHT, fill=Y)
        vertical_Scroll.config(command=self.cart_Table.yview)

        self.cart_Table.heading("Product_ID", text="PRODUCT ID")
        self.cart_Table.heading("Type", text="TYPE")
        self.cart_Table.heading("Name", text="BRAND NAME")
        self.cart_Table.heading("Price", text="PRICE")
        self.cart_Table.heading("Kilos", text="Kg/s")
        self.cart_Table["show"] = "headings"

        self.cart_Table.column("Product_ID", width=100)
        self.cart_Table.column("Type", width=100)
        self.cart_Table.column("Name", width=100)
        self.cart_Table.column("Price", width=60)
        self.cart_Table.column("Kilos", width=95)
        self.cart_Table.pack(fill=BOTH, expand=1)
        self.cart_Table.bind("<ButtonRelease-1>", self.get_Data_cart)

        #========Add_to_Cart_Widget_Frame==========#
        add_cart_Frame = Frame(self.root, bd=2, relief=RIDGE, bg="white")
        add_cart_Frame.place(x=420, y=550, width=550, height=110)

        b_lbl = Label(add_cart_Frame, text = "Brand Name", font = ("times new roman", 13),
                           bg = "white")
        b_lbl.place(x=5, y=5)
        b_txt = Entry(add_cart_Frame, textvariable = self.var_bname, font=("times new roman", 13),
                       bg="lightyellow", state = "readonly")
        b_txt.place(x=5, y=35, width = 140, height = 22)

        type_lbl = Label(add_cart_Frame, text="Type", font=("times new roman", 13),
                      bg="white")
        type_lbl.place(x=150, y=5)
        type_txt = Entry(add_cart_Frame, textvariable=self.var_type, font=("times new roman", 13),
                      bg="lightyellow", state="readonly")
        type_txt.place(x=150, y=35, width=150, height=22)

        price_lbl = Label(add_cart_Frame, text="Price Per Kilo", font=("times new roman", 13),
                      bg="white")
        price_lbl.place(x=310, y=5)
        price_txt = Entry(add_cart_Frame, textvariable=self.var_price, font=("times new roman", 13),
                      bg="lightyellow", state="readonly")
        price_txt.place(x=310, y=35, width=120, height=22)

        kilos_lbl = Label(add_cart_Frame, text="Kilo/s", font=("times new roman", 13),
                          bg="white")
        kilos_lbl.place(x=450, y=5)
        kilos_txt = Entry(add_cart_Frame, textvariable=self.var_kilos, font=("times new roman", 13),
                          bg="lightyellow")
        kilos_txt.place(x=450, y=35, width=80, height=22)

        stock_lbl = Label(add_cart_Frame, text="Stock Kg/s", font=("times new roman", 13),
                          bg="white")
        stock_lbl.place(x=5, y=70)
        stock_txt = Entry(add_cart_Frame, state = "readonly", textvariable=self.var_stock, font=("times new roman", 13),
                          bg="lightyellow")
        stock_txt.place(x=90, y=70, width=80, height=22)


        clear_cart_btn = Button(add_cart_Frame, command = self.clear_cart_cmd, text="Clear", font=("times new roman", 14, "bold"),
                            bg="lightgray", cursor="hand2")

        clear_cart_btn.place(x=180, y=70, width=150, height = 30)
        add_update_cart_btn = Button(add_cart_Frame, text="Add | Update", command = self.add_update_cart, font=("times new roman", 14, "bold"),
                                bg="#335145", fg = "white",cursor="hand2")
        add_update_cart_btn.place(x=360, y=70, width=150, height=30)

        #=======bill_area_Frame==========#
        bill_Frame = Frame(self.root, bd=2, relief=RIDGE, bg="white")
        bill_Frame.place(x=973, y=110, width=370, height=410)

        bill_Title = Label(bill_Frame, text="Customer Bill Area", font=("times new roman", 18, "bold"),
                           bg="#454B1B", fg="white")
        bill_Title.pack(side=TOP, fill=X)
        verticalscroll = Scrollbar(bill_Frame, orient = VERTICAL)
        verticalscroll.pack(side = RIGHT, fill = Y)

        self.txt_bill_area = Text(bill_Frame, yscrollcommand= verticalscroll.set)
        self.txt_bill_area.pack(fill = BOTH, expand = 1)
        verticalscroll.config(command = self.txt_bill_area.yview)

        #=======billing_buttons==========#
        bill_menu_Frame = Frame(self.root, bd=2, relief=RIDGE, bg="white")
        bill_menu_Frame.place(x=973, y=520, width=370, height=140)

        self.lbl_amount = Label(bill_menu_Frame, text = "Bill Amount \n₱[0]", font = ("times new roman", 13, "bold"),
                                bg = "#AFE1AF")
        self.lbl_amount.place(x = 2, y = 5, width = 363, height = 80)

        # print_Button = Button(bill_menu_Frame, command = self.print_bill, text="Print", font=("times new roman", 13, "bold"),
        #                         bg="#00FF7F")
        # print_Button.place(x=2, y=86, width = 120, height = 50)
        clear_Button = Button(bill_menu_Frame, command = self.clear_all_cmd, text="Clear All", font=("times new roman", 13, "bold"),
                              bg="#ECFFDC")
        clear_Button.place(x=2, y=86, width = 170, height = 50)

        generate_Button = Button(bill_menu_Frame, command = self.generate_Bill, text="Generate Bill", font=("times new roman", 13, "bold"),
                              bg="#40826D")
        generate_Button.place(x=195, y=86, width = 170, height = 50)

        # ==========Footer==========#
        footer_lbl = Label(self.root, text="RRBS - Rice Retailing Billing System by Group 9 (No Pay, No Grain)",
                           font=("Times New Roman", 13)
                           , bg="#828C51", fg="white")
        footer_lbl.pack(side=BOTTOM, fill=X)

        self.show()
        # self.bill_top()
        self.update_date_time()

        #========Functions==========#
    def get_Input(self, num):
        xnum = self.var_cal_input.get() + str(num)
        self.var_cal_input.set(xnum)

    def clear_cal_cmd(self):
        self.var_cal_input.set("")

    def perform_cal(self):
        result = self.var_cal_input.get()
        self.var_cal_input.set(eval(result))

    def show(self):
        conn = sqlite3.connect(database=r"billsystem.db")
        cur = conn.cursor()
        try:
            # self.product_Table = ttk.Treeview(product_Frame3, columns=("Product_ID", "Name", "Price",
            #                                                            "Kilos", "Status"),
            #                                   yscrollcommand=vertical_Scroll.set, xscrollcommand=horizontal_Scroll.set)
            cur.execute("select Product_ID, Type, Name, Price, Kilos, Status from product where STATUS = 'Active'")
            rows = cur.fetchall()
            self.product_Table.delete(*self.product_Table.get_children())
            for row in rows:
                self.product_Table.insert("", END, values=row)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)

    def search_cmd(self):
        conn = sqlite3.connect(database=r"billsystem.db")
        cur = conn.cursor()
        try:
            if self.var_search.get() == "Select":
                messagebox.showerror("Error", "Select Search by option", parent=self.root)
            else:
                cur.execute(
                    "select Product_ID, Type, Name, Price, Kilos, Status from product where Name LIKE '%" + self.var_search.get() + "%'")
                rows = cur.fetchall()
                if len(rows) != 0:
                    self.product_Table.delete(*self.product_Table.get_children())
                    for row in rows:
                        self.product_Table.insert("", END, values=row)
                else:
                    messagebox.showerror("Error", "No record found!", parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)

    def get_Data(self, ev):
        f = self.product_Table.focus()
        data_content = (self.product_Table.item(f))
        row = data_content["values"]
        self.var_productid.set(row[0])
        self.var_type.set(row[1])
        self.var_bname.set(row[2])
        self.var_price.set(row[3])
        self.var_stock.set(row[4])
        self.var_kilos.set("1")


    def get_Data_cart(self, ev):
        f = self.cart_Table.focus()
        data_content = (self.cart_Table.item(f))
        row = data_content["values"]
        self.var_productid.set(row[0])
        self.var_type.set(row[1])
        self.var_bname.set(row[2])
        self.var_price.set(row[3])
        self.var_kilos.set(row[4])
        self.var_stock.set(row[5])


    def add_update_cart(self):
        if self.var_productid.get() == "":
            messagebox.showerror("Error", "Please select product from list", parent = self.root)
        elif self.var_kilos.get() == "":
            messagebox.showerror("Error", "Kilo/s is/are Required", parent = self.root)
        elif int(self.var_kilos.get())>int(self.var_stock.get()):
            messagebox.showerror("Error", "Invalid Kilo/s", parent=self.root)
        else:
            # price_cal = int(self.var_kilos.get()) * float(self.var_price.get())
            # price_cal = float(price_cal)
            price_cal = self.var_price.get()
            cart_data = [self.var_productid.get(), self.var_type.get(), self.var_bname.get(), price_cal, self.var_kilos.get(), self.var_stock.get()]


            #========update_cart==========#
            present = "no"
            index_ = 0
            for row in self.cart_List:
                if self.var_productid.get() == row[0]:
                    present = "yes"
                    break
                index_ += 1
            if present == "yes":
                op = messagebox.askyesno("Confirm", "Product already present \n Do you want to Update | Remove from cart?", parent = self.root)
                if op == True:
                    if self.var_kilos.get() == "0":
                        self.cart_List.pop(index_)
                    else:
                        # self.cart_List[index_][3]= price_cal #price
                        self.cart_List[index_][4]= self.var_kilos.get() #kilos
            else:
                self.cart_List.append(cart_data)

            self.show_cart()
            self.bill_updates()


    def bill_updates(self):
        self.bill_amount = 0
        for row in self.cart_List:
            self.bill_amount = self.bill_amount + (float(row[3])*int(row[4]))

        self.lbl_amount.config(text = f"Bill Amount \n₱ {str(self.bill_amount)}")
        self.cart_Title.config(text=f"Cart \t Total Product: {str(len(self.cart_List))}")


    def show_cart(self):
        try:
            self.cart_Table.delete(*self.cart_Table.get_children())
            for row in self.cart_List:
                 self.cart_Table.insert("", END, values=row)
        except Exception as ex:
                messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)

    def generate_Bill(self):
        if self.var_cname.get() == "" or self.var_contact.get() == "":
            messagebox.showerror("Error", f"Customer Details are required", parent=self.root)
        elif len(self.cart_List) == 0:
            messagebox.showerror("Error", f"Please add product to cart", parent = self.root)
        else:
            self.bill_top()
            self.bill_middle()
            self.bill_bottom()

            open_File = open(f"bill/{str(self.invoice)}.txt", "w", encoding = "utf-8")
            open_File.write(self.txt_bill_area.get("1.0", END))
            open_File.close()
            messagebox.showinfo("Saved", "Bill has been generated", parent = self.root)
            self.check_print = 1

    def bill_top(self):
        self.invoice = int(time.strftime("%H%M%S")) + int(time.strftime(("%d%m%Y")))
        bill_top_temp = f"""
\tNo Pay No Grain Rice Retailing

{str("="*43)}
Customer Name : {self.var_cname.get()}
Contact No. : {self.var_contact.get()}
Bill No. {str(self.invoice)}\t\t\tDate : {str(time.strftime("%d/%m/%Y"))}
{str("="*43)}
Type\tBrand Name\t\tKilos\tPrice
{str("="*43)} 
        """
        self.txt_bill_area.delete("1.0", END)
        self.txt_bill_area.insert('1.0', bill_top_temp)

    def bill_middle(self):
        conn = sqlite3.connect(database=r"billsystem.db")
        cur = conn.cursor()
        try:
            for row in self.cart_List:
                productid = row[0]
                type = row[1]
                name = row[2]
                kilos = (str(int(row[5])-int(row[4])))

                if kilos == int(row[5]):
                    status = "Inactive"
                if kilos != int(row[5]):
                    status = "Active"

                price = float(row[3]) * int(row[4])
                price = str(price)

                self.txt_bill_area.insert(END, "\n"+type+"\t"+name+"\t\t"+row[4]+"\t₱"+price)
                cur.execute("Update product set Kilos = ?, Status = ? where Product_ID = ?",(
                                kilos,
                                status,
                                productid
                ))
                conn.commit()
            conn.close()

            self.show()

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)

    def bill_bottom(self):
        bill_bottom_temp = f"""
{str("="*43)}
Bill Amount\t\t\t\t₱{self.bill_amount}
{str("="*43)}\n
        """
        self.txt_bill_area.insert(END, bill_bottom_temp)

    def clear_cart_cmd(self):
        self.var_productid.set("")
        self.var_type.set("")
        self.var_bname.set("")
        self.var_price.set("")
        self.var_kilos.set("")
        self.var_stock.set("")

    def clear_all_cmd(self):
        del self.cart_List[:]
        self.var_cname.set("")
        self.var_contact.set("")
        self.txt_bill_area.delete("1.0", END)
        self.cart_Title.config( text="Cart \t Total Product: 0")
        self.var_search.set("")
        self.clear_cart_cmd()
        self.show()
        self.show_cart()


    def update_date_time(self):
        time_ = time.strftime("%I:%M:%S")
        date_ = time.strftime("%d/%m/%Y")
        self.clock_lbl.config(text=f"Date: {str(date_)}\t\t Time: {str(time_)}")
        self.clock_lbl.after(200, self.update_date_time)

    # def print_bill(self):
    #     if self.check_print == 1:
    #         messagebox.showinfo("Print", "Please wait while printing", parent = self.root)
    #         new_file = tempfile.mkdtemp(".txt")
    #         new_file = open(new_file, "w").write(self.txt_bill_area.get("1.0", END), encoding = "utf-8")
    #         os.startfile(new_file, "print")
    #         # open_File = open(f"bill/{str(self.invoice)}.txt", "w", encoding="utf-8")
    #         # open_File.write(self.txt_bill_area.get("1.0", END))
    #         # open_File.close()
    #     else:
    #         messagebox.showinfo("Print", "Please generate bill to print receipt", parent=self.root)

    def logout(self):
        self.root.destroy()
        os.system("python login.py")




if __name__ == "__main__":
    root = Tk()
    obj = Billing(root)
    root.mainloop()