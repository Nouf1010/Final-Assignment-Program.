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