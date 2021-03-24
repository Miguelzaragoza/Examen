class Boeing(Aircraft):
    def __init__(self, registration, airline):        
        self.__model = "Boeing 777"
        self.__num_rows = 56
        self.__num_seats_per_row = 9
        self.__airline = airline
        super().__init__(registration, self.__model, self.__num_rows, self.__num_seats_per_row)
    def get_airline(self):
        return self.__airline