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
