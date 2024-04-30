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


class Employee(Person):
    '''Class to represent an employee'''
    #Constructor
    def __init__(self, nameP, phone_numP, emailP, empID, role):
        super().__init__(nameP, phone_numP, emailP) #inheriting from person class
        self.__empID = empID
        self.__role = role

    #Setters and getters
    def set_empID(self, empID):
        self.__empID = empID

    def get_empID(self):
        return self.__empID

    def set_role(self, role):
        self.__role = role

    def get_role(self):
        return self.__role