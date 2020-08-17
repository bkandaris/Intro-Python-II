from room import Room
from player import Player
from item import Item

# Declare all the items and rooms

item = {
    "sword" : Item("sword", "sharp pointy thing"),
    "shield" : Item("shield", "a defensive item"),
    "coins" : Item("coin", "shiny gold coin"),
}

room = {
    'outside': Room("Outside Cave Entrance", "North of you, the cave mount beckons."),

    'foyer': Room("Foyer", """Dim light filters in from the south. Dusty
    passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
    into the darkness. Ahead to the north, a light flickers in
    the distance, but there is no way across the chasm."""),

    'narrow': Room("Narrow Passage", """The narrow passage bends here from west
    to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
    chamber! Sadly, it has already been completely emptied by
    earlier adventurers. The only exit is to the south."""),
}

# Adding items to each room
room["outside"].items.append(item['sword'])
room["treasure"].items.append(item['coins'])
room["foyer"].items.append(item['shield'])
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
player = Player(room['outside'])

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.

while True:
    decision = input(f"""
    {player.current_room}

"n" = North, "e"=East, "s"=South, "w"=West  "i"=Inventory, or "q" exits                       
    
Next command? """)
    command = decision.lower().split()

# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
    if len(command) == 1:
        if decision == "n" or decision == "e" or decision == "s" or decision == "w":
            player.go_to(decision)
        elif decision == "i":
            player.show_items()
        elif decision == "q":
            print('You quit the game.')
            break
        else:
            print("command unknown.")
    elif len(command) == 2:
        if command[0] == "take":
            player.on_take(command[1])
        elif command[0] == "drop":
            player.on_drop(command[1])
        else:
            print("Command unknown.")
    else:
        print("Not a valid choice.")