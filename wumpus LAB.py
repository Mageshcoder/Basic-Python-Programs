from random import choice
cave_number=range(1,20)
wumpus=choice(cave_number)
player=choice(cave_number)
while player==wumpus:
   player=choice(cave_number)
print("welcome to wumpus")
print("you can see", len(cave_number),"caves in here")
print("to play, enter the cave number to continue...")

#print(wumpus,"",player,cave_number)

while True:
   print("You are in cave" ,player)
   if(player==wumpus-1 or player==wumpus+1):
      print("i smell wumpus here")
   print("which cave is next")
   player_input=input()
   if ((not player_input.isdigit() or player_input) not in cave_number):
      print(player_input, " is not a cave")
   else:
      player=int(player_input)
      if player==wumpus:
         print("you got beaten by wumpus")
         break
