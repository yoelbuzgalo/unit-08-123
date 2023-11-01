import idiots_delight
import cards

def test_deal_hands():
    # Setup
    expected_deck_len = 52-4
    expected_hand = [(14, 'Spades', 'Ace of Spades', '\x1b[34mAS\x1b[37m'),(14, 'Hearts', 'Ace of Hearts', '\x1b[31mAH\x1b[37m'),(14, 'Diamonds', 'Ace of Diamonds', '\x1b[31mAD\x1b[37m'),(14, 'Clubs', 'Ace of Clubs', '\x1b[34mAC\x1b[37m')]

    # Invoke
    result_deck, result_hand = idiots_delight.deal_hands()

    print(expected_hand)

    # Analysis
    assert len(result_deck) == expected_deck_len
    assert result_hand == expected_hand

def test_discard_4():
    # Setup
    hand = [(14, 'Spades', 'Ace of Spades', '\x1b[34mAS\x1b[37m'),(14, 'Hearts', 'Ace of Hearts', '\x1b[31mAH\x1b[37m'),(14, 'Diamonds', 'Ace of Diamonds', '\x1b[31mAD\x1b[37m'),(14, 'Clubs', 'Ace of Clubs', '\x1b[34mAC\x1b[37m')]
    expected = []

    # Invoke
    result = idiots_delight.discard(hand, 4)

    # Analysis
    assert result == expected

def test_discard_2():
    # Setup
    hand = [(14, 'Spades', 'Ace of Spades', '\x1b[34mAS\x1b[37m'),(14, 'Hearts', 'Ace of Hearts', '\x1b[31mAH\x1b[37m'),(14, 'Diamonds', 'Ace of Diamonds', '\x1b[31mAD\x1b[37m'),(14, 'Clubs', 'Ace of Clubs', '\x1b[34mAC\x1b[37m')]
    expected = [(14, 'Spades', 'Ace of Spades', '\x1b[34mAS\x1b[37m'),(14, 'Clubs', 'Ace of Clubs', '\x1b[34mAC\x1b[37m')]

    # Invoke
    result = idiots_delight.discard(hand, 2)

    # Analysis
    assert result == expected

def test_discard_3():
    # Setup
    hand = [(14, 'Spades', 'Ace of Spades', '\x1b[34mAS\x1b[37m'),(14, 'Hearts', 'Ace of Hearts', '\x1b[31mAH\x1b[37m'),(14, 'Diamonds', 'Ace of Diamonds', '\x1b[31mAD\x1b[37m'),(14, 'Clubs', 'Ace of Clubs', '\x1b[34mAC\x1b[37m')]
    expected = [(14, 'Spades', 'Ace of Spades', '\x1b[34mAS\x1b[37m'),(14, 'Hearts', 'Ace of Hearts', '\x1b[31mAH\x1b[37m'),(14, 'Diamonds', 'Ace of Diamonds', '\x1b[31mAD\x1b[37m'),(14, 'Clubs', 'Ace of Clubs', '\x1b[34mAC\x1b[37m')]

    # Invoke
    result = idiots_delight.discard(hand, 3)

    # Analysis
    assert result == expected

def test_discard_empty():
    # Setup
    hand = []
    expected = []

    # Invoke
    result = idiots_delight.discard(hand, 4)

    # Analysis
    assert result == expected

def test_play_round_empty():
    # Setup
    deck = cards.make_deck()
    hand = []
    expected_deck_len = 52-5 # Minus 5 because it prints one last card if the deck still exists
    expected_hand = [(14, 'Spades', 'Ace of Spades', '\x1b[34mAS\x1b[37m'),(14, 'Hearts', 'Ace of Hearts', '\x1b[31mAH\x1b[37m'),(14, 'Diamonds', 'Ace of Diamonds', '\x1b[31mAD\x1b[37m'),(14, 'Clubs', 'Ace of Clubs', '\x1b[34mAC\x1b[37m')]

    # Invoke
    result_deck, result_hand = idiots_delight.play_round(deck, hand)

    # Analysis
    assert len(result_deck) == expected_deck_len and result_hand == expected_hand

def test_play_round_full():
    # Setup
    deck = cards.make_deck()
    hand = [(14, 'Spades', 'Ace of Spades', '\x1b[34mAS\x1b[37m'),(14, 'Hearts', 'Ace of Hearts', '\x1b[31mAH\x1b[37m'),(14, 'Diamonds', 'Ace of Diamonds', '\x1b[31mAD\x1b[37m'),(14, 'Clubs', 'Ace of Clubs', '\x1b[34mAC\x1b[37m')]
    expected_deck_len = 52-1 # Minus 1 because it prints one last card if the deck still exists
    expected_hand = [(14, 'Spades', 'Ace of Spades', '\x1b[34mAS\x1b[37m'),(14, 'Hearts', 'Ace of Hearts', '\x1b[31mAH\x1b[37m'),(14, 'Diamonds', 'Ace of Diamonds', '\x1b[31mAD\x1b[37m'),(14, 'Clubs', 'Ace of Clubs', '\x1b[34mAC\x1b[37m')]

    # Invoke
    result_deck, result_hand = idiots_delight.play_round(deck, hand)

    # Analysis
    assert len(result_deck) == expected_deck_len and result_hand == expected_hand

def test_play_round_mid():
    # Setup
    deck = cards.make_deck()
    hand = [(14, 'Spades', 'Ace of Spades', '\x1b[34mAS\x1b[37m'),(14, 'Hearts', 'Ace of Hearts', '\x1b[31mAH\x1b[37m')]
    expected_deck_len = 52-3 # Minus 1 because it prints one last card if the deck still exists
    expected_hand = [(14, 'Spades', 'Ace of Spades', '\x1b[34mAS\x1b[37m'),(14, 'Hearts', 'Ace of Hearts', '\x1b[31mAH\x1b[37m'),(14, 'Spades', 'Ace of Spades', '\x1b[34mAS\x1b[37m'),(14, 'Hearts', 'Ace of Hearts', '\x1b[31mAH\x1b[37m')]

    # Invoke
    result_deck, result_hand = idiots_delight.play_round(deck, hand)

    # Analysis
    assert len(result_deck) == expected_deck_len
    assert result_hand == expected_hand