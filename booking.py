from tabulate import tabulate

def bookingMenu(cRoomList, time):
    try:
        room=["ID", "Room Type", "Total ($)"]
        room1=[1, "Single Room", 50*time]
        room2=[2, "Double Room", 150*time]
        room3=[3, "Deluxe Room", 300*time]

        print("\nBook a room: ")
        print(tabulate(
            [room1, room2, room3], 
            room, tablefmt="fancy_grid"))

        action = int(input('\n--> Select a valid ID: '))

        if (action==1):
            cRoomList.append(room1)
        elif (action==2):
            cRoomList.append(room2)
        elif (action==3):
            cRoomList.append(room3)
        else:
            bookingMenu(cRoomList, time)
    except KeyboardInterrupt:
        print("\n\n\tExiting...")
        pass
    except:
        bookingMenu(cRoomList, time)