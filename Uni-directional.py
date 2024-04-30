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