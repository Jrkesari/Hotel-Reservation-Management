import os
import mysql.connector as sqc
from pyfiglet import Figlet
from tabulate import tabulate

from login import login
from register import register
from database import database
from booking import bookingMenu
from view import viewMenu
from cancel import cancelMenu
from food import foodMenu
from billing import billingMenu

# Connnect to DB
dbHost = "localhost"
dbUser = "root"
sql = sqc.connect(host=dbHost, user=dbUser)

# DB Init
cursor = sql.cursor()
database(cursor)

isLogged = False
mainList = []
f = Figlet(font='slant')

while True:
    if isLogged == False:
        os.system('cls')
        print(f.renderText('bytecode'))
        print("1. Login")
        print("2. Register")

        try:
            action = int(input('\n--> Select a valid ID: '))
            if action == 1:
                os.system('cls')
                print(f.renderText('Login'))
                isLogged = login(cursor)
            elif action == 2:
                os.system('cls')
                print(f.renderText('Register'))
                register(cursor, sql)
        except KeyboardInterrupt:
            print("\n\n\tExiting...")
            break

    if isLogged:
        os.system('cls')
        print(f.renderText('bytecode'))
        print("1. Book a room")
        print("2. View bookings")
        print("3. Cancel a booking")

        try:
            action = int(input('\n--> Select a valid ID: '))

            if (action == 1):
                cRoomList = []
                cFoodList = []

                os.system('cls')
                print(f.renderText('Room booking'))
                time = int(input('--> Days to stay: '))

                foodMenu(cFoodList, time)
                bookingMenu(cRoomList, time)
                billingMenu(cFoodList, cRoomList)

                confirmBooking = input("\nConfirm booking (y/n): ")

                if confirmBooking == "y":
                    l1 = cRoomList[0].copy()
                    l2 = cFoodList[0].copy()
                    newList = []

                    newList.append(str(l1[0]))
                    newList.append(str(l1[1]))
                    newList.append(str(l2[1]))
                    newList.append(str(int(l1[2])+int(l2[2])))
                    mainList.append(newList)

                    print("\n"+tabulate(mainList, ["ID", "Room Type",
                                              "Food Selection", "Total ($)"],
                                   tablefmt="fancy_grid"))
                    input('\n--> Press ENTER to continue: ')

            elif (action == 2):
                os.system('cls')
                print(f.renderText('Your booking(s)'))
                viewMenu(mainList)
            elif (action == 3):
                os.system('cls')
                print(f.renderText('Cancel a booking'))
                cancelMenu(mainList)
            else:
                print("Please select a valid option")
        except KeyboardInterrupt:
            print("\n\n\tExiting...")
            break