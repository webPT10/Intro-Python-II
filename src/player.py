# Write a class to hold player information, e.g. what room they are in
# currently.

#Day 2 MVP
# >> Make the player able to carry multiple inventory

class Player:
    def __init__(self, name, currentRoom):
        self.name = name
        self.currentRoom = currentRoom
        self.inventory = []

    def __str__(self):
        return f'Name: {self.name} > Current Room: {self.currentRoom}'

    def move(self, direction):
        nextRoom = getattr(self.currentRoom, f'{direction}_to')

        if nextRoom is not None:
            self.currentRoom = nextRoom
        else:
            print('Unable to move in that direction.')