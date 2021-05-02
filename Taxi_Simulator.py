
SilverServiceTaxi = 0
TAXI_CHOICE=0
Odometer = 0
Fuel = 100
Current_Taxi = None
print("Let's Drive ")
Option = input("q)uit, c)hoose taxi, d)rive").title()
TAXI = [("Prius",100), SilverServiceTaxi("Limo",100,2),SilverServiceTaxi("Hummer",200,4)]

while Option == "q":
    if Option == "c":
        Choose_Taxi()
    elif Option == "d":
        drive()
    else:
        quit()


def Choose_Taxi():
    print (taxis)
    TAXI_CHOICE = input("Which Taxi Would you Like to take")
    print("You have selected",TAXI_CHOICE)

def drive():
    Distance = input("How far would you like to Drive?")
    Odometer = Odometer + Distance
    Fuel = Fuel - Distance
    print("You have",Fuel,"Remaining")
    if fuel <= 0:
        Print("You are out of Fuel")

def Quit():
    print("You have travelled",Odometer)
    total_Cost = Odometer *2.3
    print("Your Total Cost for Taxi Fare is",total_Cost)