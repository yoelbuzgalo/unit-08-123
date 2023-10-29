import cards

def test_cards_JD():
    # Setup
    rank = 11
    suit = 'Diamonds'
    expected = (11, "Diamonds", "Jack of Diamonds", (cards.RED_VALUE+"JD"+cards.WHITE_VALUE))

    # Invoke
    result = cards.make_card(rank, suit)

    # Analysis
    assert result == expected

def test_cards_10C():
    # Setup
    rank = 10
    suit = 'Clubs'
    expected = (10, "Clubs", "10 of Clubs", (cards.BLUE_VALUE+"10C"+cards.WHITE_VALUE))

    # Invoke
    result = cards.make_card(rank, suit)

    # Analysis
    assert result == expected

def test_cards_8H():
    # Setup
    rank = 8
    suit = 'Hearts'
    expected = (8, "Hearts", "8 of Hearts", (cards.RED_VALUE+"8H"+cards.WHITE_VALUE))

    # Invoke
    result = cards.make_card(rank, suit)

    # Analysis
    assert result == expected


def test_cards_KS():
    # Setup
    rank = 13
    suit = 'Spades'
    expected = (13, "Spades", "King of Spades", (cards.BLUE_VALUE+"KS"+cards.WHITE_VALUE))

    # Invoke
    result = cards.make_card(rank, suit)

    # Analysis
    assert result == expected

def test_cards_invalid_suit():
    # setup
    rank = 10
    suit = 'Hehehe'
    expected = None

    # Invoke
    result = cards.make_card(rank, suit)

    # Analysis
    assert result == expected

def test_cards_invalid_rank():
    # setup
    rank = 11111
    suit = 'Clubs'
    expected = None

    # Invoke
    result = cards.make_card(rank, suit)

    # Analysis
    assert result == expected

def test_card_deck_len():
    # Setup
    expected = 52

    # Invoke
    result = len(cards.make_deck())

    # Analysis
    assert result == expected

def test_card_deck_clubs():
    # Setup
    expected = (2, "Clubs", "2 of Clubs", (cards.BLUE_VALUE+"2C"+cards.WHITE_VALUE))

    # Invoke
    result = cards.make_deck()

    # Analysis
    assert result[0] == expected

def test_card_deck_diamonds():
    # Setup
    expected =(2, "Diamonds", "2 of Diamonds", (cards.RED_VALUE+"2D"+cards.WHITE_VALUE))

    # Invoke
    result = cards.make_deck()

    # Analysis
    assert result[1] == expected

def test_card_deck_hearts():
    # Setup
    expected =(2, "Hearts", "2 of Hearts", (cards.RED_VALUE+"2H"+cards.WHITE_VALUE))

    # Invoke
    result = cards.make_deck()

    # Analysis
    assert result[2] == expected

def test_card_deck_spades():
    # Setup
    expected =(2, "Spades", "2 of Spades", (cards.BLUE_VALUE+"2S"+cards.WHITE_VALUE))

    # Invoke
    result = cards.make_deck()

    # Analysis
    assert result[3] == expected