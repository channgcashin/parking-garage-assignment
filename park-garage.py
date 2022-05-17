class ParkingGarage():
    def __init__(self):
        self.tickets = [0] * 10
        self.parkingSpaces = list(range(1,11))
        self.currentTicket = {'paid' : False}

    def takeTicket(self):
        if self.tickets:
            self.tickets.pop()
            print()
            print("You have parking space", self.parkingSpaces[-1])
            self.parkingSpaces.pop()
            print()
        else:
            print("There are no parking spaces available! Sorry for the inconvinience")
        
    def payForParking(self):
        if self.currentTicket['paid'] == False:
            payment = input("Enter an ammount to pay for your parking: ")

            if payment:
                print("Your ticket has been paid! You have 15 minutes to leave the garage.")
                self.currentTicket['paid'] = True
            else:
                print("Insufficient funds. Try Again.")
        else:
            print("Your ticket has already been paid for!")
    
    def leaveGarage(self):
        if self.currentTicket['paid'] == True:
            print("Thank you, have a nice day")
            self.parkingSpaces.append(self.parkingSpaces[-1] + 1)
            self.tickets.append(0)
            self.currentTicket['paid'] = False
        else:
            print("You have yet to pay!")

garage = ParkingGarage()

while True:
    print()
    print("Select from the following:")
    print("1) Take a parking ticket")
    print("2) Pay for your parking")
    print("3) Leave the parking garage")
    print("4) Quit\n")
    userInput = input("What would you like to do: ")

    if userInput == '1':
        garage.takeTicket()
    elif userInput == '2':
        garage.payForParking()
    elif userInput == '3':
        garage.leaveGarage()
    elif userInput == '4':
        break
    else: 
        print("Invalid input. Try again.")
