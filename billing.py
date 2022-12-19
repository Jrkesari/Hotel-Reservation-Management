from tabulate import tabulate

def billingMenu(cFoodList, cRoomList):
    try:
        if (len(cFoodList+cRoomList)==0):
            print("No bookings found.")
        else:
            l=[]
            l.append(cFoodList[0])
            l.append(cRoomList[0])

            print("\nBill: ")
            print(tabulate(
                l,
                ["ID", "Item", "Price ($)"], 
                tablefmt="fancy_grid")
            )
            print("\t\t\tTotal:",cFoodList[0][2]+cRoomList[0][2])
    except KeyboardInterrupt:
        print("\n\n\tExiting...")
        pass
    except:
        billingMenu(cFoodList, cRoomList)