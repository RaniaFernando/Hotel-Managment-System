class Resort:
    def __init__(self, norooms, price, location, availableroom):
        self.norooms = norooms
        self.price = price
        self.location = location
        self.availableroom = availableroom

    def ifo(self):
        print("Welcome to the the Resort")

    def info(self):
        print( f"The total no of Rooms are {self.norooms} the price of a rooms is {self.price}/- the location is  {self.location} and available rooms are {self.availableroom}")


p1 = Resort(32, 2000, "Mumbai", 10)
p1.ifo()
p1.info()

x = int(input("How many rooms would you like to book  "))

y = input("Do you want to confirm your Bookings y/n ")

while y == y:
    if x == 1:
        print("Your price is 2000Rs")
        break
    if x == 2:
        print("Your price is 4000Rs")
        break
    if x == 3:
        print("Your price is 6000Rs")
        break
else:
    print("Sorry to see u leave")


class Cafeteria():
    def __init__(self, indian, itailain):
        self.indian = indian
        self.itailain = itailain

    def basic(self):
        print(f"We serve {self.indian} and {self.itailain} for breakfast")


z = input("Do you want to reserve seat for the complimantry breakfast y/n ")

if z == y:
    p2 = Cafeteria("Indian", "Italian")
    p2.basic()
    num = int(input("How many seats would you like to reserve  "))
    print("{} seats have been reserved ".format(num))
else:
    print("Thanks for your confirmation")

print("We have other services like \n 1.Spa \n 2.Swimming \n 3.Kids club \n 4.Bar \n 5.Fitness Room ")

ser = input("Would you like to opt the Services y/n ")

service = int(input("Pls confirm you want additional services  "))

while (service == y and ser == range(1, 5)):
    anum = input("Kindly enter the service number ")
    if anum == 1:
        print("Your reservarton for Spa is done ")
    elif anum == 2:
        print("Your reservarton for Swimming is done ")
    elif anum == 3:
        print("Your reservarton for Kids Club is done ")
    elif anum == 4:
        print("Your reservarton for Bar is done ")
    else:
        print("You have opted for no additional services")














