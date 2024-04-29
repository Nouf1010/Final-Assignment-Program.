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
