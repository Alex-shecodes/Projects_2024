from time import sleep
import sys

# Introduction
def show_intro():
    '''Displays the game's introduction with a typewriter effect'''
    intro_text = 'You wake up on cold, damp ground, the earthy scent of moss and wet leaves thick around you.Rising slowly, you find yourself surrounded by towering trees, their dense canopy blocking out most of the light and casting deep shadows across the forest floor.\nThe forest extends endlessly in every direction, with no clear path or landmark to guide you.Panic settles in as you search your memory for any clue of how you got here—nothing. Your pockets are empty, and an eerie silence fills the air, broken only by the faint, haunting sound of a melody drifting from somewhere deeper among the trees. The atmosphere feels alive, as though the forest itself is watching, waiting for you to make your move.'

    # Typewriter effect for the introduction
    for char in intro_text:
        print(char, end='')
        sys.stdout.flush()
        sleep(0.007)  # Adjust typing speed here

# Show the current location
def show_current_location(location, locations):
    print(f'\nYou are in {locations[location]["name"]}.')
    print(locations[location]['description'])
    if 'items' in locations[location] and locations[location]['items']:
       print('You see the following items:')
       for item in locations[location]['items']:
           print(f'-{item}')
        
    print('What do you want to do next: go north, go south, go east, go west, take, inventory or quit? ')
# Get the users input
def get_player_input():
    '''Gets and validates player input'''
    action = input('> ').lower()
    if action in ('go north', 'go south', 'go west', 'go east', 'take', 'inventory', 'quit'):
        return action 
    else:
        print('Invalid action. Try again!')

# Moves the player to a new location if possible
def move_player(location, direction, locations):
    '''Moves the player to a new location if possible'''
    new_location = locations[location]['directions'].get(direction)
    if new_location:
        return new_location
    else:
        print('You cannot go that way.')
        return location


# Adds an item to the player's inventory
def take_item(location, item, locations, inventory):
    ''' Adds an item to the player's inventory if it exists at the location '''
    if 'items' in locations[location] and item in locations[location]['items']:
        inventory.append(item)
        locations[location]['items'].remove(item)
        print(f"You have taken the {item}.")
    else:
        print("That item isn't here.")

# Shows the player's inventory
def show_inventory(inventory):
        if inventory:
            print("Your inventory:")
            for item in inventory:
                print(f"- {item}")
        else:
            print("Your inventory is empty.")


# --- The Main Game Loop ---
def play_game():
    '''Main game loop'''
locations = {
    'endless grove':{
        'name': 'The Endless Grove',
        'description': 'The forest here stretches on with towering trees, their twisted branches interlocking above, blocking most of the light. It feels as though no matter how far you walk, the grove only deepens, with no way out in sight.',
        'directions': {'north': 'old oak', 'east': 'stone circle'},
        'items': ['Backpack']
        },
    'old oak':{
        'name': 'The Old Oak',
        'description': 'A massive oak tree dominates this part of the forest, its gnarled roots forming strange shapes in the ground. Carvings cover its thick bark, telling stories of past wanderers who have left their marks here.',
        'directions': {'south': 'endless grove', 'east': 'misty pond'},
        },
        'stone circle':{
        'name': 'The Stone Circle',
        'description': 'A ring of ancient stones, weathered by time, sits quietly in the forest. Moss covers each stone, and faint markings suggest they once held some ceremonial importance. The air is heavy, as though holding secrets too old to remember.',
        'directions': {'west': 'endless grove', 'north': 'misty pond'},
        'items': ['candlestick']
        },
        'misty pond':{
        'name': 'The Misty Pond',
        'description': 'A small pond appears through the trees, its surface obscured by a layer of mist. Reflections in the water seem distorted, showing glimpses of places not visible around you. A chill runs through the air here.',
        'directions': {'west': 'old oak', 'south': 'stone circle', 'east': 'fallen log'},
        },
        'fallen log':{
        'name': 'The Fallen Log',
        'description': 'A giant log lies across the forest floor, as though felled by some ancient force. Mushrooms grow along its bark, and the faint smell of decay hangs in the air. There\'s something almost inviting about its hollow interior.',
        'directions': {'west': 'misty pond', 'north': 'forest edge'},
        },
        'forest edge':{
        'name': 'The Forest Edge',
        'description': 'At last, the trees begin to thin, revealing the edge of the forest. The sky opens up, and a warm light shines from beyond the trees, promising an end to the endless woods.',
        'directions': {},  # final location
        }
    }

current_location = 'endless grove'
inventory = []

# display the introduction with a typewriter effect
show_intro()

while True:
    show_current_location(current_location, locations)
    action = get_player_input()
    if action == 'quit':
        print('Thanks for playing!')
        break
    elif action.startswith('go'):
         direction = action.split()[-1]
         current_location = move_player(current_location, direction, locations)
    elif action == 'take':
         item = input('What do you want to take\n').lower()
         take_item(current_location, item, locations, inventory)
    elif action == 'inventory':
         show_inventory(inventory)
if __name__ == '__main__':
     play_game()

