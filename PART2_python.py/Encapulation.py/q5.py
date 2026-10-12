class MovieTheater:
    def __init__(self, movie_name, total_seats):
        self.__movie_name = movie_name
        self.__total_seats = total_seats
        self.__available_seats = total_seats
        self.__booked_seats = 0

    def book_tickets(self, quantity):
        if quantity <= 0:
            print("Invalid Quantity")

        elif quantity > self.__available_seats:
            print("Not Enough Seats")

        else:
            self.__available_seats -= quantity
            self.__booked_seats += quantity
            print("Tickets Booked Successfully")

    def cancel_tickets(self, quantity):
        if quantity <= 0 or quantity > self.__booked_seats:
            print("Invalid Cancellation")

        else:
            self.__available_seats += quantity
            self.__booked_seats -= quantity
            print("Cancellation Successful")

    def show_available(self):
        print(self.__available_seats)

    def show_booked(self):
        print(self.__booked_seats)


M = MovieTheater("Avengers", 30)

M.book_tickets(20)
M.cancel_tickets(20)

M.show_available()
M.show_booked()