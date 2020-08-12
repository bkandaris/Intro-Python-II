# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name, currentRoom):
        self.name = name
        self.currentRoom = currentRoom
        self.items = []

    def __str__(self):
        return f"Name: {self.name} currentRoom: {self.currentRoom}"

    def move(self, direction):
        nextRoom = getattr(self.currentRoom, f"{direction}_to")
        if nextRoom is not None:
            self.currentRoom = nextRoom 
        else:
            print("Can't go that way!")
