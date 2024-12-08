# Elevator
### This task deals with the offline problem of elevators
## How to run this?
### create json file and edit it to something in a form like this:
<div>
  <pre>
    <code id="codeBlock">
{
  "_minFloor": 0,
  "_maxFloor": 10,
  "_elevators": [
    {"_id": 1, "_speed": 1.0, "_minFloor": 0, "_maxFloor": 10, "_closeTime": 1.0, "_openTime": 1.0, "_startTime": 1.0, "_stopTime": 1.0},
    {"_id": 2, "_speed": 1.5, "_minFloor": 0, "_maxFloor": 10, "_closeTime": 1.0, "_openTime": 1.0, "_startTime": 1.0, "_stopTime": 1.0}
  ]
}
    </code>
  </pre>
  <button onclick="copyCode()">Copy Code</button>
</div>

<script>
function copyCode() {
    const code = document.getElementById('codeBlock').innerText;
    navigator.clipboard.writeText(code).then(() => {
        alert('Code copied to clipboard!');
    });
}
</script>
### lets explain about the files:
## Call.py:
### elemnets:
#### self.callArray = [ElevatorCall, timeForCall, source, Dest, status, index]
#### ElevatorCall="ElevatorCall"
#### timeForCall- is type float and this is the time that the call was call.
#### source- The source floor of the call by type int.
#### Dest - The dest floor of the call by type int.
#### status - The status of call by type int.
#### index- index of the elevator that was allocated to the call
### function:
#### def Tavili(self):- bring self.callArray
## Section.py:
### elemnets:
#### self.listOfCall - The list of call of that section.
#### self.state - This describes if the section is for going down(-1) or up (1) in elevator. 
####  self.minOfSection- The minfloor of the section.
#### self.maxOfSection- The maxfloor of the section.
#### self.endOfSection - The floor that the section end in.
#### self.numberOfStops - The number of stops in that section.
### function:
#### def updatminMax(self, call):- This function updates maxOfSection and minOfSection and endOfSection if needs i.e the call out of the range.
#### def updateStop(self,call):- If the section doesnt already stop in source and dest it update numberOfStops if needs more stop for this call.
#### def add(self, call):- Add the call to listOfCall update minOfSection and maxOfSection by updatminMax function, and update numberOfStops by updateStop
#### def clear(self):- This function clear listOfCall.
#### def Levels(self,L):-count how much stop there is in the section between minOfSection to L floor.
## Elevator.py:
### elemnets:
#### self.listOfSection- list of section that the elevator need to do.
#### self.id- The id of the elvator
#### self.speed- The speed of the elevator
#### self.minF- The min floor that the elevator can arive to.
#### self.maxF- The max floor that the elevator can arive to.
#### self.closeTime- The time that take the elavtor close the door.
#### self.openTime- The time that take the elavtor close the door.
#### self.startTime- The time that take the elavtor start moving.
#### self.stopTime- The time that take the elavtor stop moving.
#### self.time- The time that take the elvator end all it's sections.
#### self.end- The floor that the elevator stop after it do all it's sections.
#### self.index- The index of elevator
### function:
#### def timeOfSection(self,section):- This function get section and calculate how much time it will take the elevator do this section.
#### def TimeToEnd(self,section):- This function get section and calculate how much time it will take the elevator arive this section after it do all it's sections or wait for the first call in section to be called(timeForCall) and to do this section. it give the time from now to the time that the elevator do all it's sections arive that section and end it.
#### def add(self, section):- Add the section to listOfSection update time by TimeToEnd function and end to section.endOfSection.
#### def timeOfStop(self,section,call):- This function get section and call and calculate how much time it will take the elevator get the source of call (the call in the section) after it do the section and all its stop untill it get the source of the call.
#### def timeToSource(self,section,call):- This function get section and call and calculate how much time it will take the elevator get the source of call (the call in the section) after it do all its sections arive this section and do all its stop untill it get the source of the call.
## Building.py:
### elemnets:
#### self.minFloorOfB- The min floor of the building.
#### self.maxFloorOfB- The max floor of the building.
#### self.E- The list of elvators that exist in that building.
### function:
#### GetElevatorlist(self):- This function bring copy of E.
## Control.py:
### elemnets:
#### self.B- The building that update to what is written in data (the same min and max end elevators).
#### self.calls- list of all call that need to be addressed sort by there timeForCall.
### function:
#### def timeForCall(self, n):- This function get call and return it's timeForCall.
#### def timeForElevator(self, n):- This function get elevator and return it's time.
#### def createElevators(self):- This function sort the elvator of the building by there time.
#### def isTheSameDirection(self, section, call):- This function get section and call and check if there direction is the same. i.e if both going down or both going up.
#### def isInRage(self, section, call):- This function check if the call is in the range of the section, i.e the source and dest between minOfSection and maxOfSection.
#### def isInTime(self, section, call):- This function checks if the elevator that have the longest time the time that it will take it willed it's section and arive the section do it and untill getting the source of call bigger than timeForCall if yes true else false.
#### def createSections(self):- This function create sections list according to calls. it pass all the call if the call out of range of building (source or dest not between minFloorOfB and maxFloorOfB) the function will not add it to section.The function pass all calls, If there is already exist section that the call in its range (isInRage) and the time is in time (isInRage) and (isTheSameDirection) add the call to the section else create another section.
####  allocateElevator(self):- This function call createSections and call createElevators and pass all sections and check what is the elevator that do the section in the min time. i.e it calculate which elevator do which sections.
#### def equalCall(self, call1, call2):-checks if the call are equals.
#### def Getlist(self):- return copy of calls
#### def upDateCall(self):- update the index of elevator to the correct call
## Ex1.py:
### function:
if __name__ == '__main__':- This function read the to data the json file of the building, read the calls from csv file to callsList, create Control object and call upDateCall and after it update the calls, write them in the file that the user ask for.










