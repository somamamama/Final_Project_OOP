import tkinter as tk
import mysql.connector
from sign_up import *# Import the Signup class from the signup program
from dashboard import Dashboard
from tkinter import *
import customtkinter
from PIL import Image, ImageTk
from tkinter import messagebox

class Login:
    def __init__(self):
        customtkinter.set_appearance_mode("light")
        self.login_window = customtkinter.CTk()
        self.login_window.title("Login")
        self.login_window.iconbitmap("E:/user/Desktop/School things/PYTHON FINAL PROJECT/FSP_NEW(2)/coffee-cup.ico")
        self.login_window.geometry('1407x780')
        self.login_window.resizable(False,False)
        
                
        pil_image = Image.open("loginbg.jpg")

        # Convert the PIL Image to a Tkinter PhotoImage
        self.image = ImageTk.PhotoImage(pil_image)

        # Create a Label widget to display the image
        self.image_label = tk.Label(self.login_window, image=self.image)
        self.image_label.pack()

        
        # Create GUI components
       
        frame_login = customtkinter.CTkFrame(master=self.login_window,width=444,height=384,fg_color="#FFFFFF")
        frame_login.place(relx=0.5, rely=0.5, anchor=CENTER)
        frame_login.pack_propagate(False)
        
        
        self.username_label = customtkinter.CTkLabel(master=frame_login, text="Username:",text_color="#000000",  font=('Garamond', 19))
        self.username_label.place(x=55, y= 100)

        self.username_entry = customtkinter.CTkEntry(master=frame_login, width=200,fg_color="#FFFFFF",text_color="#000000",border_color="#000000", placeholder_text="Enter username",  font=('Rockwell', 17) )
        self.username_entry.place(x=55,y=130)

        self.password_label = customtkinter.CTkLabel(master=frame_login, text="Password:",text_color="#000000",  font=('Garamond', 19))
        self.password_label.place(x=55, y=170)

        self.password_entry = customtkinter.CTkEntry(master=frame_login, show="*",  width=200,fg_color="#FFFFFF",text_color="#000000",border_color="#000000", placeholder_text="Enter password", font=('Rockwell', 17))
        self.password_entry.place(x=55, y=200)

        self.login_button = customtkinter.CTkButton(master=frame_login,fg_color="#0857FF", corner_radius=20, hover_color="#5FACF0", text="Login", command=self.authenticate)
        self.login_button.place(x=55, y=245)

        self.signup_button = customtkinter.CTkButton(master=frame_login,fg_color="#0857FF", corner_radius=20, hover_color="#5FACF0",text="Signup", command=self.open_signup)
        self.signup_button.place(x=240, y=245)

        self.status_label = customtkinter.CTkLabel(master=frame_login, text="")
        self.status_label.place(x=600, y=310)
        
    def check_credentials(self, username, password):
        try:
            connection = mysql.connector.connect(
                host='localhost',
                user='root',
                password='',
                database='FSP_DATA',
                port='3307'
            )

            cursor = connection.cursor()

            # Check if the entered credentials match any user in the database
            query = "SELECT * FROM users_db WHERE username = %s AND password = %s"
            cursor.execute(query, (username, password))

            user_data = cursor.fetchone()

            if user_data:
                return True

        except mysql.connector.Error as err:
            print(f"Error: {err}")

        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

        return False

    def authenticate(self):
       entered_username = self.username_entry.get()
       entered_password = self.password_entry.get()

       if not entered_username or not entered_password:
        messagebox.showerror("Error", "Please Sign-up first")
        
        self.login_window.destroy()
        signup_instance = Signup()
       if self.check_credentials(entered_username, entered_password):
        self.login_window.destroy()
        dashboard_instance = Dashboard(entered_username)
        dashboard_instance.open_dashboard()
       else:
        messagebox.showerror("Invalid credentials", "The entered username or password is incorrect.")

        # Run Tkinter main loop
        self.login_window.mainloop()

    def open_signup(self):
        self.login_window.destroy()
        # Create an instance of the Signup class when the Signup button is clicked
        signup_instance = Signup()
        # Destroy the login window to switch to the signup window
        

if __name__ == "__main__":
    login_instance = Login()
    login_instance.login_window.mainloop()