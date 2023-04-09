import sqlite3
from tkinter import *


conn = sqlite3.connect('restaurant.db')


c = conn.cursor()


c.execute('''CREATE TABLE IF NOT EXISTS menu
            (id INTEGER PRIMARY KEY,
             name TEXT NOT NULL,
             code TEXT NOT NULL,
             quantity INTEGER NOT NULL,
             price INTEGER NOT NULL)''')


c.execute("INSERT INTO menu (name, code, quantity, price) VALUES ('Chicken Burger', 'CB01', 10, 200)")
c.execute("INSERT INTO menu (name, code, quantity, price) VALUES ('Veggie Burger', 'VB01', 15, 150)")
c.execute("INSERT INTO menu (name, code, quantity, price) VALUES ('French Fries', 'FF01', 20, 80)")
c.execute("INSERT INTO menu (name, code, quantity, price) VALUES ('Coke', 'CK01', 30, 40)")
c.execute("INSERT INTO menu (name, code, quantity, price) VALUES ('Ice Cream', 'IC01', 12, 100)")


conn.commit()


conn.close()


class RestaurantManagementSystem:
    def __init__(self, master):
        self.master = master
        self.master.title('Restaurant Management System')
        self.master.geometry('500x500')

        
        self.label1 = Label(self.master, text='Menu')
        self.label1.grid(row=0, column=0, pady=10, padx=10)

        self.label2 = Label(self.master, text='Order')
        self.label2.grid(row=0, column=2, pady=10, padx=10)

       
        self.menu_listbox = Listbox(self.master, width=30)
        self.menu_listbox.grid(row=1, column=0, padx=10)

        
        conn = sqlite3.connect('restaurant.db')
        c = conn.cursor()
        c.execute("SELECT name, code, quantity, price FROM menu")
        menu_items = c.fetchall()
        for item in menu_items:
            self.menu_listbox.insert(END, item)
        conn.close()

        
        self.quantity_entry = Entry(self.master, width=10)
        self.quantity_entry.grid(row=1, column=2, padx=10)

        self.quantity_label = Label(self.master, text='Quantity')
        self.quantity_label.grid(row=2, column=2)

        
        self.add_order_button = Button(self.master, text='Add Order', command=self.add_order)
        self.add_order_button.grid(row=3, column=2, pady=10)

        
        self.order_listbox = Listbox(self.master, width=30)
        self.order_listbox.grid(row=1, column=3, padx=10)

       
        self.generate_bill_button = Button(self.master, text='Generate Bill', command=self.generate_bill)
        self.generate_bill_button.grid(row=3, column=3, pady=10)

        
        self.total_cost_label = Label(self.master, text='Total Cost: ')
        self.total_cost_label.grid(row=4, column=3)

        
        self.order_list = []
        self.total_cost = 0

    def add_order(self):
