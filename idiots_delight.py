import cards

def deal_hands():
    '''
    This function creates a deck and deals (draws 4 cards out of the deck)
    '''
    deck = cards.make_deck() # Create a deck
    hand = cards.deal_one_hand(deck, 4) # Draw 4 cards accordingly from the deck
    return deck, hand

def discard(a_hand, num_cards):
    '''
    This function checks and discards cards given the num_card parameter
    '''
    
    if (num_cards != 4 and num_cards != 2) or (len(a_hand) < 4):
        return a_hand
    
    if num_cards == 4:
        for _ in range(4):
            a_hand.pop()
    elif num_cards == 2:
        a_hand.pop(-2)
        a_hand.pop(-2)
    
    return a_hand