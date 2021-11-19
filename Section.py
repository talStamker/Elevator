import math
from Call import Call
class Section:
    #constructor
    def __init__(self, call):
        self.listOfCall = []
        self.listOfCall.append(call)
        if call.callArray[3] > call.callArray[2]:
            self.state = 1
        else:
            self.state = -1
        if self.state == 1:
            self.minOfSection=call.callArray[2]
            self.maxOfSection = call.callArray[3]
        else:
            self.minOfSection = call.callArray[3]
            self.maxOfSection = call.callArray[2]
        self.endOfSection = call.callArray[3]
        self.numberOfStops=2


  #Updates maximum and minimum only of the target
    # because he is the only one who can change them (the source will not change them)
    def updatminMax(self, call):
        if self.minOfSection > call.callArray[3]:
            self.minOfSection = call.callArray[3]
            self.endOfSection = self.minOfSection
        if self.maxOfSection < call.callArray[3]:
            self.maxOfSection = call.callArray[3]
            self.endOfSection = self.maxOfSection

    def updateStop(self,call):
        isSource=True
        isDest=True
        for x in self.listOfCall:
            if(x.callArray[2]==call.callArray[2] or x.callArray[3]==call.callArray[2]):
                isSource=False
            if(x.callArray[2]==call.callArray[3] or x.callArray[3]==call.callArray[3]):
                isDest=False
            if( isDest==False and isSource==False):
                break
        if(isSource):
            self.numberOfStops=self.numberOfStops+1
        if(isDest):
            self.numberOfStops=self.numberOfStops+1

    def add(self, call):
        self.updatminMax(call)
        self.listOfCall.append(call)
        self.updateStop(call)

    def clear(self):
        self.listOfCall.clear()
#change
    def Levels(self,L):
        count=0
        for i in range(self.minOfSection,L+1):
            isExists=False
            for x in self.listOfCall:
                if x.callArray[2]==i or x.callArray[3]==i:
                    count=count+1
                    break
        return count

