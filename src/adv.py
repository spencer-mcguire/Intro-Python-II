from room import Room
from player import Player
import os

# Clear screen and get ready to input name
os.system('cls')
# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
user = input('Hello, What is your name? ')
player = Player(user, room['outside'])
# clear screen after name input
os.system('cls')

print("==================================")
print(f"Welcome brave {player.name}")
print(f"Your current room is: {player.current_room.name}\n")
print(f"{player.current_room.description}")
print("==================================\n")
# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
active = True

while active == True:
    # Destructure values
    current_room = player.current_room

    # Commands
    command = input(
        'Please provide a direction of travel [n][s][e][w]: ').lower().split(" ")

    if len(command) < 2:
        command = command[0]
        # if no spaces found in input it means it is a direction of travel
        if command == 'n':
            if player.current_room.n_to:
                player.current_room = player.current_room.n_to
                print(f'\n{player.current_room.description}\n')

            else:
                print('\n There is no room to the North! \n')

        elif command == 's':
            if player.current_room.s_to:
                player.current_room = player.current_room.s_to
                print(f'\n{player.current_room.description}\n')

            else:
                print('\n There is no room to the South! \n')

        elif command == 'e':
            if player.current_room.e_to:
                player.current_room = player.current_room.e_to
                print(f'\n{player.current_room.description}\n')

            else:
                print('\n There is no room to the East! \n')

        elif command == 'w':
            if player.current_room.w_to:
                player.current_room = player.current_room.w_to
                print(f'\n{player.current_room.description}\n')

            else:
                print('\n There is no room to the West! \n')

        elif command == 'q':
            active = False

        else:
            print(f"""
                {command} is not valid!
                Use 'n', 's', 'e', 'w' to move to a differnt room. 
                Or use 'q' to quit the game.
                """)

    # else:
        # logic for picking up items in the room

print('\n\n*** Goodbye ***')
