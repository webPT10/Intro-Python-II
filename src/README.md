#Day 2 MVP

Room
# >> Make rooms able to hold multiple items

Player
# >> Make the player able to carry multiple items

ADV / ? 
# >> Add get [ITEM_NAME] and drop [ITEM_NAME] commands to the parser

?
# >> Add items to the game that the user can carry around

-----

item.py
# ** Create file, item.py > done
# ** Item class w/ name & description attributes > done
 --

Add the ability to ADD items to Rooms.
# ** completed > self.roomItems = []


# Add way to see items available in that room 


# Add capability to add (pick up) Items to the player's inventory. 
# ** completed > self.inventory = []



# Add a new type of sentence the parser can understand: two words.

But now we want to add the in the command line:
verb object - such as "take coins" or "drop sword".

Split the entered command and see if it has 1 or 2 words in it to determine if it's the first or second form.


# ** have user able to see the Items in their Room printed to the command line

# Implement support for the verb GET/TAKE followed by an Item name. This will be used to pick up Items.

If the user enters GET or TAKE followed by an Item name, look at the contents of the current Room to see if the item is there.

    If it is there, remove it from the Room contents, and add it to the Player contents.

    If it's not there, print an error message telling the user so.

# ** Add an on_take method to Item.
Called when the Item is picked up by the player.

on_take print out > "You have picked up [NAME]" when you pick up an item.

The Item can use this to run additional code when it is picked up.

# ** Add an on_drop method to Item. 
Implement it similar to on_take

# Implement support for the verb DROP followed by an Item name. 
This is the opposite of GET/TAKE


# Add the i and inventory commands that both show a list of items currently carried by the player.