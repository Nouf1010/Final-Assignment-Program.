class Person:
    '''Class to represent a person'''
    #Constructor
    def __init__(self, nameP, phone_numP, emailP):
        self._nameP = nameP
        self._phone_numP = phone_numP
        self._emailP = emailP

    #Setters and getters
    def set_nameP(self, nameP):
        self._nameP = nameP

    def get_nameP(self):
        return self._nameP

    def set_phone_numP(self, phone_numP):
        self._phone_numP = phone_numP

    def get_phone_numP(self):
        return self._phone_numP

    def set_emailP(self, emailP):
        self._emailP = emailP

    def get_emailP(self):
        return self._emailP