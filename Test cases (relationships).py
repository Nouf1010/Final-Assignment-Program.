#Importing all the classes needed from different files
from Aggregation import *
from Composition import *
from Inheritance import *
from Uni import *

#Inheritance 1 (Person + Client) --> done
try:
    # Creating instances of Person and Client classes with user inputs
    while True:
        person_name = input("Enter client's name: ")
        if not person_name.isalpha():
            print("Name should only contain alphabetic characters.")
        else:
            break

    while True:
        phone_num = input("Enter client's phone number: ")
        if not phone_num.isdigit() or len(phone_num) != 10:
            print("Phone number should contain 10 digits.")
        else:
            break

    while True:
        email = input("Enter client's email: ")
        if "@" not in email or "." not in email:
            print("Invalid email format.")
        else:
            break

    clientID = input("Enter client ID: ")

    while True:
        try:
            budget = float(input("Enter client's budget: "))
            if budget < 0:
                print("Budget cannot be negative.")
            else:
                break
        except ValueError:
            print("Budget should be a number.")

    client = Client(person_name, phone_num, email, clientID, budget)

    # Testing getters for Person and Client classes
    print("\nClient Details:")
    print("Name:", client.get_nameP())
    print("Phone Number:", client.get_phone_numP())
    print("Email:", client.get_emailP())
    print("Client ID:", client.get_clientID())
    print("Budget:", client.get_budget())

except ValueError as e:
    print("Error:", e)
finally:
    print("Execution completed.")


#Inheritance 2 (Person + Employee) --> done
try:
    # Creating instances of Person and Employee classes with user inputs
    while True:
        person_name = input("Enter employee's name: ")
        if not person_name.isalpha():
            print("Name should only contain alphabetic characters.")
        else:
            break

    while True:
        phone_num = input("Enter employee's phone number: ")
        if not phone_num.isdigit() or len(phone_num) != 10:
            print("Phone number should contain 10 digits.")
        else:
            break

    while True:
        email = input("Enter employee's email: ")
        if "@" not in email or "." not in email:
            print("Invalid email format.")
        else:
            break

    empID = input("Enter employee ID: ")

    while True:
        role = input("Enter employee's role (manager/planner/coordinator): ").lower()
        if role not in ["manager", "planner", "coordinator"]:
            print("Invalid role. Choose from manager, planner, or coordinator.")
        else:
            break

    employee = Employee(person_name, phone_num, email, empID, role)

    # Testing getters for Person and Employee classes
    print("\nEmployee Details:")
    print("Name:", employee.get_nameP())
    print("Phone Number:", employee.get_phone_numP())
    print("Email:", employee.get_emailP())
    print("Employee ID:", employee.get_empID())
    print("Role:", employee.get_role())

except ValueError as e:
    print("Error:", e)
finally:
    print("Execution completed.")


#Inheritance 3 (Person + Guest) --> done
try:
    # Creating instances of Person and Guest classes with user inputs
    while True:
        person_name = input("Enter guest's name: ")
        if not person_name.isalpha():
            print("Name should only contain alphabetic characters.")
        else:
            break

    while True:
        phone_num = input("Enter guest's phone number: ")
        if not phone_num.isdigit() or len(phone_num) != 10:
            print("Phone number should contain 10 digits.")
        else:
            break

    while True:
        email = input("Enter guest's email: ")
        if "@" not in email or "." not in email:
            print("Invalid email format.")
        else:
            break

    guestID = input("Enter guest ID: ")

    guest = Guest(person_name, phone_num, email, guestID)

    # Testing getters for Person and Guest classes
    print("\nGuest Details:")
    print("Name:", guest.get_nameP())
    print("Phone Number:", guest.get_phone_numP())
    print("Email:", guest.get_emailP())
    print("Guest ID:", guest.get_guestID())

except ValueError as e:
    print("Error:", e)
finally:
    print("Execution completed.")


#Composition (Venue + Event) --> done
def validate_date(date_str):
    try:
        day, month, year = date_str.split('/')
        day, month, year = int(day), int(month), int(year)
        if 1 <= day <= 31 and 1 <= month <= 12 and year >= 1000:
            return True
        return False
    except ValueError:
        return False


