from maze import Maze
from room import Room
my_rooms = []
my_rooms.append(Room("This room is the entrance."))
my_rooms.append(Room("This room has a table. Maybe a dinning room?"))
my_rooms.append(Room("This is drexel."))
my_rooms.append(Room("This upenn."))
my_rooms.append(Room("your house."))
my_rooms.append(Room("downstreet."))
my_rooms.append(Room("brickwall."))
my_rooms.append(Room("another brick wall."))
my_rooms.append(Room("another brick wall you are unlucky."))
my_rooms.append(Room("This room is the exit. Good Job."))

#room 0 is south of room 1
my_rooms[0].setNorth(my_rooms[1])
my_rooms[1].setSouth(my_rooms[0])
my_rooms[2].setNorth(my_rooms[4])
my_rooms[3].setSouth(my_rooms[2])
my_rooms[4].setNorth(my_rooms[5])
my_rooms[5].setSouth(my_rooms[7])
my_rooms[6].setNorth(my_rooms[8])
my_rooms[7].setSouth(my_rooms[9])
my_rooms[8].setNorth(my_rooms[9])
my_rooms[9].setSouth(my_rooms[9])

#Room 2 is east of room 1
my_rooms[1].setEast(my_rooms[2])
my_rooms[2].setWest(my_rooms[1])
my_rooms[3].setEast(my_rooms[2])
my_rooms[4].setWest(my_rooms[5])
my_rooms[6].setEast(my_rooms[8])
my_rooms[7].setWest(my_rooms[6])
my_rooms[8].setWest(my_rooms[9])
my_rooms[4].setEast(my_rooms[9])
my_rooms[5].setEast(my_rooms[7])
my_maze = Maze(my_rooms[0],my_rooms[9])

while True:
    print(my_maze.getCurrent())
    userInput = input("Enter direction to move north west east south restart\n")
    userInput = userInput.lower()
    if userInput == "north":
        if my_maze.moveNorth() == False:
            print("Direction invalid, try again.")
            continue 
    elif userInput == "south":
        if my_maze.moveSouth() == False:
            print("Direction invalid, try again.")
            continue
    elif userInput == "west":
        if my_maze.moveWest() == False:
            print("Direction invalid, try again.")
            continue
    elif userInput == "east":
        if my_maze.moveEast() == False:
            print("Direction invalid, try again.")
            continue
    elif userInput == "reset":
        my_maze.reset()
        continue
    elif my_maze.getCurrent() == my_maze.atExit():
        print("You have reached the end of the maze")
        
    
    