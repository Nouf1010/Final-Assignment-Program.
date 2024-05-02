import tkinter as tk
from tkinter import messagebox
import pickle

from Aggregation import *
from Composition import *
from Inheritance import *
from Uni import *


class Application(tk.Tk):  # Define a class 'Application' inheriting from 'tk.Tk'
    def __init__(self):  # Constructor method for the class
        super().__init__()  # Calling the constructor of the superclass
        self.title("Event Management System")  # Setting the title of the application window
        self.geometry("600x400")  # Setting the initial size of the application window

        # Create lists to store different types of data
        self.employees = []  # List to store employee data
        self.events = []  # List to store event data
        self.guests = []  # List to store guest data
        self.suppliers = []  # List to store supplier data
        self.venues = []  # List to store venue data
        self.clients = []  # List to store client data

        # Create GUI elements
        self.create_widgets()  # Call a method to create GUI elements

        # Initialize windows for adding new data (None initially)
        self.add_employee_window = None  # Window for adding employee
        self.add_event_window = None  # Window for adding event
        self.add_guest_window = None  # Window for adding guest
        self.add_supplier_window = None  # Window for adding supplier
        self.add_venue_window = None  # Window for adding venue
        self.add_client_window = None  # Window for adding client

    def create_widgets(self):
    #EMPLOYEE BUTTONS
    # Create buttons for adding, deleting, modifying, and displaying employee details
    add_employee_button = tk.Button(self, text="Add Employee", command=self.add_employee)  # Button to add an employee
    add_employee_button.pack()  # Adding the button to the application window

    delete_employee_button = tk.Button(self, text="Delete Employee", command=self.delete_employee)  # Button to delete an employee
    delete_employee_button.pack()  # Adding the button to the application window

    modify_employee_button = tk.Button(self, text="Modify Employee", command=self.modify_employee)  # Button to modify an employee
    modify_employee_button.pack()  # Adding the button to the application window

    display_employee_button = tk.Button(self, text="Display Employee", command=self.display_employee)  # Button to display employee details
    display_employee_button.pack()  # Adding the button to the application window



