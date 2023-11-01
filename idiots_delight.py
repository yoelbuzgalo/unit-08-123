import cards

def deal_hands():
    '''
    This function creates a deck and deals (draws 4 cards out of the deck)
    '''
    deck = cards.make_deck() # Create a deck
    hand = cards.deal_one_hand(deck, 4) # Draw 4 cards accordingly from the deck
    return deck, hand