from .Constant import Constant


class Reservation:
    NR = -1


    def __init__(self, nr: int, day: int, time: int, room: int):
        Reservation.NR = nr
        self.Day = day
        self.Time = time
        self.Room = room
        self._index = self.Day * Reservation.NR * Constant.DAY_HOURS + self.Room * Constant.DAY_HOURS + self.Time


    def __hash__(self) -> int:
        return self._index


    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        return self._index == other._index
            
    def __ne__(self, other):
        return not self.__eq__(other)
        