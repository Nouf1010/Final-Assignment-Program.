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
        # EMPLOYEE BUTTONS
        # Create buttons for adding, deleting, modifying, and displaying employee details
        add_employee_button = tk.Button(self, text="Add Employee", command=self.add_employee)  # Button to add an employee
        add_employee_button.pack()  # Adding the button to the application window

        delete_employee_button = tk.Button(self, text="Delete Employee", command=self.delete_employee)  # Button to delete an employee
        delete_employee_button.pack()  # Adding the button to the application window

        modify_employee_button = tk.Button(self, text="Modify Employee", command=self.modify_employee)  # Button to modify an employee
        modify_employee_button.pack()  # Adding the button to the application window

        display_employee_button = tk.Button(self, text="Display Employee", command=self.display_employee)  # Button to display employee details
        display_employee_button.pack()  # Adding the button to the application window

        # EVENT BUTTONS
        # Create buttons for adding, deleting, modifying, and displaying event details
        add_event_button = tk.Button(self, text="Add Event", command=self.add_event)  # Button to add an event
        add_event_button.pack()  # Adding the button to the application window

        delete_event_button = tk.Button(self, text="Delete Event", command=self.delete_event)  # Button to delete an event
        delete_event_button.pack()  # Adding the button to the application window

        modify_event_button = tk.Button(self, text="Modify Event", command=self.modify_event)  # Button to modify an event
        modify_event_button.pack()  # Adding the button to the application window

        display_event_button = tk.Button(self, text="Display Event", command=self.display_event)  # Button to display event details
        display_event_button.pack()  # Adding the button to the application window

        # GUEST BUTTONS
        # Create buttons for adding, deleting, modifying, and displaying guest details
        add_guest_button = tk.Button(self, text="Add Guest", command=self.add_guest)  # Button to add a guest
        add_guest_button.pack()  # Adding the button to the application window

        delete_guest_button = tk.Button(self, text="Delete Guest", command=self.delete_guest)  # Button to delete a guest
        delete_guest_button.pack()  # Adding the button to the application window

        modify_guest_button = tk.Button(self, text="Modify Guest", command=self.modify_guest)  # Button to modify a guest
        modify_guest_button.pack()  # Adding the button to the application window

        display_guest_button = tk.Button(self, text="Display Guest", command=self.display_guest)  # Button to display guest details
        display_guest_button.pack()  # Adding the button to the application window

        # SUPPLIER BUTTONS
        # Create buttons for adding, deleting, modifying, and displaying supplier details
        add_supplier_button = tk.Button(self, text="Add Supplier", command=self.add_supplier)  # Button to add a supplier
        add_supplier_button.pack()  # Adding the button to the application window

        delete_supplier_button = tk.Button(self, text="Delete Supplier", command=self.delete_supplier)  # Button to delete a supplier
        delete_supplier_button.pack()  # Adding the button to the application window

        modify_supplier_button = tk.Button(self, text="Modify Supplier", command=self.modify_supplier)  # Button to modify a supplier
        modify_supplier_button.pack()  # Adding the button to the application window

        display_supplier_button = tk.Button(self, text="Display Supplier", command=self.display_supplier)  # Button to display supplier details
        display_supplier_button.pack()  # Adding the button to the application window

        # VENUE BUTTONS
        # Create buttons for adding, deleting, modifying, and displaying venue details
        add_venue_button = tk.Button(self, text="Add Venue", command=self.add_venue)  # Button to add a venue
        add_venue_button.pack()  # Adding the button to the application window

        delete_venue_button = tk.Button(self, text="Delete Venue", command=self.delete_venue)  # Button to delete a venue
        delete_venue_button.pack()  # Adding the button to the application window

        modify_venue_button = tk.Button(self, text="Modify Venue", command=self.modify_venue)  # Button to modify a venue
        modify_venue_button.pack()  # Adding the button to the application window

        display_venue_button = tk.Button(self, text="Display Venue", command=self.display_venue)  # Button to display venue details
        display_venue_button.pack()  # Adding the button to the application window

        # CLIENT BUTTONS
        # Create buttons for adding, deleting, modifying, and displaying client details
        add_client_button = tk.Button(self, text="Add Client", command=self.add_client)  # Button to add a client
        add_client_button.pack()  # Adding the button to the application window

        delete_client_button = tk.Button(self, text="Delete Client", command=self.delete_client)  # Button to delete a client
        delete_client_button.pack()  # Adding the button to the application window

        modify_client_button = tk.Button(self, text="Modify Client", command=self.modify_client)  # Button to modify a client
        modify_client_button.pack()  # Adding the button to the application window

        display_client_button = tk.Button(self, text="Display Client", command=self.display_client)  # Button to display client details
        display_client_button.pack()  # Adding the button to the application window

    #EMPLOYEE
    def add_employee(self):
        # Create a new Toplevel window for adding employee details
        self.add_employee_window = tk.Toplevel(self)
        self.add_employee_window.title("Add Employee")  # Setting title for the window

        # Label and Entry widgets for employee details
        tk.Label(self.add_employee_window, text="Name:").grid(row=0, column=0)  # Label for employee name
        name_entry = tk.Entry(self.add_employee_window)  # Entry field for entering employee name
        name_entry.grid(row=0, column=1)  # Positioning entry field

        tk.Label(self.add_employee_window, text="Phone Number:").grid(row=1, column=0)  # Label for phone number
        phone_entry = tk.Entry(self.add_employee_window)  # Entry field for entering phone number
        phone_entry.grid(row=1, column=1)  # Positioning entry field

        tk.Label(self.add_employee_window, text="Email:").grid(row=2, column=0)  # Label for email
        email_entry = tk.Entry(self.add_employee_window)  # Entry field for entering email
        email_entry.grid(row=2, column=1)  # Positioning entry field

        tk.Label(self.add_employee_window, text="Employee ID:").grid(row=3, column=0)  # Label for employee ID
        emp_id_entry = tk.Entry(self.add_employee_window)  # Entry field for entering employee ID
        emp_id_entry.grid(row=3, column=1)  # Positioning entry field

        tk.Label(self.add_employee_window, text="Role:").grid(row=4, column=0)  # Label for employee role
        role_entry = tk.Entry(self.add_employee_window)  # Entry field for entering employee role
        role_entry.grid(row=4, column=1)  # Positioning entry field

        # Function to handle submission of employee details
        def submit_employee():
            # Get values from Entry widgets
            name = name_entry.get()  # Retrieve the name entered by the user
            phone = phone_entry.get()  # Retrieve the phone number entered by the user
            email = email_entry.get()  # Retrieve the email entered by the user
            emp_id = emp_id_entry.get()  # Retrieve the employee ID entered by the user
            role = role_entry.get()  # Retrieve the role entered by the user

            # Create an instance of Employee class with provided details
            employee = Employee(name, phone, email, emp_id, role)  # Create an Employee object

            # Add the employee instance to the list
            self.employees.append(employee)  # Append the new employee to the list of employees

            # Serialize the employee object and store it in a binary file
            with open('employees.pkl', 'ab') as file:  # Open the file in binary append mode
                pickle.dump(employee, file)  # Serialize and write the employee object to the file

            # Display success message
            messagebox.showinfo("Success", "Employee added successfully")  # Show a success message dialog box

            # Close the Toplevel window
            self.add_employee_window.destroy()  # Destroy the window for adding an employee
            # Reset the reference to the window
            self.add_employee_window = None  # Set the window reference to None to indicate it's closed

        # Button to submit employee details
        submit_button = tk.Button(self.add_employee_window, text="Submit", command=submit_employee)  # Button to submit employee details
        submit_button.grid(row=5, column=0)  # Positioning the submit button

        # Button to go back
        back_button = tk.Button(self.add_employee_window, text="Back", command=self.add_employee_window.destroy)  # Button to close the window
        back_button.grid(row=5, column=1)  # Positioning the back button

    def delete_employee(self):
        # Create a new Toplevel window for deleting an employee
        self.delete_employee_window = tk.Toplevel(self)
        self.delete_employee_window.title("Delete Employee")  # Set title for the window

        # Label and Entry widgets for employee ID
        tk.Label(self.delete_employee_window, text="Employee ID:").grid(row=0, column=0)  # Label for employee ID
        emp_id_entry = tk.Entry(self.delete_employee_window)  # Entry field for entering employee ID
        emp_id_entry.grid(row=0, column=1)  # Positioning entry field

        # Function to handle deletion of employee
        def delete_employee_action():
            # Get the employee ID to delete
            emp_id = emp_id_entry.get()  # Retrieve the employee ID entered by the user

            # Search for the employee with the given ID
            for employee in self.employees:  # Iterate through the list of employees
                if employee.get_empID() == emp_id:  # Check if the employee ID matches
                    # Remove the employee from the list
                    self.employees.remove(employee)  # Remove the employee from the list

                    # Update the serialized file (overwrite it entirely)
                    with open('employees.pkl', 'wb') as file:  # Open the file in write-binary mode
                        pickle.dump(self.employees, file)  # Serialize and write the updated employee list to the file

                    # Display success message
                    messagebox.showinfo("Success", "Employee deleted successfully")  # Show a success message dialog box

                    # Close the Toplevel window
                    self.delete_employee_window.destroy()  # Destroy the window for deleting an employee
                    return

            # If employee with given ID is not found
            messagebox.showerror("Error", "Employee with the given ID not found")  # Show an error message dialog box

        # Button to delete employee
        delete_button = tk.Button(self.delete_employee_window, text="Delete", command=delete_employee_action)  # Button to trigger deletion
        delete_button.grid(row=1, column=0)  # Positioning the delete button

        # Button to go back
        back_button = tk.Button(self.delete_employee_window, text="Back", command=self.delete_employee_window.destroy)  # Button to close the window
        back_button.grid(row=1, column=1)  # Positioning the back button


    def modify_employee(self):
        # Create a new Toplevel window for modifying an employee
        self.modify_employee_window = tk.Toplevel(self)
        self.modify_employee_window.title("Modify Employee")  # Set title for the window

        # Label and Entry widgets for employee ID
        tk.Label(self.modify_employee_window, text="Employee ID:").grid(row=0, column=0)  # Label for employee ID
        emp_id_entry = tk.Entry(self.modify_employee_window)  # Entry field for entering employee ID
        emp_id_entry.grid(row=0, column=1)  # Positioning entry field

        # Function to handle modification of employee
        def modify_employee_inner():
            # Get the employee ID to modify
            emp_id = emp_id_entry.get()  # Retrieve the employee ID entered by the user

            # Search for the employee with the given ID
            for employee in self.employees:  # Iterate through the list of employees
                if employee.get_empID() == emp_id:  # Check if the employee ID matches
                    # Open a new window to modify employee details
                    modify_window = tk.Toplevel(self.modify_employee_window)  # Create a new window
                    modify_window.title("Modify Employee Details")  # Set title for the new window

                    # Label and Entry widgets to display current details
                    tk.Label(modify_window, text="Name:").grid(row=0, column=0)  # Label for employee name
                    name_entry = tk.Entry(modify_window)  # Entry field for entering employee name
                    name_entry.insert(0, employee.get_nameP())  # Insert current name into the entry field
                    name_entry.grid(row=0, column=1)  # Positioning entry field

                    tk.Label(modify_window, text="Phone Number:").grid(row=1, column=0)  # Label for phone number
                    phone_entry = tk.Entry(modify_window)  # Entry field for entering phone number
                    phone_entry.insert(0, employee.get_phone_numP())  # Insert current phone number into the entry field
                    phone_entry.grid(row=1, column=1)  # Positioning entry field

                    tk.Label(modify_window, text="Email:").grid(row=2, column=0)  # Label for email
                    email_entry = tk.Entry(modify_window)  # Entry field for entering email
                    email_entry.insert(0, employee.get_emailP())  # Insert current email into the entry field
                    email_entry.grid(row=2, column=1)  # Positioning entry field

                    tk.Label(modify_window, text="Role:").grid(row=3, column=0)  # Label for role
                    role_entry = tk.Entry(modify_window)  # Entry field for entering role
                    role_entry.insert(0, employee.get_role())  # Insert current role into the entry field
                    role_entry.grid(row=3, column=1)  # Positioning entry field

                    # Function to handle modification submission
                    def submit_modification():
                        # Update the employee object with new details
                        employee.set_nameP(name_entry.get())  # Set new name
                        employee.set_phone_numP(phone_entry.get())  # Set new phone number
                        employee.set_emailP(email_entry.get())  # Set new email
                        employee.set_role(role_entry.get())  # Set new role

                        # Update the serialized file (you might want to overwrite it entirely)
                        with open('employees.pkl', 'wb') as file:  # Open the file in write-binary mode
                            pickle.dump(self.employees, file)  # Serialize and write the updated employee list to the file

                        # Display success message
                        messagebox.showinfo("Success","Employee details modified successfully")  # Show a success message dialog box

                        # Close the modification window
                        modify_window.destroy()  # Destroy the window for modifying employee details

                    # Button to submit modifications
                    submit_button = tk.Button(modify_window, text="Submit", command=submit_modification)  # Button to submit modifications
                    submit_button.grid(row=4, column=0)  # Positioning the submit button

                    return

            # If employee with given ID is not found
            messagebox.showerror("Error", "Employee with the given ID not found")  # Show an error message dialog box

        # Button to modify employee
        modify_button = tk.Button(self.modify_employee_window, text="Modify", command=modify_employee_inner)  # Button to trigger modification
        modify_button.grid(row=1, column=0)  # Positioning the modify button

        # Button to go back
        back_button = tk.Button(self.modify_employee_window, text="Back", command=self.modify_employee_window.destroy)  # Button to close the window
        back_button.grid(row=1, column=1)  # Positioning the back button

    def display_employee(self):
        # Create a new Toplevel window for displaying an employee's details
        self.display_employee_window = tk.Toplevel(self)
        self.display_employee_window.title("Display Employee Details")  # Set title for the window

        # Label and Entry widgets for employee ID
        tk.Label(self.display_employee_window, text="Employee ID:").grid(row=0, column=0)  # Label for employee ID
        emp_id_entry = tk.Entry(self.display_employee_window)  # Entry field for entering employee ID
        emp_id_entry.grid(row=0, column=1)  # Positioning entry field

        # Function to handle displaying employee details
        def display_employee_action():
            # Get the employee ID to display
            emp_id = emp_id_entry.get()  # Retrieve the employee ID entered by the user

            # Search for the employee with the given ID
            for employee in self.employees:  # Iterate through the list of employees
                if employee.get_empID() == emp_id:  # Check if the employee ID matches
                    # Display employee details in a messagebox or label
                    details = f"Name: {employee.get_nameP()}\nPhone: {employee.get_phone_numP()}\nEmail: {employee.get_emailP()}\nRole: {employee.get_role()}"
                    messagebox.showinfo("Employee Details", details)  # Show a messagebox with employee details
                    return

            # If employee with given ID is not found
            messagebox.showerror("Error", "Employee with the given ID not found")  # Show an error message dialog box

        # Button to display employee details
        display_button = tk.Button(self.display_employee_window, text="Display", command=display_employee_action)  # Button to trigger display
        display_button.grid(row=1, column=0)  # Positioning the display button

        # Button to go back
        back_button = tk.Button(self.display_employee_window, text="Back", command=self.display_employee_window.destroy)  # Button to close the window
        back_button.grid(row=1, column=1)  # Positioning the back button

    #EVENT
    def add_event(self):
        # Create a new Toplevel window for adding event details
        self.add_event_window = tk.Toplevel(self)
        self.add_event_window.title("Add Event")  # Set title for the window

        # Label and Entry widgets for event details
        tk.Label(self.add_event_window, text="Event ID:").grid(row=0, column=0)  # Label for event ID
        event_id_entry = tk.Entry(self.add_event_window)  # Entry field for entering event ID
        event_id_entry.grid(row=0, column=1)  # Positioning entry field

        tk.Label(self.add_event_window, text="Type:").grid(row=1, column=0)  # Label for event type
        type_entry = tk.Entry(self.add_event_window)  # Entry field for entering event type
        type_entry.grid(row=1, column=1)  # Positioning entry field

        tk.Label(self.add_event_window, text="Date:").grid(row=2, column=0)  # Label for event date
        date_entry = tk.Entry(self.add_event_window)  # Entry field for entering event date
        date_entry.grid(row=2, column=1)  # Positioning entry field

        tk.Label(self.add_event_window, text="Time:").grid(row=3, column=0)  # Label for event time
        time_entry = tk.Entry(self.add_event_window)  # Entry field for entering event time
        time_entry.grid(row=3, column=1)  # Positioning entry field

        tk.Label(self.add_event_window, text="Duration:").grid(row=4, column=0)  # Label for event duration
        duration_entry = tk.Entry(self.add_event_window)  # Entry field for entering event duration
        duration_entry.grid(row=4, column=1)  # Positioning entry field

        tk.Label(self.add_event_window, text="Venue:").grid(row=5, column=0)  # Label for event venue
        venue_entry = tk.Entry(self.add_event_window)  # Entry field for entering event venue
        venue_entry.grid(row=5, column=1)  # Positioning entry field

        # Function to handle submission of event details
        def submit_event():
            # Get values from Entry widgets
            event_id = event_id_entry.get()  # Get event ID
            type = type_entry.get()  # Get event type
            date = date_entry.get()  # Get event date
            time = time_entry.get()  # Get event time
            duration = duration_entry.get()  # Get event duration
            venue = venue_entry.get()  # Get event venue

            # Create an instance of Event class with provided details
            event = Event(event_id, type, date, time, duration, venue, guest_list=None)

            # Add the event instance to the list
            self.events.append(event)

            # Serialize the event object and store it in a binary file
            with open('events.pkl', 'ab') as file:
                pickle.dump(event, file)

            # Display success message
            messagebox.showinfo("Success", "Event added successfully")

            # Close the Toplevel window
            self.add_event_window.destroy()
            # Reset the reference to the window
            self.add_event_window = None

        # Button to submit event details
        submit_button = tk.Button(self.add_event_window, text="Submit", command=submit_event)
        submit_button.grid(row=6, column=0)

        # Button to go back
        back_button = tk.Button(self.add_event_window, text="Back", command=self.add_event_window.destroy)
        back_button.grid(row=6, column=1)








