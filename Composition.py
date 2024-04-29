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