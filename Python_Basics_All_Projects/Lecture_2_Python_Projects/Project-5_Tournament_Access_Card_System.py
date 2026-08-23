print("\n----- Tournament Access System -----")

Name = input("\nPlease enter your name: ")
gameID = input(Name + ", do you have a Game ID? (y/n): ")
Pass = input(Name + ", do you have a Tournament Pass? (y/n): ")
Card = input(Name + ", do you have a Tournament Player Card? (y/n): ")

if gameID == "y" and Pass == "y" and Card == "y":
    Status = "Tournament Player"
    Access = "You can enter the stadium and play in the tournament."

elif gameID == "y" and Pass == "y" and Card == "n":
    Status = "Special Viewer"
    Access = "You can enter the stadium and watch the tournament."

elif gameID == "n" and Pass == "y" and Card == "n":
    Status = "Viewer"
    Access = "You can enter the stadium and watch the tournament."

elif gameID == "y" and Pass == "n" and Card == "n":
    Status = "Free Streamer"
    Access = "You can stream the tournament for free on Game.stream using your Game ID."

else:
    Status = "No Access"
    Access = "Sorry, you do not have access to the tournament."

print("\nStatus:",Status)
print("Access:",Access)