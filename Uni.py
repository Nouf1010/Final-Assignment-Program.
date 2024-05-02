#importing the inheritance file so that we can use the class client
from Inheritance import *
class Client(Person):
    '''Class to represent a client'''
    #Constructor
    def __init__(self, nameP, phone_numP, emailP, clientID, budget):
        super().__init__(nameP, phone_numP, emailP) #inheriting from person class
        self.__clientID = clientID
        self.__budget = budget

    #Setters and getters
    def set_clientID(self, clientID):
        self.__clientID = clientID

    def get_clientID(self):
        return self.__clientID

    def set_budget(self, budget):
        self.__budget = budget

    def get_budget(self):
        return self.__budget


class Event:
    '''Class to represent an event'''
    # Constructor
    def __init__(self, eventID, type, date, time, duration, venue, guest_list):
        self.__eventID = eventID
        self.__type = type
        self.__date = date
        self.__time = time
        self.__duration = duration
        self.__venue = venue
        self.__guest_list = guest_list
        self.__client = None  # Reference to client (unidirectional relationship)

    # Method to set the client for the event
    def set_client(self, client):
        self.__client = client

    # Method to get the client for the event
    def get_client(self):
        return self.__client

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