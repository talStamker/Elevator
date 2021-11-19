import math


class Elevator:

   #constructor
    def __init__(self,id,speed,minF,maxF,closeTime,openTime,startTime,stopTime,end=0,index=0):
        self.listOfSection=[]
        self.id=id
        self.speed=speed
        self.minF=minF
        self.maxF=maxF
        self.closeTime=closeTime
        self.openTime=openTime
        self.startTime=startTime
        self.stopTime=stopTime
        self.time=0
        self.end=0
        self.index=index

    # how much time take to the section with this elevator
    def timeOfSection(self,section):
        time=abs(section.maxOfSection-section.minOfSection)/self.speed
        i=0
        while(i<section.numberOfStops):
            time = time +self.openTime + self.startTime + self.closeTime+ self.stopTime
            i=i+1
        return time

    #  how much time it take to th elevator to end this section
    def TimeToEnd(self,section):
        time =self.time
        ariveTimeToSection=0
        if (len(self.listOfSection) == 0):
            ariveTimeToSection = time + (abs(0 - section.listOfCall[0].callArray[2])) / self.speed
        else:
            ariveTimeToSection = time + (
                abs(section.listOfCall[0].callArray[2] - self.end)) / self.speed

        if ariveTimeToSection>section.listOfCall[0].callArray[1]:
                time=time+ariveTimeToSection
        else:
                time = section.listOfCall[0].callArray[1]

        time = time + self.timeOfSection(section)
        return time

    #this function add section to elevator
    def add(self, section):
        self.time = self.TimeToEnd(section)
        if len(self.listOfSection)!=0:
            self.end=section.endOfSection
        self.listOfSection.append(section)

    # how much time it will take to elevator arive the source in the section
    def timeOfStop(self,section,call):
        start=0
        if(section.state==1):
            start=section.minOfSection
        else:
            start=section.maxOfSection
        time = abs(start - call.callArray[2]) / self.speed
        i = 0
        while (i < section.Levels(call.callArray[2])):
            time = time + self.openTime + self.startTime + self.closeTime + self.stopTime
            i = i + 1
        return time

   # how much time it will take to elevator arive the source
    def timeToSource(self,section,call):
        time = self.time
        ariveTimeToSection = 0
        if (len(self.listOfSection) == 0):
            ariveTimeToSection = time + (abs(0 - section.listOfCall[0].callArray[2])) / self.speed
        else:
            ariveTimeToSection = time + (
                abs(section.listOfCall[0].callArray[2] - self.end)) / self.speed

        if ariveTimeToSection > section.listOfCall[0].callArray[1]:
            time = time + ariveTimeToSection
        else:
            time = section.listOfCall[0].callArray[1]
        time = time + self.timeOfStop(section,call)
        return time
