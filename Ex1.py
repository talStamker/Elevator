import sys
import json
import csv

from Call import Call
from Control import Control
from Elevator import Elevator
import Building
if __name__ == '__main__':
    with open(sys.argv[1], 'r') as f:
      data = json.load(f)

    with open(sys.argv[2], 'r') as file:
      cvs_reader = csv.reader(file)
      callsList=[]
      for line in cvs_reader:
          callsList.append(Call(line))
    test=Control(data,callsList)
    test.upDateCall()
    output=test.Getlist()
    listprin=[]

    with open(sys.argv[3], 'w',newline="") as cvskos:
        csvwriter = csv.writer(cvskos)
        for x in output:
         listprin.append(x.Tavili())
        csvwriter.writerows(listprin)
    print("done")



