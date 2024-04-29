#importing the inheritance file so that we can use the class guest
from Inheritance import *
#Aggregation 1 (Event + Guest)
class Event:
    '''Class to represent an event'''
    #Constructor
    def __init__(self, eventID, type, date, time, duration, venue, guest_list = []):
        self.__eventID = eventID
        self.__type = type
        self.__date = date
        self.__time = time
        self.__duration = duration
        self.__venue = venue
        self.__guest_list = guest_list  # Aggregation relationship (A list to hold guest objects)

    # Method to add a guest to the event
    def add_guest(self, guest):
        self.__guest_list.append(guest)

    # Method to remove a guest from the event
    def remove_guest(self, guest):
        if guest in self.__guest_list:
            self.__guest_list.remove(guest)
        else:
            print("Guest not found in the guest list.")

    #Setters and getters
    def set_eventID(self, eventID):
        self.__eventID = eventID

    def get_eventID(self):
        return self.__eventID

    def set_type(self, type):
        self.__type = type

    def get_type(self):
        return self.__type

    def set_date(self, date):
        self.__date = date

    def get_date(self):
        return self.__date

    def set_time(self, time):
        self.__time = time

    def get_time(self):
        return self.__time

    def set_duration(self, duration):
        self.__duration = duration

    def get_duration(self):
        return self.__duration

    def set_venue(self, venue):
        self.__venue = venue

    def get_venue(self):
        return self.__venue

    def set_guest_list(self, guest_list):
        self.__guest_list = guest_list

    def get_guest_list(self):
        return self.__guest_list

 #Add guest class here
class Guest(Person):
    '''Class to represent a guest'''
    # Constructor
    def __init__(self, nameP, phone_numP, emailP, guestID):
        super().__init__(nameP, phone_numP, emailP)  # inheriting from person class
        self.__guestID = guestID

    # Setters and getters
    def set_guestID(self, guestID):
        self.__guestID = guestID

    def get_guestID(self):
        return self.__guestID

#Aggregation 2 (Venue + Supplier)
class Venue:
    '''Class to represent a venue'''
    #Constructor
    def __init__(self, venueID, venue_name, venue_address, venue_contact_num, min_guests, max_guests):
        self.__venueID = venueID
        self.__venue_name = venue_name
        self.__venue_address = venue_address
        self.__venue_contact_num = venue_contact_num
        self.__min_guests = min_guests
        self.__max_guests = max_guests
        self.__suppliers = []  # List to hold supplier objects

    # Method to add a supplier
    def add_supplier(self, supplier):
        self.__suppliers.append(supplier)

    # Method to remove a supplier
    def remove_supplier(self, supplier):
        self.__suppliers.remove(supplier)

    #Setters and getters
    def set_venueID(self, venueID):
        self.__venueID = venueID

    def get_venueID(self):
        return self.__venueID

    def set_venue_name(self, venue_name):
        self.__venue_name = venue_name

    def get_venue_name(self):
        return self.__venue_name

    def set_venue_address(self, venue_address):
        self.__venue_address = venue_address

    def get_venue_address(self):
        return self.__venue_address

    def set_venue_contact_num(self, venue_contact_num):
        self.__venue_contact_num = venue_contact_num

    def get_venue_contact_num(self):
        return self.__venue_contact_num

    def set_min_guests(self, min_guests):
        self.__min_guests = min_guests

    def get_min_guests(self):
        return self.__min_guests

    def set_max_guests(self, max_guests):
        self.__max_guests = max_guests

    def get_max_guests(self):
        return self.__max_guests