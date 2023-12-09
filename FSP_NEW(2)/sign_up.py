import tkinter as tk
from tkinter import *
import mysql.connector
from login import Login
from dashboard import Dashboard
import customtkinter
from PIL import Image, ImageTk

class Signup:
    def __init__(self):
        customtkinter.set_appearance_mode("light")
        self.signup_window = customtkinter.CTk()
        self.signup_window.geometry('1407x780')
        self.signup_window.iconbitmap("E:/user/Desktop/School things/PYTHON FINAL PROJECT/FSP_NEW(2)/coffee-cup.ico")
        self.signup_window.resizable(False,False)
        self.signup_window.title("Sign-up")
        
        pil_image = Image.open("loginbg.jpg")

        # Convert the PIL Image to a Tkinter PhotoImage
        self.image = ImageTk.PhotoImage(pil_image)

        # Create a Label widget to display the image
        self.image_label = tk.Label(self.signup_window, image=self.image)
        self.image_label.pack()

        
        frame_signup = customtkinter.CTkFrame(master=self.signup_window,width=371, height=329, fg_color="#FFFFFF")
        frame_signup.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        frame_signup.pack_propagate(False)
        

        # Create GUI components
        self.username_label = customtkinter.CTkLabel(master=frame_signup, text="Username:", font=('Garamond', 19), text_color="#000000")
        self.username_label.pack(pady=20)

        self.username_entry = customtkinter.CTkEntry(master=frame_signup, width=200,fg_color="#FFFFFF",text_color="#000000",border_color="#000000", placeholder_text="Enter username", font=('Rockwell', 17))
        self.username_entry.pack()

        self.password_label = customtkinter.CTkLabel(master=frame_signup, text="Password:", font=('Garamond', 19), text_color="#000000")
        self.password_label.pack(pady=20)

        self.password_entry = customtkinter.CTkEntry(master=frame_signup, show="*", width=200,fg_color="#FFFFFF",text_color="#000000",border_color="#000000", placeholder_text="Enter username", font=('Rockwell', 17))
        self.password_entry.pack()

        self.signup_button = customtkinter.CTkButton(master=frame_signup, text="Sign Up",fg_color="#0857FF", corner_radius=20, hover_color="#5FACF0", font=('Rockwell', 12), command=self.sign_up)
        self.signup_button.pack(pady=20)
        
        self.signup_window.mainloop()

    def sign_up(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        try:
            connection = mysql.connector.connect(
                host='localhost',
                user='root',
                password='',
                database='FSP_DATA',
                port='3307'
            )

            cursor = connection.cursor()

            # Insert user data into the database
            query = "INSERT INTO users_db (username, password) VALUES (%s, %s)"
            cursor.execute(query, (username, password))

            connection.commit()
            print("User registered successfully")

            # Open the login window after successful registration
        # Open the login window after successful registration
            self.signup_window.destroy()
            login_instance = Login()
            login_instance.login_window.mainloop()

        except mysql.connector.Error as err:
            print(f"Error: {err}")

        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()
                
    def open_sign_up(self):
        # Run Tkinter main loop
        self.signup_window.mainloop()

if __name__ == "__main__":
    signup_instance = Signup()