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