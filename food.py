from tabulate import tabulate

def foodMenu(cFoodList, time):
    try:
        f=["ID", "Food", "Total ($)"]
        f1=[1, "1 Time Meal", 10*time]
        f2=[2, "2 Time Meal", 20*time]
        f3=[3, "3 Time Meal", 30*time]
    
        print("\nSelect food package: ")
        print(tabulate(
            [f1, f2, f3], 
            f, tablefmt="fancy_grid"))

        action = int(input('\n--> Select a valid ID: '))

        if (action==1):
            cFoodList.append(f1)
        elif (action==2):
            cFoodList.append(f2)
        elif (action==3):
            cFoodList.append(f3)
        else:
            foodMenu(cFoodList, time)    
    except KeyboardInterrupt:
        print("\n\n\tExiting...")
        pass
    except:
        foodMenu(cFoodList, time)