def validate_time(time_str):
    try:
        hour, minute, period = time_str[:-6], time_str[3:-3], time_str[-2:]
        hour, minute = int(hour), int(minute)
        if hour < 1 or hour > 12 or minute < 0 or minute > 59 or period not in ['AM', 'PM']:
            return False
        return True
    except ValueError:
        return False

try:
    # Creating an instance of Venue with predefined values
    venueID = "VENUE001"
    venue_name = "Venue A"
    venue_address = "Abu Dhabi, Yas Island"
    venue_contact_num = "0501234561"
    min_guests = 1
    max_guests = 200

    venue = Venue(venueID, venue_name, venue_address, venue_contact_num, min_guests, max_guests)

    # Creating an instance of Event with user inputs
    while True:
        eventID = input("Enter event ID: ")
        if not eventID:
            print("Event ID cannot be empty.")
        else:
            break

    while True:
        event_type = input("Enter event type (wedding/birthday/themed party/graduation): ").lower()
        if event_type not in ["wedding", "birthday", "themed party", "graduation"]:
            print("Invalid event type. Choose from wedding, birthday, themed party, or graduation.")
        else:
            break

    while True:
        event_date = input("Enter event date (DD/MM/YYYY): ")
        if not validate_date(event_date):
            print("Invalid date format. Please enter date in DD/MM/YYYY format.")
        else:
            break

    while True:
        event_time = input("Enter event time (HH:MM AM/PM): ")
        if not validate_time(event_time):
            print("Invalid time format. Please enter time in HH:MM AM/PM format.")
        else:
            break

    while True:
        event_duration = input("Enter event duration (whole day or half day): ").lower()
        if event_duration not in ["whole day", "half day"]:
            print("Invalid duration option. Choose from whole day or half day.")
        else:
            break

    event = Event(eventID, event_type, event_date, event_time, event_duration, venue)

    # Testing getters for Event and Venue classes
    print("\nEvent Details:")
    print("Event ID:", event.get_eventID())
    print("Event Type:", event.get_type())
    print("Event Date:", event.get_date())
    print("Event Time:", event.get_time())
    print("Event Duration:", event.get_duration())
    print("\nVenue Details:")
    print("Venue ID:", venue.get_venueID())  # Using getters to access private attributes
    print("Venue Name:", venue.get_venue_name())
    print("Venue Address:", venue.get_venue_address())
    print("Venue Contact Number:", venue.get_venue_contact_num())
    print("Minimum Guests:", venue.get_min_guests())
    print("Maximum Guests:", venue.get_max_guests())

except ValueError as e:
    print("Error:", e)
finally:
    print("Execution completed.")


#Uni-directional (Client + Event) --> done

def validate_date(date_str):
    try:
        day, month, year = date_str.split('/')
        day, month, year = int(day), int(month), int(year)
        if 1 <= day <= 31 and 1 <= month <= 12 and year >= 1000:
            return True
        return False
    except ValueError:
        return False


def validate_time(time_str):
    try:
        hour, minute, period = time_str[:-6], time_str[3:-3], time_str[-2:]
        hour, minute = int(hour), int(minute)
        if hour < 1 or hour > 12 or minute < 0 or minute > 59 or period not in ['AM', 'PM']:
            return False
        return True
    except ValueError:
        return False

