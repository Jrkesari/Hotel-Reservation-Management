from tabulate import tabulate

def cancelMenu(mainList):
    if (len(mainList)==0):
        print("No bookings found.")
    else:
        print(tabulate(
            mainList,
            ["ID", "Room Type", "Prices/day ($)"], 
            tablefmt="fancy_grid")
        )
    
    try:
        action = int(input('\n--> Choose a booking ID to cancel: '))
        mainList.remove(mainList[action-1])
    except KeyboardInterrupt:
        print("\n\n\tExiting...")
        pass
    except:
        cancelMenu(mainList)