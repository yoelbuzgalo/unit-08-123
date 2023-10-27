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
        if suit == 'Diamonds' or suit == 'Clubs' or suit == 'Hearts' or suit == 'Spades':
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


    return (rank, suit, name, shorthand) # Return a tuple containing these values