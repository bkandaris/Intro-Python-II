# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, starting_room):
        self.current_room = starting_room
        self.items = []

    def go_to(self, direction):
        if getattr(self.current_room, f"{direction}_to") is not None:
            self.current_room = getattr(self.current_room, f"{direction}_to")
        else:
            print("Can't go this way!.")

    def show_items(self):
        print(f'Inventory: {", and ".join([item.name + ": " + item.description for item in self.items])}')

    def on_take(self, the_item):
        for item in self.current_room.items:
            if item.name == the_item:
                self.items.append(item)
                self.current_room.items.remove(item)
                print(f'You took {item.name}')
            else:
                print("Item isn't here!.")

    def on_drop(self, the_item):
        for item in self.items:
            if item.name == the_item:
                self.items.remove(item)
                self.current_room.items.append(item)
                print(f'You have dropped the {item.name}')
            else:
                print("Item not available.")