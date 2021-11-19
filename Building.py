from Elevator import Elevator


class Building:
    # constructor
    def __init__(self, minFloor, maxFloor, elevators):
        self.minFloorOfB = minFloor
        self.maxFloorOfB = maxFloor
        self.E = []
        i = 0
        for x in elevators:
            self.E.append(
                Elevator(x["_id"], x["_speed"], x["_minFloor"], x["_maxFloor"], x["_closeTime"], x["_openTime"],
                         x["_startTime"], x["_stopTime"], 0, i))
            i = i + 1

    # this function give the elevator list
    def GetElevatorlist(self):
        return self.E.copy()
