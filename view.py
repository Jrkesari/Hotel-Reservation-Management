from tabulate import tabulate

def viewMenu(mainList):
    if (len(mainList) == 0):
        print("No bookings found.")
    else:
        print(tabulate(
            mainList,
            ["ID", "Room Type", "Food Selection", "Total ($)"],
            tablefmt="fancy_grid")
        )

    try:
        input('\n--> Press ENTER to go back: ')
        pass
    except KeyboardInterrupt:
        print("\n\n\tExiting...")
        pass
    except:
        viewMenu(mainList)