#BEFORE RUNNING THE CODE MAKE SURE THAT - 

#YOU HAVE DOWNLOADED AND INSTALLED Connector/Python from MySQL Community Server Downloads on your OS

#YOU HAVE mysql.connector module
#    (if not then execute the following command on your Terminal/cmd : pip install mysql-connector-python

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector

class Register:

    def __init__(self, root):

        self.root = root
        self.root.title("Registration")
        self.root.geometry("600x470+400+200")
        self.root.resizable(False, False)

        Label(root, text="Python Registration Form", font="arial 25").pack(pady=50)

        Label(text="Name:", font=23).place(x=100,y=150)
        self.nameValue = StringVar()
        self.name = Entry(root, textvariable = self.nameValue, width = 30, bd=2, font = 20)
        self.name.place(x=200,y=150)

        Label(text="Phone no:", font=23).place(x=100,y=200)
        self.phoneValue = StringVar()
        self.phone = Entry(root, textvariable = self.phoneValue, width = 30, bd=2, font = 20)
        self.phone.place(x=200,y=200)

        Label(text="Gender:", font=23).place(x=100,y=250)
        self.genderValue = StringVar()
        self.gender = ttk.Combobox(root, textvariable = self.genderValue, width = 25, font = 20, state = "readonly")
        self.gender['values'] = ("Male", "Female", "Afzal(others)")
        self.gender.place(x=200,y=250)

        Label(text="E-mail:", font=23).place(x=100,y=300)
        self.emailValue = StringVar()
        self.email = Entry(root, textvariable = self.emailValue, width = 30, bd=2, font = 20)
        self.email.place(x=200,y=300)

        checkValue = IntVar
        checkbtn = Checkbutton(text="DO YOU AGREE THAT THE ENTERED INFORMATION IS CORRECT?", variable = checkValue)
        checkbtn.place(x=100,y=340)

        Button(root, text="Submit", font = 20, width = 11, height = 2, cursor = "hand1", command = self.register_data).place(x=250, y=380)

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

            cur.execute("INSERT INTO data (name, phone_no, gender, email) VALUES (%s, %s, %s, %s)",
                        (
                            self.name.get(),
                            self.phone.get(),
                            self.gender.get(),
                            self.email.get()
                        )
            )
            mydb.commit()
            mydb.close()
            messagebox.showinfo("Success", "Registration successful", parent=self.root)


root = Tk()
obj = Register(root)
root.mainloop()

#additions yet to implement
#show data in grid
#update from grid 
