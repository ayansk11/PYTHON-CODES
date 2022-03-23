
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter
import mysql.connector

class Register:

    def __init__(self, root):

        self.root = root
        self.root.title("Registration")
        self.root.geometry("800x770+350+60")
        self.root.resizable(False, False)

        Label(root, text="Python Registration Form", font="arial 25").pack(pady=50)

        Label(text="Name:", font=23).place(x=200,y=400)
        self.nameValue = StringVar()
        self.name = Entry(root, textvariable = self.nameValue, width = 30, bd=2, font = 20)
        self.name.place(x=300,y=400)

        Label(text="Phone no:", font=23).place(x=200,y=450)
        self.phoneValue = StringVar()
        self.phone = Entry(root, textvariable = self.phoneValue, width = 30, bd=2, font = 20)
        self.phone.place(x=300,y=450)

        Label(text="Gender:", font=23).place(x=200,y=500)
        self.genderValue = StringVar()
        self.gender = ttk.Combobox(root, textvariable = self.genderValue, width = 25, font = 20, state = "readonly")
        self.gender['values'] = ("Male", "Female", "(others)")
        self.gender.place(x=300,y=500)

        Label(text="E-mail:", font=23).place(x=200,y=550)
        self.emailValue = StringVar()
        self.email = Entry(root, textvariable = self.emailValue, width = 30, bd=2, font = 20)
        self.email.place(x=300,y=550)

        checkValue = IntVar
        checkbtn = Checkbutton(text="DO YOU AGREE THAT THE ENTERED INFORMATION IS CORRECT?", variable = checkValue)
        checkbtn.place(x=200,y=600)

        Label(text="Enter the C_id", font=23).place(x=660,y=650)
        self.id_value = StringVar()
        self.id = Entry(root, textvariable = self.id_value, width = 5, bd = 2, font = 20)
        self.id.place(x=590,y=650)

        Button(root, text="Submit", font = 20, width = 11, height = 2, cursor = "hand1", command = lambda: [self.register_data(), self.delete_entry()]).place(x=350, y=670)
        Button(root, text="Delete", font = 20, width = 11, height = 2, cursor = "hand1", command = lambda: [self.delete_row()]).place(x=600, y=700)
        Button(root, text="View Data", font = 20, width = 11, height = 2, cursor = "hand1", command = lambda: [self.view_data()]).place(x=120, y=700)



    def register_data(self):

        if self.name.get()=="" or self.phone.get()=="" or self.email.get()=="" or self.gender.get()=="":

            messagebox.showerror("Error", "ALL FIELDS ARE REQUIRED", parent=self.root)

        else:

            mydb = mysql.connector.connect(host= "localhost", user="root",passwd="root@321", database="gui")
            cur = mydb.cursor()
            #cur.execute("select * from data where phone_no = %s", self.phone.get())
            #row = cur.fetchone()
            #if row!=None:
            #    
            #    messagebox.showerror("Error", "USER ALREADY EXISTS, PLEASE TRY WITH A DIFFERENT PHONE NO AND EMAIL", parent=self.root)
            #
            #else:

            self.sp_insert(cur)

            mydb.commit()
            mydb.close()

            messagebox.showinfo("Success", "Registration successful", parent=self.root)




    def view_data(self):

        mydb = mysql.connector.connect(host= "localhost", user="root",passwd="root@321", database="gui")
        cur = mydb.cursor()
        self.sp_view_data(cur)
        rows = cur.fetchall()


        tree_view = ttk.Treeview(self.root, columns = (1,2,3,4,5), show = "headings", height = "10")
        ybar=tkinter.Scrollbar(self.root, orient = tkinter.VERTICAL, command = tree_view.yview)
        tree_view.configure(yscroll = ybar.set)

        tree_view.column(1, stretch = NO, width = 40)
        tree_view.heading(1, text = "C_ID")
        
        tree_view.column(2, stretch = NO, width = 200)
        tree_view.heading(2, anchor = CENTER, text = "Name")

        tree_view.column(3, stretch = NO, width = 150)
        tree_view.heading(3, anchor = CENTER, text = "Phone No")

        tree_view.column(4, stretch = NO, width = 80)
        tree_view.heading(4, anchor = CENTER, text = "Gender")

        tree_view.column(5, stretch = NO, width = 200)
        tree_view.heading(5, anchor = CENTER, text = "E-mail")

        tree_view.pack()

        for i in rows:

            tree_view.insert("", "end", values = i)



    def delete_entry(self):

        self.name.delete(0, END)
        self.phone.delete(0, END)
        self.gender.delete(0, END)
        self.email.delete(0, END)



    def delete_row(self):
    
        if self.id.get() == "":

            messagebox.showerror("Error", "Enter C_ID to delete", parent=self.root)

        else:

            mydb = mysql.connector.connect(host= "localhost", user="root",passwd="root@321", database="gui")
            cur = mydb.cursor()
            
            self.sp_delete_row(cur)

            mydb.commit()
            mydb.close()
            self.id.delete(0, END)
            messagebox.showinfo("Success", "Record deleted successfully", parent=self.root)




    def sp_insert(self, cur):

        cur.execute("INSERT INTO data (name, phone_no, gender, email) VALUES (%s, %s, %s, %s)",
                        (
                            self.name.get(),
                            self.phone.get(),
                            self.gender.get(),
                            self.email.get()
                        )
            )

    
    def sp_view_data(self, cur):

        cur.execute("select * from data")


    def sp_delete_row(self, cur):

        cur.execute("delete from data where c_id = '"+ self.id.get() +"'")



root = Tk()
obj = Register(root)
root.mainloop()