try:
    # Creating instances of Client and Event classes with user inputs
    while True:
        client_name = input("Enter client's name: ")
        if not client_name.isalpha():
            print("Name should only contain alphabetic characters.")
        else:
            break

    while True:
        client_phone = input("Enter client's phone number (10 digits): ")
        if not client_phone.isdigit() or len(client_phone) != 10:
            print("Phone number should be a 10-digit number.")
        else:
            break

    while True:
        client_email = input("Enter client's email: ")
        if '@' not in client_email or '.' not in client_email:
            print("Invalid email address.")
        else:
            break

    while True:
        client_ID = input("Enter client's ID: ")
        if not client_ID:
            print("Client ID cannot be empty.")
        else:
            break

    while True:
        client_budget = input("Enter client's budget: ")
        try:
            client_budget = float(client_budget)
            break
        except ValueError:
            print("Budget should be a number.")

    client = Client(client_name, client_phone, client_email, client_ID, client_budget)

    while True:
        event_ID = input("Enter event ID: ")
        if not event_ID:
            print("Event ID cannot be empty.")
        else:
            break

    while True:
        event_type = input("Enter event type (wedding, birthday, themed party, graduation): ").lower()
        if event_type not in ["wedding", "birthday", "themed party", "graduation"]:
            print("Invalid event type. Choose from: wedding, birthday, themed party, graduation")
        else:
            break

    while True:
        event_date = input("Enter event date (MM/DD/YYYY): ")
        if not event_date or not validate_date(event_date):
            print("Invalid date format or value. Please enter in MM/DD/YYYY format.")
        else:
            break

    while True:
        event_time = input("Enter event time (HH:MM AM/PM): ")
        if not event_time or not validate_time(event_time):
            print("Invalid time format or value. Please enter in HH:MM AM/PM format.")
        else:
            break

    while True:
        event_duration = input("Enter event duration (whole day or half day): ").lower()
        if event_duration not in ["whole day", "half day"]:
            print("Invalid duration option. Choose from: whole day, half day")
        else:
            break

    # Creating an Event instance and associating it with the Client instance
    event = Event(event_ID, event_type, event_date, event_time, event_duration, [])
    event.set_client(client)

    # Testing getters for Event and Client classes
    print("\nEvent Details:")
    print("Event ID:", event.get_eventID())
    print("Event Type:", event.get_type())
    print("Event Date:", event.get_date())
    print("Event Time:", event.get_time())
    print("Event Duration:", event.get_duration())
    print("\nAssociated Client Details:")
    print("Client Name:", event.get_client().get_nameP())
    print("Client Phone:", event.get_client().get_phone_numP())
    print("Client Email:", event.get_client().get_emailP())
    print("Client ID:", event.get_client().get_clientID())
    print("Client Budget:", event.get_client().get_budget())

except ValueError as e:
    print("Error:", e)
finally:
    print("Execution completed.")


#Aggregation 1 (Event + Guest) --> done
from Aggregation import Event  # Importing event class from the aggregation file

# Function to validate date format (MM/DD/YYYY)
def validate_date(date_str):
    try:
        day, month, year = date_str.split('/')
        day, month, year = int(day), int(month), int(year)
        if 1 <= day <= 31 and 1 <= month <= 12 and year >= 1000:
            return True
        return False
    except ValueError:
        return False


def validate_time(time_str):
    try:
        hour, minute, period = time_str[:-6], time_str[3:-3], time_str[-2:]
        hour, minute = int(hour), int(minute)
        if hour < 1 or hour > 12 or minute < 0 or minute > 59 or period not in ['AM', 'PM']:
            return False
        return True
    except ValueError:
        return False

# Function to validate duration (whole day or half day)
def validate_duration(duration):
    return duration.lower() in ['whole day', 'half day']

# Function to validate phone number (10 digits)
def validate_phone(phone):
    return len(phone) == 10 and phone.isdigit()

# Function to validate email format
def validate_email(email):
    return '@' in email and '.' in email

