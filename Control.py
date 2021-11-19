import json
import csv
from Building import Building
from Elevator import Elevator
from Section import Section
from Call import Call


class Control:
    # help function for constractor
    def timeForCall(self, n):
        return n.callArray[1]

    # constractor
    def __init__(self, data={}, callsLists=[]):
        self.B = Building(data["_minFloor"], data["_maxFloor"], data["_elevators"])
        self.calls = callsLists.copy()
        self.calls.sort(key=self.timeForCall)

    # help do sort
    def timeForElevator(self, n):
        return n.time

    # this function create list of elevator
    # and sort it
    def createElevators(self):
        E = self.B.GetElevatorlist()
        E.sort(key=self.timeForElevator)
        return E

    # This function checks whether the reading is in a state like SECTION
    def isTheSameDirection(self, section, call):
        if (section.state == 1 and call.callArray[2] < call.callArray[3]):
            return True
        if (section.state == -1 and call.callArray[2] > call.callArray[3]):
            return True
        return False

    # This function checks whether the source is in the middle of the section
    def isInRage(self, section, call):
        if (call.callArray[2] >= section.minOfSection and call.callArray[2] <= section.maxOfSection):
            return True
        return False

    # help function witch find whether this call's time is lower than the arive time of elevator to the source
    def isInTime(self, section, call):
        E = self.createElevators()
        e = E[len(E) - 1]
        if (e.timeToSource(section, call) > call.callArray[1]):
            return True
        return False

    # this function create section with legality
    def createSections(self):
        sections = []
        for i in range(len(self.calls)):
            isAdd = False
            if (self.calls[i].callArray[2] < self.B.minFloorOfB or self.calls[i].callArray[3] < self.B.minFloorOfB or
                    self.calls[i].callArray[2] > self.B.maxFloorOfB or self.calls[i].callArray[3] > self.B.maxFloorOfB):
                continue
            for j in range(len(sections)):
                if (self.isInRage(sections[j], self.calls[i]) and self.isTheSameDirection(sections[j], self.calls[
                    i]) and self.isInTime(sections[j], self.calls[i])):
                    sections[j].add(self.calls[i])
                    isAdd = True
            if (isAdd == False):
                sections.append(Section(self.calls[i]))
        return sections.copy()

    #this function allocate elevator to the most lucrative section
    def allocateElevator(self):
        sections = self.createSections()
        elevators = self.createElevators()
        for x in sections:
            min = elevators[0].TimeToEnd(x)
            elevator = elevators[0]
            for y in elevators:
                if (min > y.TimeToEnd(x)):
                    min = y.TimeToEnd(x)
                    elevator = y
            elevator.add(x)
        return elevators.copy()

    #help function find if the calss are equaal
    def equalCall(self, call1, call2):
        if (call1.callArray[1] == call2.callArray[1] and call1.callArray[2] == call2.callArray[2] and call1.callArray[
            3] == call2.callArray[3] and call1.callArray[4] == call2.callArray[4]):
            return True
        return False
    #copy constructor
    def Getlist(self):
        return self.calls.copy()

    #this function take the section and update the list
    def upDateCall(self):
        elevators = self.allocateElevator()
        for x in elevators:
            for y in x.listOfSection:
                for z in y.listOfCall:
                    for w in self.calls:
                        if self.equalCall(z, w):
                            w.callArray[5] = x.index
                            print(x.index)
