class ParkingGarage():
    def __init__(self, tickets, parkingSpaces, currentTicket):
        self.tickets = tickets
        self.parkingSpaces = parkingSpaces
        self.currentTicket = currentTicket

    def takeTicket(self):
        self.tickets.pop()
        self.parkingSpaces.pop()

    def payForParking(self):
        if self.currentTicket['paid'] == False:
            payment = input("Enter an ammount to pay for your parking: ")

            if payment != None:
                print("Your ticket has been paid! You have 15 minutes to leave the garage.")
                self.currentTicket['paid'] = True
            else:
                print("Insufficient funds. Try Again.")
        else:
            print("Your ticket has already been paid for!")
    
    def leaveGarage(self):
        if self.currentTicket['paid'] == True:
            print("Thank you, have a nice day")
            self.tickets.append(0)
            self.parkingSpaces.append(0)
        else:
            payment2 = input("You have yet to pay for your ticket. Enter an ammount to pay for your parking: ")
            if payment2 != None:
                print("Thank you, have a nice day")
                self.tickets.append(0)
                self.parkingSpaces.append(0)
            else:
                print("Insufficient funds. Try Again.")

ticks = [0] * 10
spaces = [0] * 10
paid = {'paid':False}
left = False
thisParkingSpot = ParkingGarage(ticks, spaces, paid)

take = input("Welcome to our parking garage! Would you like to take a ticket? (Y/N) ")
lowerTake = take.lower()
if lowerTake == 'y':
    thisParkingSpot.takeTicket()
    while left == False:
        userInput = input("Enter 1 when you would like to pay for your parking. Enter 2 when you would like to leave the garage. ")

        if userInput == '1':
            thisParkingSpot.payForParking()
        else:
            thisParkingSpot.leaveGarage()
            left = True
else:
    print("Thank you, have a nice day.")