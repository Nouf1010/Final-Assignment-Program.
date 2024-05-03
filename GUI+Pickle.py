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

    def delete_event(self):
        # Create a new Toplevel window for deleting an event
        self.delete_event_window = tk.Toplevel(self)
        self.delete_event_window.title("Delete Event")  # Set title for the window

        # Label and Entry widgets for event ID
        tk.Label(self.delete_event_window, text="Event ID:").grid(row=0, column=0)  # Label for event ID
        event_id_entry = tk.Entry(self.delete_event_window)  # Entry field for entering event ID
        event_id_entry.grid(row=0, column=1)  # Positioning entry field

        # Function to handle deletion of event
        def delete_event_action():
            # Get the event ID to delete
            event_id = event_id_entry.get()  # Retrieve the event ID entered by the user

            # Search for the event with the given ID
            for event in self.events:  # Iterate through the list of events
                if event.get_eventID() == event_id:  # Check if the event ID matches
                    # Remove the event from the list
                    self.events.remove(event)  # Remove the event from the list

                    # Display success message
                    messagebox.showinfo("Success", "Event deleted successfully")  # Show a success message dialog box

                    # Close the Toplevel window
                    self.delete_event_window.destroy()  # Destroy the window for deleting an event
                    return

            # If event with given ID is not found
            messagebox.showerror("Error", "Event with the given ID not found")  # Show an error message dialog box

        # Button to delete event
        delete_button = tk.Button(
            self.delete_event_window, text="Delete", command=delete_event_action)  # Button to trigger deletion
        delete_button.grid(row=1, column=0)  # Positioning the delete button

        # Button to go back
        back_button = tk.Button(
            self.delete_event_window, text="Back",
            command=self.delete_event_window.destroy)  # Button to close the window
        back_button.grid(row=1, column=1)  # Positioning the back button

    def modify_event(self):
        # Create a new Toplevel window for modifying an event
        self.modify_event_window = tk.Toplevel(self)
        self.modify_event_window.title("Modify Event")

        # Label and Entry widgets for event ID
        tk.Label(self.modify_event_window, text="Event ID:").grid(row=0, column=0)
        event_id_entry = tk.Entry(self.modify_event_window)
        event_id_entry.grid(row=0, column=1)

        # Function to handle modification of an event
        def modify_event_inner():
            # Get the event ID to modify
            event_id = event_id_entry.get()  # Retrieve the event ID entered by the user

            # Search for the event with the given ID
            for event in self.events:  # Iterate through the list of events
                if event.get_eventID() == event_id:  # Check if the event ID matches
                    # Open a new window to modify event details
                    modify_window = tk.Toplevel(self.modify_event_window)  # Create a new window
                    modify_window.title("Modify Event Details")  # Set title for the new window

                    # Label and Entry widgets to display current details
                    tk.Label(modify_window, text="Type:").grid(row=0, column=0)  # Label for event type
                    type_entry = tk.Entry(modify_window)  # Entry field for entering event type
                    type_entry.insert(0, event.get_type())  # Insert current type into the entry field
                    type_entry.grid(row=0, column=1)  # Positioning entry field

                    tk.Label(modify_window, text="Date:").grid(row=1, column=0)  # Label for event date
                    date_entry = tk.Entry(modify_window)  # Entry field for entering event date
                    date_entry.insert(0, event.get_date())  # Insert current date into the entry field
                    date_entry.grid(row=1, column=1)  # Positioning entry field

                    tk.Label(modify_window, text="Time:").grid(row=2, column=0)  # Label for event time
                    time_entry = tk.Entry(modify_window)  # Entry field for entering event time
                    time_entry.insert(0, event.get_time())  # Insert current time into the entry field
                    time_entry.grid(row=2, column=1)  # Positioning entry field

                    tk.Label(modify_window, text="Duration:").grid(row=3, column=0)  # Label for event duration
                    duration_entry = tk.Entry(modify_window)  # Entry field for entering event duration
                    duration_entry.insert(0, event.get_duration())  # Insert current duration into the entry field
                    duration_entry.grid(row=3, column=1)  # Positioning entry field

                    tk.Label(modify_window, text="Venue:").grid(row=4, column=0)  # Label for event venue
                    venue_entry = tk.Entry(modify_window)  # Entry field for entering event venue
                    venue_entry.insert(0, event.get_venue())  # Insert current venue into the entry field
                    venue_entry.grid(row=4, column=1)  # Positioning entry field

                    # Function to handle modification submission
                    def submit_modification():
                        # Update the event object with new details
                        event.set_type(type_entry.get())  # Set new type
                        event.set_date(date_entry.get())  # Set new date
                        event.set_time(time_entry.get())  # Set new time
                        event.set_duration(duration_entry.get())  # Set new duration
                        event.set_venue(venue_entry.get())  # Set new venue

                        # Update the serialized file (you might want to overwrite it entirely)
                        with open('events.pkl', 'wb') as file:  # Open the file in write-binary mode
                            pickle.dump(self.events, file)  # Serialize and write the updated event list to the file

                        # Display success message
                        messagebox.showinfo("Success","Event details modified successfully")  # Show a success message dialog box

                        # Close the modification window
                        modify_window.destroy()  # Destroy the window for modifying event details

                    # Button to submit modifications
                    submit_button = tk.Button(modify_window, text="Submit", command=submit_modification)  # Button to submit modifications
                    submit_button.grid(row=5, column=0)  # Positioning the submit button

                    return

            # If event with given ID is not found
            messagebox.showerror("Error", "Event with the given ID not found")  # Show an error message dialog box

        # Button to modify event
        modify_button = tk.Button(self.modify_event_window, text="Modify", command=modify_event_inner)  # Button to trigger modification
        modify_button.grid(row=1, column=0)  # Positioning the modify button

        # Button to go back
        back_button = tk.Button(self.modify_event_window, text="Back", command=self.modify_event_window.destroy)  # Button to close the window
        back_button.grid(row=1, column=1)  # Positioning the back button


    def display_event(self):
        # Create a new Toplevel window for displaying an event's details
        self.display_event_window = tk.Toplevel(self)
        self.display_event_window.title("Display Event Details")

        # Label and Entry widgets for event ID
        tk.Label(self.display_event_window, text="Event ID:").grid(row=0, column=0)
        event_id_entry = tk.Entry(self.display_event_window)
        event_id_entry.grid(row=0, column=1)

        # Function to handle displaying event details
        def display_event_action():
            # Get the event ID to display
            event_id = event_id_entry.get()

            # Search for the event with the given ID
            for event in self.events:
                if event.get_eventID() == event_id:
                    # Display event details in a messagebox or label
                    details = f"Type: {event.get_type()}\nDate: {event.get_date()}\nTime: {event.get_time()}\nDuration: {event.get_duration()}\nVenue: {event.get_venue()}"
                    messagebox.showinfo("Event Details", details)
                    return

            # If event with given ID is not found
            messagebox.showerror("Error", "Event with the given ID not found")

        # Button to display event details
        display_button = tk.Button(self.display_event_window, text="Display", command=display_event_action)
        display_button.grid(row=1, column=0)

        # Button to go back
        back_button = tk.Button(self.display_event_window, text="Back", command=self.display_event_window.destroy)
        back_button.grid(row=1, column=1)

    #GUEST
    def add_guest(self):
        # Create a new Toplevel window for adding guest details
        self.add_guest_window = tk.Toplevel(self)
        self.add_guest_window.title("Add Guest")

        # Label and Entry widgets for guest details
        tk.Label(self.add_guest_window, text="Name:").grid(row=0, column=0)
        name_entry = tk.Entry(self.add_guest_window)
        name_entry.grid(row=0, column=1)

        tk.Label(self.add_guest_window, text="Phone Number:").grid(row=1, column=0)
        phone_entry = tk.Entry(self.add_guest_window)
        phone_entry.grid(row=1, column=1)

        tk.Label(self.add_guest_window, text="Email:").grid(row=2, column=0)
        email_entry = tk.Entry(self.add_guest_window)
        email_entry.grid(row=2, column=1)

        tk.Label(self.add_guest_window, text="Guest ID:").grid(row=3, column=0)
        guest_id_entry = tk.Entry(self.add_guest_window)
        guest_id_entry.grid(row=3, column=1)

        # Function to handle submission of guest details
        def submit_guest():
            # Get values from Entry widgets
            name = name_entry.get()
            phone = phone_entry.get()
            email = email_entry.get()
            guest_id = guest_id_entry.get()

            # Create an instance of Guest class with provided details
            guest = Guest(name, phone, email, guest_id)

            # Add the guest instance to the list
            self.guests.append(guest)

            # Serialize the guest object and store it in a binary file
            with open('guests.pkl', 'ab') as file:
                pickle.dump(guest, file)

            # Display success message
            messagebox.showinfo("Success", "Guest added successfully")

            # Close the Toplevel window
            self.add_guest_window.destroy()
            # Reset the reference to the window
            self.add_guest_window = None

        # Button to submit guest details
        submit_button = tk.Button(self.add_guest_window, text="Submit", command=submit_guest)
        submit_button.grid(row=4, column=0)

        # Button to go back
        back_button = tk.Button(self.add_guest_window, text="Back", command=self.add_guest_window.destroy)
        back_button.grid(row=4, column=1)

    def delete_guest(self):
        # Create a new Toplevel window for deleting a guest
        self.delete_guest_window = tk.Toplevel(self)
        self.delete_guest_window.title("Delete Guest")

        # Label and Entry widgets for guest ID
        tk.Label(self.delete_guest_window, text="Guest ID:").grid(row=0, column=0)
        guest_id_entry = tk.Entry(self.delete_guest_window)
        guest_id_entry.grid(row=0, column=1)

        # Function to handle deletion of guest
        def delete_guest_action():
            # Get the guest ID to delete
            guest_id = guest_id_entry.get()

            # Search for the guest with the given ID
            for guest in self.guests:
                if guest.get_guestID() == guest_id:
                    # Remove the guest from the list
                    self.guests.remove(guest)

                    # Update the serialized file (overwrite it entirely)
                    with open('guests.pkl', 'wb') as file:
                        pickle.dump(self.guests, file)

                    # Display success message
                    messagebox.showinfo("Success", "Guest deleted successfully")

                    # Close the Toplevel window
                    self.delete_guest_window.destroy()
                    return

            # If guest with given ID is not found
            messagebox.showerror("Error", "Guest with the given ID not found")

        # Button to delete guest
        delete_button = tk.Button(self.delete_guest_window, text="Delete", command=delete_guest_action)
        delete_button.grid(row=1, column=0)

        # Button to go back
        back_button = tk.Button(self.delete_guest_window, text="Back", command=self.delete_guest_window.destroy)
        back_button.grid(row=1, column=1)

    def modify_guest(self):
        # Create a new Toplevel window for modifying a guest
        self.modify_guest_window = tk.Toplevel(self)
        self.modify_guest_window.title("Modify Guest")

        # Label and Entry widgets for guest ID
        tk.Label(self.modify_guest_window, text="Guest ID:").grid(row=0, column=0)
        guest_id_entry = tk.Entry(self.modify_guest_window)
        guest_id_entry.grid(row=0, column=1)

        # Function to handle modification of a guest
        def modify_guest_inner():
            # Get the guest ID to modify
            guest_id = guest_id_entry.get()  # Retrieve the guest ID entered by the user

            # Search for the guest with the given ID
            for guest in self.guests:  # Iterate through the list of guests
                if guest.get_guestID() == guest_id:  # Check if the guest ID matches
                    # Open a new window to modify guest details
                    modify_window = tk.Toplevel(self.modify_guest_window)  # Create a new window
                    modify_window.title("Modify Guest Details")  # Set title for the new window

                    # Label and Entry widgets to display current details
                    tk.Label(modify_window, text="Name:").grid(row=0, column=0)  # Label for guest name
                    name_entry = tk.Entry(modify_window)  # Entry field for entering guest name
                    name_entry.insert(0, guest.get_nameP())  # Insert current name into the entry field
                    name_entry.grid(row=0, column=1)  # Positioning entry field

                    tk.Label(modify_window, text="Phone Number:").grid(row=1, column=0)  # Label for phone number
                    phone_entry = tk.Entry(modify_window)  # Entry field for entering phone number
                    phone_entry.insert(0, guest.get_phone_numP())  # Insert current phone number into the entry field
                    phone_entry.grid(row=1, column=1)  # Positioning entry field

                    tk.Label(modify_window, text="Email:").grid(row=2, column=0)  # Label for email
                    email_entry = tk.Entry(modify_window)  # Entry field for entering email
                    email_entry.insert(0, guest.get_emailP())  # Insert current email into the entry field
                    email_entry.grid(row=2, column=1)  # Positioning entry field

                    tk.Label(modify_window, text="Guest ID:").grid(row=3, column=0)  # Label for guest ID
                    guest_id_entry_modify = tk.Entry(modify_window)  # Entry field for entering guest ID
                    guest_id_entry_modify.insert(0, guest.get_guestID())  # Insert current guest ID into the entry field
                    guest_id_entry_modify.grid(row=3, column=1)  # Positioning entry field

                    # Function to handle modification submission
                    def submit_modification():
                        # Update the guest object with new details
                        guest.set_nameP(name_entry.get())  # Set new name
                        guest.set_phone_numP(phone_entry.get())  # Set new phone number
                        guest.set_emailP(email_entry.get())  # Set new email
                        guest.set_guestID(guest_id_entry_modify.get())  # Set new guest ID

                        # Update the serialized file (you might want to overwrite it entirely)
                        with open('guests.pkl', 'wb') as file:  # Open the file in write-binary mode
                            pickle.dump(self.guests, file)  # Serialize and write the updated guest list to the file

                        # Display success message
                        messagebox.showinfo("Success","Guest details modified successfully")  # Show a success message dialog box

                        # Close the modification window
                        modify_window.destroy()  # Destroy the window for modifying guest details

                    # Button to submit modifications
                    submit_button = tk.Button(modify_window, text="Submit", command=submit_modification)  # Button to submit modifications
                    submit_button.grid(row=4, column=0)  # Positioning the submit button

                    return

            # If guest with given ID is not found
            messagebox.showerror("Error", "Guest with the given ID not found")  # Show an error message dialog box

        # Button to modify guest
        modify_button = tk.Button(self.modify_guest_window, text="Modify", command=modify_guest_inner)  # Button to trigger modification
        modify_button.grid(row=1, column=0)  # Positioning the modify button

        # Button to go back
        back_button = tk.Button(self.modify_guest_window, text="Back", command=self.modify_guest_window.destroy)  # Button to close the window
        back_button.grid(row=1, column=1)  # Positioning the back button

    def display_guest(self):
        # Create a new Toplevel window for displaying a guest's details
        self.display_guest_window = tk.Toplevel(self)
        self.display_guest_window.title("Display Guest Details")

        # Label and Entry widgets for guest ID
        tk.Label(self.display_guest_window, text="Guest ID:").grid(row=0, column=0)
        guest_id_entry = tk.Entry(self.display_guest_window)
        guest_id_entry.grid(row=0, column=1)

        # Function to handle displaying guest details
        def display_guest_action():
            # Get the guest ID to display
            guest_id = guest_id_entry.get()

            # Search for the guest with the given ID
            for guest in self.guests:
                if guest.get_guestID() == guest_id:
                    # Display guest details in a messagebox or label
                    details = f"Name: {guest.get_nameP()}\nPhone: {guest.get_phone_numP()}\nEmail: {guest.get_emailP()}"
                    messagebox.showinfo("Guest Details", details)
                    return

            # If guest with given ID is not found
            messagebox.showerror("Error", "Guest with the given ID not found")

        # Button to display guest details
        display_button = tk.Button(
            self.display_guest_window, text="Display", command=display_guest_action)
        display_button.grid(row=1, column=0)

        # Button to go back
        back_button = tk.Button(
            self.display_guest_window, text="Back", command=self.display_guest_window.destroy)
        back_button.grid(row=1, column=1)

    #SUPPLIER
    def add_supplier(self):
        # Create a new Toplevel window for adding supplier details
        self.add_supplier_window = tk.Toplevel(self)
        self.add_supplier_window.title("Add Supplier")

        # Label and Entry widgets for supplier details
        tk.Label(self.add_supplier_window, text="Supplier ID:").grid(row=0, column=0)
        sup_id_entry = tk.Entry(self.add_supplier_window)
        sup_id_entry.grid(row=0, column=1)

        tk.Label(self.add_supplier_window, text="Name:").grid(row=1, column=0)
        name_entry = tk.Entry(self.add_supplier_window)
        name_entry.grid(row=1, column=1)

        tk.Label(self.add_supplier_window, text="Phone Number:").grid(row=2, column=0)
        phone_entry = tk.Entry(self.add_supplier_window)
        phone_entry.grid(row=2, column=1)

        tk.Label(self.add_supplier_window, text="Address:").grid(row=3, column=0)
        address_entry = tk.Entry(self.add_supplier_window)
        address_entry.grid(row=3, column=1)


        # Function to handle submission of supplier details
        def submit_supplier():
            # Get values from Entry widgets
            sup_id = sup_id_entry.get()
            name = name_entry.get()
            phone = phone_entry.get()
            address = address_entry.get()

            # Create an instance of Supplier class with provided details
            new_supplier = Supplier(sup_id, name, phone, address)

            # Add the supplier instance to the list
            self.suppliers.append(new_supplier)

            # Serialize the supplier object and store it in a binary file
            with open('suppliers.pkl', 'ab') as file:
                pickle.dump(new_supplier, file)

            # Display success message
            messagebox.showinfo("Success", "Supplier added successfully")

            # Close the Toplevel window
            self.add_supplier_window.destroy()
            # Reset the reference to the window
            self.add_supplier_window = None

        # Button to submit supplier details
        submit_button = tk.Button(
            self.add_supplier_window, text="Submit", command=submit_supplier)
        submit_button.grid(row=7, column=0)

        # Button to go back
        back_button = tk.Button(
            self.add_supplier_window, text="Back", command=self.add_supplier_window.destroy)
        back_button.grid(row=7, column=1)

    def delete_supplier(self):
        # Create a new Toplevel window for deleting a supplier
        self.delete_supplier_window = tk.Toplevel(self)
        self.delete_supplier_window.title("Delete Supplier")

        # Label and Entry widgets for supplier ID
        tk.Label(self.delete_supplier_window, text="Supplier ID:").grid(row=0, column=0)
        sup_id_entry = tk.Entry(self.delete_supplier_window)
        sup_id_entry.grid(row=0, column=1)

        # Function to handle deletion of supplier
        def delete_supplier_action():
            # Get the supplier ID to delete
            sup_id = sup_id_entry.get()

            # Search for the supplier with the given ID
            for supplier in self.suppliers:
                if supplier.get_supID() == sup_id:
                    # Remove the supplier from the list
                    self.suppliers.remove(supplier)

                    # Update the serialized file (overwrite it entirely)
                    with open('suppliers.pkl', 'wb') as file:
                        pickle.dump(self.suppliers, file)

                    # Display success message
                    messagebox.showinfo("Success", "Supplier deleted successfully")

                    # Close the Toplevel window
                    self.delete_supplier_window.destroy()
                    return

            # If supplier with given ID is not found
            messagebox.showerror("Error", "Supplier with the given ID not found")

        # Button to delete supplier
        delete_button = tk.Button(self.delete_supplier_window, text="Delete", command=delete_supplier_action)
        delete_button.grid(row=1, column=0)

        # Button to go back
        back_button = tk.Button(self.delete_supplier_window, text="Back", command=self.delete_supplier_window.destroy)
        back_button.grid(row=1, column=1)

    def modify_supplier(self):
        # Create a new Toplevel window for modifying a supplier
        self.modify_supplier_window = tk.Toplevel(self)
        self.modify_supplier_window.title("Modify Supplier")

        # Label and Entry widgets for supplier ID
        tk.Label(self.modify_supplier_window, text="Supplier ID:").grid(row=0, column=0)
        sup_id_entry = tk.Entry(self.modify_supplier_window)
        sup_id_entry.grid(row=0, column=1)

        # Function to handle modification of a supplier
        def modify_supplier_inner():
            # Get the supplier ID to modify
            sup_id = sup_id_entry.get()  # Retrieve the supplier ID entered by the user

            # Search for the supplier with the given ID
            for supplier in self.suppliers:  # Iterate through the list of suppliers
                if supplier.get_supID() == sup_id:  # Check if the supplier ID matches
                    # Open a new window to modify supplier details
                    modify_window = tk.Toplevel(self.modify_supplier_window)  # Create a new window
                    modify_window.title("Modify Supplier Details")  # Set title for the new window

                    # Label and Entry widgets to display current details
                    tk.Label(modify_window, text="Supplier Name:").grid(row=0, column=0)  # Label for supplier name
                    name_entry = tk.Entry(modify_window)  # Entry field for entering supplier name
                    name_entry.insert(0, supplier.get_sup_name())  # Insert current name into the entry field
                    name_entry.grid(row=0, column=1)  # Positioning entry field

                    tk.Label(modify_window, text="Phone Number:").grid(row=1, column=0)  # Label for phone number
                    phone_entry = tk.Entry(modify_window)  # Entry field for entering phone number
                    phone_entry.insert(0,
                                       supplier.get_sup_phone_num())  # Insert current phone number into the entry field
                    phone_entry.grid(row=1, column=1)  # Positioning entry field

                    tk.Label(modify_window, text="Address:").grid(row=2, column=0)  # Label for address
                    address_entry = tk.Entry(modify_window)  # Entry field for entering address
                    address_entry.insert(0, supplier.get_sup_address())  # Insert current address into the entry field
                    address_entry.grid(row=2, column=1)  # Positioning entry field

                    # Function to handle modification submission
                    def submit_modification():
                        # Update the supplier object with new details
                        supplier.set_sup_name(name_entry.get())  # Set new supplier name
                        supplier.set_sup_phone_num(phone_entry.get())  # Set new phone number
                        supplier.set_sup_address(address_entry.get())  # Set new address

                        # Display success message
                        messagebox.showinfo("Success",
                                            "Supplier details modified successfully")  # Show a success message dialog box

                        # Close the modification window
                        modify_window.destroy()  # Destroy the window for modifying supplier details

                    # Button to submit modifications
                    submit_button = tk.Button(modify_window, text="Submit",
                                              command=submit_modification)  # Button to submit modifications
                    submit_button.grid(row=3, column=0)  # Positioning the submit button

                    return

            # If supplier with given ID is not found
            messagebox.showerror("Error", "Supplier with the given ID not found")  # Show an error message dialog box

        # Button to modify supplier
        modify_button = tk.Button(self.modify_supplier_window, text="Modify",
                                  command=modify_supplier_inner)  # Button to trigger modification
        modify_button.grid(row=1, column=0)  # Positioning the modify button

        # Button to go back
        back_button = tk.Button(self.modify_supplier_window, text="Back",
                                command=self.modify_supplier_window.destroy)  # Button to close the window
        back_button.grid(row=1, column=1)  # Positioning the back button

    def display_supplier(self):
        # Create a new Toplevel window for displaying a supplier's details
        self.display_supplier_window = tk.Toplevel(self)
        self.display_supplier_window.title("Display Supplier Details")

        # Label and Entry widgets for supplier ID
        tk.Label(self.display_supplier_window, text="Supplier ID:").grid(row=0, column=0)
        sup_id_entry = tk.Entry(self.display_supplier_window)
        sup_id_entry.grid(row=0, column=1)

        # Function to handle displaying supplier details
        def display_supplier_action():
            # Get the supplier ID to display
            sup_id = sup_id_entry.get()

            # Search for the supplier with the given ID
            for supplier in self.suppliers:
                if supplier.get_supID() == sup_id:
                    # Display supplier details in a messagebox or label
                    details = f"Name: {supplier.get_sup_name()}\nPhone: {supplier.get_sup_phone_num()}\nAddress: {supplier.get_sup_address()}"
                    messagebox.showinfo("Supplier Details", details)
                    return

            # If supplier with given ID is not found
            messagebox.showerror("Error", "Supplier with the given ID not found")

        # Button to display supplier details
        display_button = tk.Button(
            self.display_supplier_window, text="Display", command=display_supplier_action)
        display_button.grid(row=1, column=0)

        # Button to go back
        back_button = tk.Button(
            self.display_supplier_window, text="Back", command=self.display_supplier_window.destroy)
        back_button.grid(row=1, column=1)

    # VENUE
    def add_venue(self):
        # Create a new Toplevel window for adding venue details
        self.add_venue_window = tk.Toplevel()
        self.add_venue_window.title("Add Venue")  # Setting title for the window

        # Label and Entry widgets for venue details
        tk.Label(self.add_venue_window, text="Venue ID:").grid(row=0, column=0)  # Label for venue ID
        venue_id_entry = tk.Entry(self.add_venue_window)  # Entry field for entering venue ID
        venue_id_entry.grid(row=0, column=1)  # Positioning entry field

        tk.Label(self.add_venue_window, text="Venue Name:").grid(row=1, column=0)  # Label for venue name
        venue_name_entry = tk.Entry(self.add_venue_window)  # Entry field for entering venue name
        venue_name_entry.grid(row=1, column=1)  # Positioning entry field

        tk.Label(self.add_venue_window, text="Venue Address:").grid(row=2, column=0)  # Label for venue address
        venue_address_entry = tk.Entry(self.add_venue_window)  # Entry field for entering venue address
        venue_address_entry.grid(row=2, column=1)  # Positioning entry field

        tk.Label(self.add_venue_window, text="Contact Number:").grid(row=3, column=0)  # Label for contact number
        contact_num_entry = tk.Entry(self.add_venue_window)  # Entry field for entering contact number
        contact_num_entry.grid(row=3, column=1)  # Positioning entry field

        tk.Label(self.add_venue_window, text="Minimum Guests:").grid(row=4, column=0)  # Label for minimum guests
        min_guests_entry = tk.Entry(self.add_venue_window)  # Entry field for entering minimum guests
        min_guests_entry.grid(row=4, column=1)  # Positioning entry field

        tk.Label(self.add_venue_window, text="Maximum Guests:").grid(row=5, column=0)  # Label for maximum guests
        max_guests_entry = tk.Entry(self.add_venue_window)  # Entry field for entering maximum guests
        max_guests_entry.grid(row=5, column=1)  # Positioning entry field

        def submit_venue():
            # Get values from Entry widgets
            venueID = venue_id_entry.get()  # Retrieve the venue id entered by the user
            venue_name = venue_name_entry.get()  # Retrieve the venue name entered by the user
            venue_address = venue_address_entry.get()  # Retrieve the venue address entered by the user
            venue_contact_num = contact_num_entry.get()  # Retrieve the contact number entered by the user
            min_guests = min_guests_entry.get()  # Retrieve the minimum guests entered by the user
            max_guests = max_guests_entry.get()  # Retrieve the maximum guests entered by the user

            # Create an instance of Venue class with provided details
            venue = Venue(venueID, venue_name, venue_address, venue_contact_num, min_guests,
                          max_guests)  # Create a Venue object

            # Add the venue instance to the list
            self.venues.append(venue)  # Append the new venue to the list of venues

            # Serialize the venue object and store it in a binary file
            with open('venues.pkl', 'ab') as file:  # Open the file in binary append mode
                pickle.dump(venue, file)  # Serialize and write the venue object to the file

            # Display success message
            messagebox.showinfo("Success", "Venue added successfully")  # Show a success message dialog box

            # Close the Toplevel window
            self.add_venue_window.destroy()  # Destroy the window for adding a venue
            # Reset the reference to the window
            self.add_venue_window = None  # Set the window reference to None to indicate it's closed

        # Button to submit venue details
        submit_button = tk.Button(self.add_venue_window, text="Submit",
                                  command=submit_venue)  # Button to submit venue details
        submit_button.grid(row=6, column=0)  # Positioning the submit button

        # Button to go back
        back_button = tk.Button(self.add_venue_window, text="Back",
                                command=self.add_venue_window.destroy)  # Button to close the window
        back_button.grid(row=6, column=1)  # Positioning the back button




















