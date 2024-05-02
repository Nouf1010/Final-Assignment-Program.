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