try:
    # Creating an instance of Venue with predefined values
    venueID = "VENUE001"
    venue_name = "Venue A"
    venue_address = "Abu Dhabi, Yas Island"
    venue_contact_num = "0501234561"
    min_guests = 1
    max_guests = 200

    venue = Venue(venueID, venue_name, venue_address, venue_contact_num, min_guests, max_guests)

    # Creating an instance of Event with user inputs
    eventID = input("Enter event ID: ")

    # Validating event type
    while True:
        event_type = input("Enter event type (wedding/birthday/themed party/graduation): ").lower()
        if event_type not in ["wedding", "birthday", "themed party", "graduation"]:
            print("Invalid event type. Choose from wedding, birthday, themed party, or graduation.")
        else:
            break

    # Validating event date
    while True:
        event_date = input("Enter event date (MM/DD/YYYY): ")
        if not validate_date(event_date):
            print("Invalid date format. Please enter date in MM/DD/YYYY format.")
        else:
            break

    # Validating event time
    while True:
        event_time = input("Enter event time (HH:MM AM/PM): ")
        if not validate_time(event_time):
            print("Invalid time format. Please enter time in HH:MM AM/PM format.")
        else:
            break

    # Validating event duration
    while True:
        event_duration = input("Enter event duration (whole day/half day): ")
        if not validate_duration(event_duration):
            print("Invalid duration. Please enter either 'whole day' or 'half day'.")
        else:
            break

    event = Event(eventID, event_type, event_date, event_time, event_duration, venue)

    # Creating instances of Guest
    guest_list = []
    num_guests = int(input("Enter the number of guests: "))
    for i in range(num_guests):
        guest_name = input(f"Enter guest {i+1} name: ")
        while not guest_name.isalpha():
            print("Invalid name. Please enter only alphabetic characters.")
            guest_name = input(f"Enter guest {i+1} name: ")

        guest_phone = input(f"Enter guest {i+1} phone number: ")
        while not validate_phone(guest_phone):
            print("Invalid phone number. Please enter 10-digit phone number.")
            guest_phone = input(f"Enter guest {i+1} phone number: ")

        guest_email = input(f"Enter guest {i+1} email: ")
        while not validate_email(guest_email):
            print("Invalid email format. Please enter a valid email address.")
            guest_email = input(f"Enter guest {i+1} email: ")

        guestID = f"GUEST00{i+1}"
        guest = Guest(guest_name, guest_phone, guest_email, guestID)
        guest_list.append(guest)

    # Adding guests to the event
    for guest in guest_list:
        event.add_guest(guest)

    # Testing getters for Event and Venue classes
    print("\nEvent Details:")
    print("Event ID:", event.get_eventID())
    print("Event Type:", event.get_type())
    print("Event Date:", event.get_date())
    print("Event Time:", event.get_time())
    print("Event Duration:", event.get_duration())
    print("\nVenue Details:")
    print("Venue ID:", venue.get_venueID())  # Using getters to access private attributes
    print("Venue Name:", venue.get_venue_name())
    print("Venue Address:", venue.get_venue_address())
    print("Venue Contact Number:", venue.get_venue_contact_num())
    print("Minimum Guests:", venue.get_min_guests())
    print("Maximum Guests:", venue.get_max_guests())

    # Testing getter for Guest class
    print("\nGuest Details:")
    for i, guest in enumerate(guest_list):
        print(f"Guest {i+1} ID:", guest.get_guestID())
        print(f"Guest {i+1} Name:", guest.get_nameP())
        print(f"Guest {i+1} Phone Number:", guest.get_phone_numP())
        print(f"Guest {i+1} Email:", guest.get_emailP())

except ValueError as e:
    print("Error:", e)
finally:
    print("Execution completed.")


#Aggregation 2 (Venue + Supplier) --> done

from Aggregation import Venue  # Importing event class from the aggregation file
def validate_supplier_phone(phone):
    return len(phone) == 10 and phone.isdigit()

try:
    # Creating an instance of Venue with predefined values
    venueID = "VENUE001"
    venue_name = "Venue A"
    venue_address = "Abu Dhabi, Yas Island"
    venue_contact_num = "0501234561"
    min_guests = 1
    max_guests = 200

    venue = Venue(venueID, venue_name, venue_address, venue_contact_num, min_guests, max_guests)

    # Creating instances of Supplier with user inputs
    num_suppliers = int(input("Enter the number of suppliers: "))
    for i in range(num_suppliers):
        print(f"\nSupplier {i+1}:")
        supID = input("Enter supplier ID: ")
        sup_name = input("Enter supplier name: ")
        sup_phone_num = input("Enter supplier phone number: ")
        while not validate_supplier_phone(sup_phone_num):
            print("Invalid phone number. Please enter a 10-digit phone number.")
            sup_phone_num = input("Enter supplier phone number: ")
        sup_address = input("Enter supplier address: ")

        supplier = Supplier(supID, sup_name, sup_phone_num, sup_address)
        venue.add_supplier(supplier)

    # Displaying venue details along with associated suppliers
    print("\nVenue Details:")
    print("Venue ID:", venue.get_venueID())
    print("Venue Name:", venue.get_venue_name())
    print("Venue Address:", venue.get_venue_address())
    print("Venue Contact Number:", venue.get_venue_contact_num())
    print("Minimum Guests:", venue.get_min_guests())
    print("Maximum Guests:", venue.get_max_guests())

    print("\nSuppliers:")
    for i, supplier in enumerate(venue.get_suppliers()):
        print(f"\nSupplier {i+1} Details:")
        print("Supplier ID:", supplier.get_supID())
        print("Supplier Name:", supplier.get_sup_name())
        print("Supplier Phone Number:", supplier.get_sup_phone_num())
        print("Supplier Address:", supplier.get_sup_address())

except ValueError as e:
    print("Error:", e)
finally:
    print("Execution completed.")

