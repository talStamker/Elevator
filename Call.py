class Call:
    # constructor
    def __init__(self, line=[]):
        ElevatorCall = line[0]
        timeForCall = float(line[1])
        source = int(line[2])
        Dest = int(line[3])
        status = int(line[4])
        index = int(line[5])
        self.callArray = [ElevatorCall, timeForCall, source, Dest, status, index]

    # this function give the cakkArray
    def Tavili(self):
        return self.callArray
