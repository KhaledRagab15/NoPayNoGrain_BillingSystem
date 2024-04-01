from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk, messagebox
import sqlite3
import os

class Sales:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1100x500+220+130")
        self.root.title("Rice Retailing Billing System")
        self.root.config(bg = "white")
        self.root.focus_force()
        self.root.resizable(0,0)

        self.bill_List = []

        #========Variables========#
        self.var_invoice = StringVar()


        #========Title========#
        lbl_title = Label(self.root, text="View Customer Bills", font=("times new roman", 27, "bold"),
                    bg="#828c51", fg="white", bd = 3, relief = RIDGE)
        lbl_title.pack(side = TOP, fill = X)

        lbl_invoice = Label(self.root, text = "Invoice No.", font=("times new roman", 13),
                    bg="white")
        lbl_invoice.place(x = 50, y = 100)

        txt_invoice = Entry(self.root, textvariable= self.var_invoice, font=("times new roman", 13),
                        bg="white")
        txt_invoice.place(x=160, y=100, width = 170, height = 27)

        #========Buttons========#
        btn_search = Button(self.root, text = "Search", command = self.search_cmd, bg="#4caf50", font=("Times New Roman", 13),
                            cursor="hand2", fg="white")
        btn_search.place(x = 360, y = 100, width = 120, height = 27)
        btn_clear = Button(self.root, command = self.clear, text="Clear", bg="#808080", font=("Times New Roman", 13),
                            cursor="hand2", fg="white")
        btn_clear.place(x=490, y=100, width=120, height=27)

        #========Bill_List_Frame========#
        sales_Frame = Frame(self.root, bd = 3, relief = RIDGE)
        sales_Frame.place(x = 50, y = 140, width = 200, height = 330)

        scrolly = Scrollbar(sales_Frame, orient = VERTICAL)
        self.sales_List = Listbox(sales_Frame, font = ("times new roman", 14), bg = "white", yscrollcommand= scrolly.set)
        scrolly.config(command = self.sales_List.yview)
        scrolly.pack(side = RIGHT, fill = Y)
        self.sales_List.pack(fill = BOTH, expand = 1)
        self.sales_List.bind("<ButtonRelease-1>", self.get_Data)

        #========Bill_Area========#
        bill_Frame = Frame(self.root, bd = 3, relief = RIDGE)
        bill_Frame.place(x = 280, y = 140, width = 420, height = 330)

        lbl_title2 = Label(bill_Frame, text="Customer Bill Area", font=("times new roman", 20, "bold"),
                          bg="#A6C36F")
        lbl_title2.pack(side=TOP, fill=X)

        scrolly2 = Scrollbar(bill_Frame, orient=VERTICAL)
        self.bill_Area = Text(bill_Frame, font=("times new roman", 14), yscrollcommand= scrolly2.set)
        scrolly2.config(command=self.sales_List.yview)
        scrolly2.pack(side=RIGHT, fill=Y)
        self.bill_Area.pack(fill=BOTH, expand=1)

        #=========Image==========#
        self.image1 = Image.open("img/sales.png")
        self.image1 = self.image1.resize((450, 300), Image.LANCZOS)
        self.image1 = ImageTk.PhotoImage(self.image1)

        self.label_image1 = Label(self.root, image=self.image1,
                                  bd=0, relief=RAISED)
        self.label_image1.place(x=700, y=110)

        self.show()
    #=============================================================
    def show(self):
        del self.bill_List[:]
        self.sales_List.delete(0, END)
        #print(os.listdir("../BillSystem"))
        for i in os.listdir('bill'):
            if i.split(".")[-1] == "txt":
                self.sales_List.insert(END, i)
                self.bill_List.append(i.split(".")[0])

    def get_Data(self, ev):
        index_= self.sales_List.curselection()
        file_Name = self.sales_List.get(index_)
        print(file_Name)
        self.bill_Area.delete("1.0", END)
        open_File = open(f'bill/{file_Name}', 'r')
        for i in open_File:
            self.bill_Area.insert(END, i)
        open_File.close()

    def search_cmd(self):
        if self.var_invoice.get() == "":
            messagebox.showerror("Error", "Invoice No. should be required", parent = self.root)
        else:
            if self.var_invoice.get() in self.bill_List:
                open_File = open(f"bill/{self.var_invoice.get()}.txt","r")
                self.bill_Area.delete("1.0", END)
                for i in open_File:
                    self.bill_Area.insert(END, i)
                open_File.close()
            else:
                messagebox.showerror("Error", "Invalid Invoice No.", parent=self.root)

    def clear(self):
        self.show()
        self.bill_Area.delete("1.0", END)




if __name__ == "__main__":
    root = Tk()
    obj = Sales(root)
    root.mainloop()