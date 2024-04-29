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
