avaiable_exits = ["east", "north east", "south"]

choosen_exit = ""

while choosen_exit not in avaiable_exits:
    choosen_exit = input("Please enter the direction : ")
    if choosen_exit == "quit":
        print("Your GAME OVER")
        break

else:
    print("Are you not glad that you are out of this loop")