from abc import ABC, abstractmethod

class ReservationSystem(ABC):
    @abstractmethod
    def search(self):
        pass

    @abstractmethod
    def select(self):
        pass

    @abstractmethod
    def confirm(self):
        pass

    def reserve(self):
        self.search()
        self.select()
        self.confirm()

class HotelReservation(ReservationSystem):
    def search(self):
        print("Căutare hoteluri disponibile")

    def select(self):
        print("Selectare hotel")

    def confirm(self):
        print("Confirmare rezervare hotel")

class TransportReservation(ReservationSystem):
    def search(self):
        print("Căutare opțiuni de transport")

    def select(self):
        print("Selectare opțiune de transport")

    def confirm(self):
        print("Confirmare rezervare transport")

class EventReservation(ReservationSystem):
    def search(self):
        print("Căutare evenimente disponibile")

    def select(self):
        print("Selectare eveniment")

    def confirm(self):
        print("Confirmare rezervare eveniment")

hotel_reservation = HotelReservation()
hotel_reservation.reserve()

print("-------------------------")

transport_reservation = TransportReservation()
transport_reservation.reserve()

print("-------------------------")

event_reservation = EventReservation()
event_reservation.reserve()
