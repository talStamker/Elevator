import unittest
from Call import Call
from  Building import Building
from  Elevator import Elevator
from Section import Section
from Control import Control


class MyTestCase(unittest.TestCase):
    def test_something(self):
        call1=Call(["Elevator call",15.74901825,0,-6,0,-1])
        call2 = Call(["Elevator call", 15.74901825, 0, 6, 0, -1])
        call3 = Call(["Elevator call", 15.74901825, 0, 12, 0, -1])
        call4 = Call(["Elevator call", 200.74901825, 0, 100, 0, -1])
        listcall=[call1,call3,call2]
        call5 = Call(["Elevator call", 15.74901825, 0, 12, 0, 0])
        data={"_minFloor": -10,"_maxFloor": 100,"_elevators": [{"_id": 0,"_speed": 3.0, "_minFloor": -10,"_maxFloor": 100,
      "_closeTime": 2.0,
      "_openTime": 2.0,
      "_startTime": 3.0,
      "_stopTime": 3.0
         },
    {
      "_id": 1,
      "_speed": 7.0,
      "_minFloor": -10,
      "_maxFloor": 100,
      "_closeTime": 1.4285714285714286,
      "_openTime": 1.4285714285714286,
      "_startTime": 2.142857142857143,
      "_stopTime": 2.142857142857143
           }
          ]
          }
        c=Control(data,listcall)
        c.upDateCall()
        arrs=c.Getlist()
        for x in c.Getlist():
            self.assertNotEqual(x.Tavili()[5],-1,True)
        self.assertEqual(arrs[1].Tavili()[5],arrs[2].Tavili()[5],True)
        self.assertNotEqual(arrs[0].Tavili()[5], arrs[2].Tavili()[5],True)
        listcall.append(call4)


        data = {"_minFloor": -10, "_maxFloor": 100,
                "_elevators": [{"_id": 0, "_speed": 0.0000000000000001, "_minFloor": -10, "_maxFloor": 100,
                                "_closeTime": 2.0,
                                "_openTime": 2.0,
                                "_startTime": 3.0,
                                "_stopTime": 3.0
                                },
                               {
                                   "_id": 1,
                                   "_speed": 100000.0,
                                   "_minFloor": -10,
                                   "_maxFloor": 100,
                                   "_closeTime": 1.4285714285714286,
                                   "_openTime": 1.4285714285714286,
                                   "_startTime": 2.142857142857143,
                                   "_stopTime": 2.142857142857143
                               }
                               ]
                }
        c = Control(data, listcall)
        c.upDateCall()
        for x in c.Getlist():
            self.assertNotEqual(x.Tavili()[5], 0, True)
    # def test_equal_call(self):
    #     call3 = Call(["Elevator call", 15.74901825, 0, 12, 0, -1])
    #     call5 = Call(["Elevator call", 15.74901825, 0, 12, 0, 0])
    #     call1 = Call(["Elevator call", 15.74901825, 0, -6, 0, -1])
    #     boo=Control.equalCall(call5,call3)
    #     boo2 = Control.equalCall(call5, call1)
    #     self.assertEqual(boo,True,True)
    #     self.assertNotEqual(boo2, True, True)


if __name__ == '__main__':
    unittest.main()
