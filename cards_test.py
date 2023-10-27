import cards

def test_cards_JD():
    # Setup
    rank = 11
    suit = 'Diamonds'
    expected = (11, "Diamonds", "Jack of Diamonds", "JD")

    # Invoke
    result = cards.make_card(rank, suit)

    # Analysis
    assert result == expected

def test_cards_10C():
    # Setup
    rank = 10
    suit = 'Clubs'
    expected = (10, "Clubs", "10 of Clubs", "10C")

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