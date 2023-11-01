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

def play_round(a_deck, a_hand):
    '''
    This function plays a round of game, given a deck and a hand of cards.
    '''

    if len(a_hand) < 4:
        for i in range(len(a_hand), 4):
            cards.draw(a_deck, a_hand)

    while len(a_hand) > 4:
        first = a_hand[-4][0]
        fourth = a_hand[-1][0]
        if first == fourth:
            discard(a_hand, 4)
    
    print(a_hand)

    if len(a_deck) > 0:
        last_hand = a_deck.pop()
        print(last_hand)

    return a_deck, a_hand
    