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

class Event:
    '''Class to represent an event'''
    # Constructor
    def __init__(self, eventID, type, date, time, duration, venue, guest_list=[]):
        self.__eventID = eventID
        self.__type = type
        self.__date = date
        self.__time = time
        self.__duration = duration
        self.__venue = venue  # Composition relationship because venue is an object in the event class
        self.__guest_list = guest_list

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
