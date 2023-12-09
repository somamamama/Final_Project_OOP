import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import mysql.connector
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
from mysql.connector import Error
import customtkinter


class Dashboard:
    def __init__(self,username):
        self.username = username
        customtkinter.set_appearance_mode("light") # Set the appearance mode using the customtkinter module
        self.root = customtkinter.CTk() # Create the main Tkinter window
        self.root.title("Sales Calculator")
        self.root.geometry('1407x780')
        self.root.iconbitmap("E:/user/Desktop/School things/PYTHON FINAL PROJECT/FSP_NEW(2)/coffee-cup.ico")

        self.products = {}  # Initialize variables to store product data and totals
        self.profit = 0
        self.total_cost = 0
        
        try:
            # Connect to MySQL database
            self.connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password='',
                database="FSP_DATA",
                port='3307'
            )

            if self.connection.is_connected():
                print("Connected to MySQL")
                
        except Error as e:
            print(f"Error: {e}")

         # Create main frame
        self.main_frame = customtkinter.CTkFrame(master=self.root, fg_color="#FFFFFF",bg_color="#FFFFFF")
        self.main_frame.pack(expand=1, fill="both")

        # Create frames for each "page"
        self.page_sales = customtkinter.CTkFrame(master=self.main_frame)
        self.page_graph = customtkinter.CTkFrame(master=self.main_frame)

        # Create widgets for Home page
        # Create widgets for Home page

        self.listbox = tk.Listbox(self.page_sales, width=70, height=20, bd=2)
        self.listbox.place(x= 60, y= 70)
        
        
        
        self.navsales_frame = customtkinter.CTkFrame(self.page_sales, fg_color="#FFFFFF",width=1000, height=291)
        self.navsales_frame.place(x=125, y=470)
        self.navsales_frame.pack_propagate(False) 
        # Create widgets for Sales page
        self.label_product = customtkinter.CTkLabel(master=self.navsales_frame, text="Product:", font=('Garamond', 19), text_color="#000000")
        self.label_quantity = customtkinter.CTkLabel(master=self.navsales_frame, text="Quantity:", font=('Garamond', 19), text_color="#000000")
        self.label_price = customtkinter.CTkLabel(master=self.navsales_frame, text="Price:", font=('Garamond', 19), text_color="#000000")
        self.label_cost = customtkinter.CTkLabel(master=self.navsales_frame, text="Cost:", font=('Garamond', 19), text_color="#000000")
        self.entry_product = customtkinter.CTkEntry(master=self.navsales_frame, width=200,fg_color="#FFFFFF",text_color="#000000",border_color="#000000", placeholder_text="Enter product",  font=('Rockwell', 17))
        self.entry_quantity = customtkinter.CTkEntry(master=self.navsales_frame, width=200,fg_color="#FFFFFF",text_color="#000000",border_color="#000000", placeholder_text="Enter quantity",  font=('Rockwell', 17))
        self.entry_price = customtkinter.CTkEntry(master=self.navsales_frame, width=200,fg_color="#FFFFFF",text_color="#000000",border_color="#000000", placeholder_text="Enter price",  font=('Rockwell', 17))
        self.entry_cost = customtkinter.CTkEntry(master=self.navsales_frame, width=200,fg_color="#FFFFFF",text_color="#000000",border_color="#000000", placeholder_text="Enter cost",  font=('Rockwell', 17))
        self.btn_add_product = customtkinter.CTkButton(master=self.navsales_frame, text="Add Product",corner_radius=20, hover_color="#5FACF0", command=self.add_product)
        self.btn_delete_product = customtkinter.CTkButton(master=self.navsales_frame,fg_color="#0857FF", corner_radius=20, hover_color="#5FACF0", text="Delete Product", command=self.delete_product)
        self.btn_calculate = customtkinter.CTkButton(master=self.navsales_frame,fg_color="#0857FF", corner_radius=20, hover_color="#5FACF0", text="Calculate", command=self.calculate_total_cost_and_profit)
        self.btn_reset = customtkinter.CTkButton(master=self.navsales_frame,fg_color="#0857FF", corner_radius=20, hover_color="#5FACF0", text="Reset Data", command=self.reset_data)
        
        

        self.label_product.place(x=80, y=15)
        self.label_quantity.place(x=600, y=15)
        self.label_price.place(x=330, y=15)
        self.label_cost.place(x=855, y=15)
        self.entry_product.place(x=20, y=55)
        self.entry_quantity.place(x=270, y=55)
        self.entry_price.place(x=530, y=55)
        self.entry_cost.place(x= 780, y=55)
        self.btn_add_product.place(x=37, y=115)
        self.btn_delete_product.place(x=820, y=115)
        self.btn_calculate.place(x= 290, y=115)
        self.btn_reset.place(x=555, y=115)

        # Create widgets for Graph page
        self.welcome_graph = customtkinter.CTkLabel(master=self.page_graph,text="Welcome to Sales Calculator!", font=('Garamond', 25, 'bold'), text_color="#171D2E")
        self.welcome_graph.pack(pady=20)
        self.btn_show_chart = customtkinter.CTkButton(master=self.page_graph,fg_color="#0857FF", corner_radius=20, hover_color="#5FACF0", text="Show Chart", command=self.show_chart)
        self.btn_show_chart.pack(side="bottom",pady=10)

        # Create widgets for navigation bar
        self.nav_frame = customtkinter.CTkFrame(master=self.main_frame, fg_color="#C0943C",width=166, height=515)
        self.nav_frame.pack(side=tk.LEFT, fill="y")
        self.nav_frame.pack_propagate(False)  # Prevent navigation frame from propagating its size to children


        self.btn_sales = customtkinter.CTkButton(master=self.nav_frame, text="Sales", font=('Rockwell', 24), fg_color="#C0943C", text_color="#FFFFFF", hover_color="#C0943C", command=lambda: self.show_page(self.page_sales))
        self.btn_graph = customtkinter.CTkButton(master=self.nav_frame, text="Graph", font=('Rockwell', 24), fg_color="#C0943C", text_color="#FFFFFF", hover_color="#C0943C", command=lambda: self.show_page(self.page_graph))
        self.btn_exit = customtkinter.CTkButton(master=self.nav_frame, text="Exit", font=('Rockwell', 24), fg_color="#C0943C", text_color="#FFFFFF", hover_color="#C0943C", command=self.root.destroy)


        self.btn_sales.place(x= 10, y= 100)
        self.btn_graph.place(x= 10, y= 350)
        self.btn_exit.place(x= 10, y= 700)

        

        # Create listbox for displaying added products, total cost, and total profit
        self.listbox_totals = tk.Listbox(self.page_sales, width=70, height=20)
        self.listbox_totals.place(x= 750, y= 70)

        # Initial display
        self.update_listbox()

        # Run the Tkinter main loop
        self.root.mainloop()

    def show_page(self, page):
        # Hide all pages and then show the specified page
        self.page_sales.pack_forget()
        self.page_graph.pack_forget()
        page.pack(expand=1, fill="both")
        
    
    def add_product(self):
        try:
         product = self.entry_product.get() # Get input values from entry widgets
         quantity = int(self.entry_quantity.get())
         price = float(self.entry_price.get())
         cost = quantity * price  # Assuming cost is calculated as quantity * price
        
         self.calculate_total_cost_and_profit() # Calculate total cost and profit and update the display
        
        # Update the listbox
         self.update_listbox()

    # Call the modified add_product_to_database method with the actual parameters
         self.add_product_to_database(product, quantity, price, cost)
    
    # Clearing entries and updating the listbox can be done after displaying the product
         self.clear_entries()
         self.update_totals_listbox()
        
        except ValueError:
         # Handle invalid input
         messagebox.showerror("Error", "Invalid input. Please enter a valid quantity, cost, and price.")
         self.quantity_entry.delete(0, 'end')
         self.cost_entry.delete(0, 'end')
         self.price_entry.delete(0, 'end')
  

    def add_product_to_database(self,product,quantity,price,cost):
        
      try:
        # Insert data into MySQL
        cursor = self.connection.cursor()
        query = "INSERT INTO sales (product, quantity, price, cost) VALUES (%s, %s, %s, %s)"
        data = (product, quantity, price, cost)
        cursor.execute(query, data)
        self.connection.commit()
        print(f"Product {product} added to the database")

        # Update the local products dictionary
        if product in self.products:
            self.products[product]["quantity"] += quantity
        else:
            self.products[product] = {"quantity": quantity, "price": price, "cost": cost}

        # Call the method to calculate total cost and profit
        self.calculate_total_cost_and_profit()

        # Display the added product in the listbox
        self.listbox.insert(tk.END, f"{product}: {quantity} units x ${price} each (Cost: ${cost:.2f})")

        # Update the listbox with all products and totals
        self.update_listbox()

      except Error as e:
        print(f"Error: {e}")

        if product and quantity > 0 and price > 0 and cost >= 0:
            if product in self.products:
                self.products[product]["quantity"] += quantity
            else:
                self.products[product] = {"quantity": quantity, "price": price, "cost": cost}
                self.listbox.insert(tk.END, f"{product} - Quantity: {quantity}, Price: ${price:.2f}, Cost: ${cost:.2f}")
            messagebox.showinfo("Success", "Product added successfully.")
            self.clear_entries()
        else:
            messagebox.showerror("Error", "Invalid input. Please enter valid values.")

    def delete_product(self):
        
        selected_item = self.listbox.curselection()
        if not selected_item:
            self.show_warning("Please select a product to delete.")
            return

        product = self.listbox.get(selected_item[0]).split(":")[0].strip()

        # Delete the product from the database
        self.delete_product_from_database(product)

        # Update the local products dictionary and refresh the listbox
        if product in self.products:
            del self.products[product]
            self.update_listbox()
            self.calculate_total_cost_and_profit()

        product = self.listbox.get(selected_item[0]).split(":")[0].strip()

        # Call the modified delete_product method with the actual parameter
        self.delete_product_from_database(product)
        self.clear_entries()
        self.update_listbox()
        self.calculate_total_cost_and_profit()
        self.update_totals_listbox()
    
    def delete_product_from_database(self, product):
        try:
            # Delete data from MySQL
            cursor = self.connection.cursor()
            query = "DELETE FROM sales WHERE product = %s"
            data = (product,)
            cursor.execute(query, data)
            self.connection.commit()
            print(f"Product {product} deleted from the database")
        except Error as e:
            print(f"Error: {e}")
        
    
    
    def reset_data(self):
        confirmation = messagebox.askyesno("Confirmation", "Are you sure you want to reset all data?")
        if confirmation:
            try:
                cursor = self.connection.cursor()
                # Delete all data from the 'sales' table
                query = "DELETE FROM sales"
                cursor.execute(query)
                self.connection.commit()
                print("All data reset")
            except Error as e:
                print(f"Error: {e}")

            # Clear local data and update the listbox
            self.products = {}
            self.update_listbox()
            self.calculate_total_cost_and_profit()
            self.show_chart()  # Update the chart after resetting data
            # Clear the listbox in the Sales page
            self.listbox.delete(0, tk.END)
            self.update_totals_listbox()        

    def calculate_total_cost_and_profit(self):
     self.total_cost = sum(item["quantity"] * item["cost"] for item in self.products.values())
     self.profit = sum(item["quantity"] * (item["price"] - item["cost"]) for item in self.products.values())

     self.update_listbox()
     self.update_totals_listbox()

    # Show total cost and profit using messagebox
     messagebox.showinfo("Total Cost and Profit", f"Total Cost: P{self.total_cost:.2f}\nTotal Profit: P{self.profit:.2f}")

    # Check if total cost is greater than total selling price and show warning message
     if self.total_cost > self.profit:
        messagebox.showwarning("Warning", "The total cost of the products is greater than their total selling price. Please adjust the prices and costs accordingly.")

    def show_chart(self):
        if not self.products:
            self.show_warning("No products added. Add products to generate a chart.")
            return

        labels = list(self.products.keys())
        values = [item["quantity"] * (item["price"] - item["cost"]) for item in self.products.values()]

        fig, ax = plt.subplots()
        ax.plot(labels, values, marker='o', linestyle='-', color='b')
        ax.set_xlabel('Products')
        ax.set_ylabel('Profit per Product')
        ax.set_title('Sales Line Chart')

        chart_canvas = FigureCanvasTkAgg(fig, self.page_graph)
        chart_canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        chart_canvas.draw()
        


    def show_warning(self, message):
        tk.messagebox.showwarning("Warning", message)

    def clear_entries(self):
        # Implementation remains the same
        self.entry_product.delete(0, tk.END)
        self.entry_quantity.delete(0, tk.END)
        self.entry_price.delete(0, tk.END)
        self.entry_cost.delete(0, tk.END)
    
    def update_totals_listbox(self):
    # Clear the totals listbox
     self.listbox_totals.delete(0, tk.END)

    # Display total cost and total profit in the totals listbox
     self.listbox_totals.insert(tk.END, f"Total Cost: P{self.total_cost:.2f}")
     self.listbox_totals.insert(tk.END, f"Total Profit: P{self.profit:.2f}")

    def update_listbox(self):
    # Clear the product listbox
        self.listbox.delete(0, tk.END)

    # Display added products
        for product, (price, quantity, cost) in self.products.items():
         self.listbox.insert(tk.END, f"{product}: {quantity} units x ${price} each (Cost: ${cost})")

        try:
           cursor = self.connection.cursor()
           query = "SELECT product, quantity, price, cost FROM sales"
           cursor.execute(query)
           records = cursor.fetchall()

           for record in records:
            self.listbox.insert(tk.END, f"{record[0]}: {record[1]} units x ${record[2]} each (Cost: ${record[3]})")

        # Display total cost and total profit in the product listbox
           self.listbox.insert(tk.END, f"Total Cost: P{self.total_cost:.2f}")
           self.listbox.insert(tk.END, f"Total Profit: P{self.profit:.2f}")
        
        except Error as e:
         print(f"Error: {e}")

    # Clear the totals listbox
        self.listbox_totals.delete(0, tk.END)

    # Display total cost and total profit in the totals listbox
        self.listbox_totals.insert(tk.END, f"Total Cost: P{self.total_cost:.2f}")
        self.listbox_totals.insert(tk.END, f"Total Profit: P{self.profit:.2f}")
              
        
    def open_dashboard(self):
    # Run Tkinter main loop
        self.root.mainloop()

if __name__ == "__main__":
    app = Dashboard()
    app.open_dashboard()