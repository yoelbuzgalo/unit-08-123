import random
from sorts import swap

SUITS = ("Clubs", "Diamonds", "Hearts", "Spades") # Global constant for suit names to be used in different functions (better to use same variable value to prevent spelling errors)
RED_VALUE, BLUE_VALUE, WHITE_VALUE = "\033[31m", "\033[34m" , "\033[37m" # Global constants for the pytest to be able to import and use in syntax check

def make_card(rank, suit):
    '''
    This function makes and returns a card
    '''

    # Initialize variables to empty string values
    shorthand = ""
    name = ""

    # This function hardcodes name and shorthand based on values passed to this function
    try:
        if rank > 14 or rank < 1:
            raise ValueError()
        if suit == SUITS[0] or suit == SUITS[1] or suit == SUITS[2] or suit == SUITS[3]:
            if rank == 11:
                name = "Jack of " + suit
                shorthand = 'J' + suit[0]
            elif rank == 12:
                name = "Queen of " + suit
                shorthand = 'Q' + suit[0]
            elif rank == 13:
                name = "King of " + suit
                shorthand = 'K' + suit[0]
            elif rank == 14:
                name = "Ace of " + suit
                shorthand = 'A' + suit[0]
            else:
                name = str(rank) + " of " + suit
                shorthand = str(rank) + suit[0]
        else:
            raise ValueError()
    except:
        print("There was an error with passed suit or rank to this function")
        return None

    # Color insertion by shorthand value, depending on the Suit..
    # Checks the last index of any shorthand of its current suit and inserts accordingly its color
    if shorthand[-1] == 'D':
        shorthand = RED_VALUE + shorthand + WHITE_VALUE
    elif shorthand[-1] == 'C':
        shorthand = BLUE_VALUE + shorthand + WHITE_VALUE
    elif shorthand[-1] == 'H':
        shorthand = RED_VALUE + shorthand + WHITE_VALUE
    elif shorthand[-1] == 'S':
        shorthand = BLUE_VALUE + shorthand + WHITE_VALUE

    return (rank, suit, name, shorthand) # Return a tuple containing these values

def make_deck():
    '''
    This function makes a standard 52 deck with make_card function, it returns a deck of 52 cards containing different ranks and suits
    '''
    ranks = range(2, 15)
    return [make_card(x, y) for x in ranks for y in SUITS]

def shuffle(a_deck):
    '''
    This function shuffles any given deck, changing cards' order and returns a new shuffled deck
    '''
    for index in range(0,len(a_deck)):
        selected_index = random.randrange(0, len(a_deck))
        copy_value = a_deck[index]
        a_deck[index] = a_deck[selected_index]
        a_deck[selected_index] = copy_value

    return a_deck


def main():
    # print(make_card(8, 'Diamonds')[3], make_card(13, 'Clubs')[3])
    # print(shuffle(make_deck()))
    pass
    

if __name__ == "__main__":
    main()