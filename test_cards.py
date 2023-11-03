import unittest
from cards import *


class TestCard(unittest.TestCase):
    def test_card_creation(self):
        # Test the creation of a valid card with rank 1 and suit 1.
        valid_card = Card(1, 1)
        self.assertEqual(valid_card.rank, 1)
        self.assertEqual(valid_card.suit, 1)
        self.assertFalse(valid_card.color)
        self.assertFalse(valid_card.face_card)

        # Test creating a card with invalid rank and valid suit.
        with self.assertRaises(ValueError):
            Card(-1, 1)

        # Test creating a card with valid rank and invalid suit.
        with self.assertRaises(ValueError):
            Card(1, -1)

        # Test creating a card with rank greater than 13.
        with self.assertRaises(ValueError):
            Card(14, 1)

        # Test creating a card with valid rank and suit, but an invalid rank for a face card.
        with self.assertRaises(ValueError):
            Card(1, 14)

        # Test creating a valid face card (King of Hearts).
        valid_card = Card("King", "Hearts")
        self.assertEqual(valid_card.rank, 13)
        self.assertEqual(valid_card.suit, 4)
        self.assertTrue(valid_card.color)
        self.assertTrue(valid_card.face_card)

        # Test creating a card with an invalid rank for a face card (Knight is not a valid rank).
        with self.assertRaises(ValueError):
            Card("Knight", "Clubs")

        # Test creating a card with a valid rank but an invalid suit for a face card.
        with self.assertRaises(ValueError):
            Card("Ace", "Club")

        # Test creating a card with an invalid type (True) for rank.
        with self.assertRaises(TypeError):
            Card(1, True)

        # Test creating a card with a floating-point rank, which should raise a TypeError.
        with self.assertRaises(TypeError):
            Card(1.0, 1)

    def test_unicode(self):
        # Test getting the Unicode representation of a card with rank 1 and suit 1 (Ace of Clubs).
        card = Card(1, 1)
        self.assertEqual(card.get_rank_unicode(), 'A')

        # Test getting the Unicode representation of a card with an invalid rank (0).
        card.rank = 0
        with self.assertRaises(ValueError):
            card.get_rank_unicode()

        # Test getting the Unicode representation of a card with an invalid type for rank (True).
        card.rank = True
        with self.assertRaises(TypeError):
            card.get_rank_unicode()

        # Test getting the Unicode representation of a card with rank 1 and suit 1 (Ace of Clubs).
        card.rank = 1
        self.assertEqual(card.get_suit_unicode(), '♣')

        # Test getting the Unicode representation of a card with an invalid suit (0).
        card.suit = 0
        with self.assertRaises(ValueError):
            card.get_suit_unicode()

        # Test getting the Unicode representation of a card with an invalid type for suit (True).
        card.suit = True
        with self.assertRaises(TypeError):
            card.get_suit_unicode()

        # Test getting the Unicode representation of a card with rank 1 and suit 1 (Ace of Clubs).
        card.suit = 1
        self.assertEqual(card.get_card_unicode(), '🃑')

        # Test getting the Unicode representation of a card with an invalid rank (0).
        card.rank = 0
        with self.assertRaises(ValueError):
            card.get_card_unicode()

        # Test getting the Unicode representation of a card with an invalid type for rank (True).
        card.rank = True
        with self.assertRaises(TypeError):
            card.get_card_unicode()

        # Test getting the Unicode representation of a card with rank 1 and an invalid suit (0).
        card.rank = 1
        card.suit = 0
        with self.assertRaises(ValueError):
            card.get_card_unicode()

        # Test getting the Unicode representation of a card with an invalid type for suit (True).
        card.suit = True
        with self.assertRaises(TypeError):
            card.get_card_unicode()

    def test_card_string(self):
        # Test getting the string representation of a card with rank 1 and suit 1 (Ace of Clubs).
        card = Card(1, 1)
        self.assertEqual(str(card), "Ace of Clubs")

        # Test setting the short string format for the card and getting its string representation.
        card.set_short_str_format(True)
        self.assertEqual(str(card), "A♣")

        # Test attempting to set the short string format with an invalid argument ("True").
        with self.assertRaises(TypeError):
            card.set_short_str_format("True")

        # Reset the short string format to the default (False) for subsequent tests.
        card.set_short_str_format(False)

    def test_attribute_comparisons(self):
        # Create four cards with different ranks and suits for comparison.
        card1 = Card(1, 1)  # Ace of Clubs
        card2 = Card(1, 3)  # Ace of Hearts
        card3 = Card(2, 1)  # Two of Clubs
        card4 = Card(2, 4)  # Two of Spades

        # Test if card1 has the same rank as card2 (both are Aces).
        self.assertTrue(card1.same_rank(card2))
        # Test if card1 has the same rank as card3 (different ranks).
        self.assertFalse(card1.same_rank(card3))
        # Test if card1 has the same suit as card3 (both are Clubs).
        self.assertTrue(card1.same_suit(card3))
        # Test if card1 has the same suit as card2 (different suits).
        self.assertFalse(card1.same_suit(card2))
        # Test if card1 has the same color as card3 (both are black).
        self.assertTrue(card1.same_color(card3))
        # Test if card2 has the same color as card4 (both are red).
        self.assertTrue(card2.same_color(card4))
        # Test if card1 has the same color as card2 (different colors).
        self.assertFalse(card1.same_color(card2))

    def test_card_rank_comparisons(self):
        # Create two cards with different ranks but the same suit (Clubs).
        card1 = Card(2, 1)  # Two of Clubs
        card2 = Card(3, 1)  # Three of Clubs

        # Test the < operator
        self.assertTrue(card1 < card2)
        self.assertFalse(card1 < card1)
        self.assertFalse(card2 < card1)

        # Test the <= operator
        self.assertTrue(card1 <= card2)
        self.assertTrue(card1 <= card1)
        self.assertFalse(card2 <= card1)

        # Test the > operator
        self.assertFalse(card1 > card2)
        self.assertFalse(card1 > card1)
        self.assertTrue(card2 > card1)

        # Test the >= operator
        self.assertFalse(card1 >= card2)
        self.assertTrue(card1 >= card1)
        self.assertTrue(card2 >= card1)

    def test_ace_card_comparison(self):
        # Create an Ace of Clubs (rank 1) and another card (rank 8) with the same suit.
        ace = Card(1, 1)
        card = Card(8, 1)

        # Test the < operator
        self.assertTrue(ace > card)  # Ace's rank is worth 14 here, so it is greater
        ace.set_ace_worth_1(True)
        self.assertFalse(ace > card)  # Now Ace's rank is worth 1, so it is smaller
        ace.set_ace_worth_1(False)

        # Test the <= operator
        self.assertTrue(ace >= card)
        ace.set_ace_worth_1(True)
        self.assertFalse(ace >= card)
        ace.set_ace_worth_1(False)

        # Test the > operator
        self.assertFalse(ace < card)
        ace.set_ace_worth_1(True)
        self.assertTrue(ace < card)
        ace.set_ace_worth_1(False)

        # Test the >= operator
        self.assertFalse(ace <= card)
        ace.set_ace_worth_1(True)
        self.assertTrue(ace <= card)
        ace.set_ace_worth_1(False)

    def test_card_equality(self):
        # Create several cards with different ranks, suits, and attributes for comparison.
        card1 = Card(2, 1)  # Two of Clubs
        card2 = Card(3, 1)  # Three of Clubs
        card3 = Card(2, 2)  # Two of Diamonds
        card4 = card1.copy()
        card4.color = True
        card5 = card1.copy()
        card5.face_card = True

        # Test equality (==) between different cards.
        self.assertTrue(card1 == card1)
        self.assertFalse(card1 == card2)
        self.assertFalse(card1 == card3)
        self.assertFalse(card1 == card4)
        self.assertFalse(card1 == card5)

        # Test inequality (!=) between different cards.
        self.assertFalse(card1 != card1)
        self.assertTrue(card1 != card2)
        self.assertTrue(card1 != card3)
        self.assertTrue(card1 != card4)
        self.assertTrue(card1 != card5)


class TestJoker(unittest.TestCase):
    def test_joker_creation(self):
        # Test the creation of a red Joker.
        joker = Joker("Red")
        self.assertEqual(joker.rank, 0)
        self.assertEqual(joker.suit, 0)
        self.assertTrue(joker.color)
        self.assertTrue(joker.face_card)

        # Test creating a Joker with an invalid color ("Green" is not allowed).
        with self.assertRaises(ValueError):
            Joker("Green")

        # Test the creation of a black Joker (color set to False).
        joker = Joker(False)
        self.assertEqual(joker.rank, 0)
        self.assertEqual(joker.suit, 0)
        self.assertFalse(joker.color)
        self.assertTrue(joker.face_card)

        # Test creating a Joker with an invalid argument (None is not allowed).
        with self.assertRaises(TypeError):
            Joker(None)  # This should raise a TypeError.

    def test_unicode(self):
        # Create a black Joker and test its rank Unicode representation.
        joker = Joker(False)
        self.assertEqual(joker.get_rank_unicode(), "J")

        # Set the color to None and test the rank Unicode representation again.
        joker.color = None
        self.assertEqual(joker.get_rank_unicode(), "J")

        # Set the color to True (red) and test the suit Unicode representation.
        joker.color = True
        self.assertEqual(joker.get_suit_unicode(), "R")

        # Set the color to None and attempt to get the suit Unicode representation, which should raise a TypeError.
        joker.color = None
        with self.assertRaises(TypeError):
            joker.get_suit_unicode()

        # Set the color to False (black) and test the full card Unicode representation (Joker).
        joker.color = False
        self.assertEqual(joker.get_card_unicode(), "🃏")

        # Set the color to None and attempt to get the full card Unicode representation, which should raise a TypeError.
        joker.color = None
        with self.assertRaises(TypeError):
            joker.get_card_unicode()

    def test_joker_string(self):
        # Create a black Joker and test its string representation.
        joker = Joker(False)
        self.assertEqual(str(joker), "Black Joker")

        # Set the color to red and enable the short string format, then test the string representation.
        joker.color = True
        joker.set_short_str_format(True)
        self.assertEqual(str(joker), "RJ")

        # Attempt to set the short string format with an invalid argument ("Vrai"), which should raise a TypeError.
        with self.assertRaises(TypeError):
            joker.set_short_str_format("Vrai")

        # Reset the short string format to the default (False) for subsequent tests.
        joker.set_short_str_format(False)


def generate_combinatory_arguments(binary_combination, elements):
    # Calculate the number of argument types needed based on the binary combination.
    argument_types = binary_combination.count("1")
    dividend = 4  # Dividend to determine argument ranges.

    args = []  # Initialize a list to store the arguments.

    # Check each bit of the binary combination to determine which arguments to generate.
    if binary_combination[-1] == '1':  # ...1 : Individual cards
        args = elements[round((dividend - 4) / argument_types):round(dividend / argument_types)]
        dividend += 4
    if binary_combination[-2] == '1':  # ..1. : List of cards
        args += [elements[round((dividend - 4) / argument_types):round(dividend / argument_types)]]
        dividend += 4
    if binary_combination[-3] == '1':  # .1.. : Tuple of cards
        args += [tuple(elements[round((dividend - 4) / argument_types):round(dividend / argument_types)])]
        dividend += 4
    if binary_combination[-4] == '1':  # 1... : Deck of cards
        args += [Deck(elements[round((dividend - 4) / argument_types):round(dividend / argument_types)])]
        dividend += 4

    return args


class TestDeck(unittest.TestCase):
    def test_deck_creation(self):
        valid_list = [Card(1, 1), Joker("Red"), Card(10, 2), Card("Queen", 1)]

        # Loop through every binary number from 0001 to 1111
        for i in range(1, 2 ** 4):
            # Generate the arguments for initialising based on the binary representation of i.
            arguments = generate_combinatory_arguments(format(i, '04b'), valid_list)
            deck = Deck(*arguments)

            # Check if the created deck contains cards in the expected order.
            for j in range(len(deck)):
                self.assertEqual(deck.cards[j], valid_list[j])

        # Create a deck with no input arguments to generate a standard deck.
        deck = Deck()
        valid_list = Deck.generate_standard_deck()
        for i in range(len(deck)):
            self.assertEqual(deck.cards[i], valid_list[i])

        # Test creating a deck with an invalid list containing a boolean (True).
        invalid_list = [Card(1, 1), Joker("Red"), True]
        with self.assertRaises(TypeError):
            Deck(*invalid_list)

        # Test creating a deck with an invalid list of arguments (mixed types).
        with self.assertRaises(TypeError):
            Deck(invalid_list)

        # Test creating a deck with a tuple containing an invalid list (mixed types).
        with self.assertRaises(TypeError):
            Deck(tuple(invalid_list))

    def test_deck_string(self):
        # Create a deck with a variety of cards.
        deck = Deck(Card(1, 1), Joker("Red"), Card(10, 2), Card("Queen", 1))

        # Test the string representation of the deck in the default format.
        self.assertEqual(str(deck), "D[Ace of Clubs, Red Joker, 10 of Spades, Queen of Clubs]")

        # Enable the short string format for cards and test the deck string representation.
        Card.set_short_str_format(True)
        self.assertEqual(str(deck), "D[A♣, RJ, 10♠, Q♣]")

        # Reset the card format to the default (False) for subsequent tests.
        Card.set_short_str_format(False)

    def test_deck_sorting(self):
        # Create a deck with a variety of cards.
        deck = Deck(Card(1, 1), Joker("Red"), Card(10, 2), Card("Queen", 1))

        # Create a sorted deck by rank and compare it with the expected order.
        sorted_deck = deck.copy()
        sorted_deck.sort_by_rank()
        valid_list = [Joker("Red"), Card(10, 2), Card("Queen", 1), Card(1, 1)]
        for i in range(len(sorted_deck.cards)):
            self.assertEqual(sorted_deck.cards[i], valid_list[i])

        # Set Ace to be worth 1 and sort by rank again.
        Card.set_ace_worth_1(True)
        sorted_deck = deck.copy()
        sorted_deck.sort_by_rank()
        valid_list = [Joker("Red"), Card(1, 1), Card(10, 2), Card("Queen", 1)]
        for i in range(len(sorted_deck.cards)):
            self.assertEqual(sorted_deck.cards[i], valid_list[i])

        # Reset Ace worth and sort the deck by suit, then compare with the expected order.
        Card.set_ace_worth_1(False)
        sorted_deck = deck.copy()
        sorted_deck.sort_by_suit()
        valid_list = [Joker("Red"), Card("Queen", 1), Card(1, 1), Card(10, 2)]
        for i in range(len(sorted_deck.cards)):
            self.assertEqual(sorted_deck.cards[i], valid_list[i])

        # Set Ace to be worth 1 and sort by suit again.
        Card.set_ace_worth_1(True)
        sorted_deck = deck.copy()
        sorted_deck.sort_by_suit()
        valid_list = [Joker("Red"), Card(1, 1), Card("Queen", 1), Card(10, 2)]
        for i in range(len(sorted_deck.cards)):
            self.assertEqual(sorted_deck.cards[i], valid_list[i])

        # Reset Ace worth for subsequent tests.
        Card.set_ace_worth_1(False)

    def test_card_adding(self):
        # Define initial cards and cards to add.
        initial_cards = [Joker(False), Card(7, 3)]
        cards_to_add = [Card(1, 1), Joker("Red"), Card(10, 2), Card("Queen", 1)]

        # Create a deck with the initial cards.
        deck = Deck(initial_cards)

        # Define valid lists for testing different index scenarios.
        valid_list_none = initial_cards + cards_to_add
        valid_list_0 = cards_to_add + initial_cards
        valid_list_neg1 = [initial_cards[0]] + cards_to_add + [initial_cards[-1]]

        # Loop through every binary number from 0001 to 1111.
        for k in range(1, 2 ** 4):
            binary_k = format(k, '04b')
            # Generate the arguments for adding based on the binary representation of k.
            args = generate_combinatory_arguments(binary_k, cards_to_add)

            # Determine the index where the cards should be added based on the binary representation.
            index = None if binary_k[-1] == '1' else -1

            # Iterate between two scenarios (j = 0 and j = 1).
            for j in range(2):
                test_deck = deck.copy()

                # Add cards to the test deck using the determined index.
                test_deck.add(*args, index=(index if j == 0 else 0))

                # Determine the expected order of cards in the test deck based on the index and binary representation.
                valid_list = valid_list_0 if j == 1 else valid_list_none if index is None else valid_list_neg1

                # Compare the cards in the test deck with the corresponding cards in the valid list.
                for i in range(len(test_deck)):
                    self.assertEqual(test_deck.cards[i], valid_list[i])

        # Test adding no cards, ensuring the original deck remains unchanged.
        deck.add()
        for i in range(len(deck)):
            self.assertEqual(deck.cards[i], initial_cards[i])

        # Test adding cards with an incorrect list containing a boolean (True).
        incorrect_list = [Card(1, 1), Joker("Red"), True]
        with self.assertRaises(TypeError):
            deck.add(*incorrect_list)

        # Test adding cards with an incorrect list of arguments (mixed types).
        with self.assertRaises(TypeError):
            deck.add(incorrect_list)

        # Test adding cards with a tuple containing an incorrect list (mixed types).
        with self.assertRaises(TypeError):
            deck.add(tuple(incorrect_list))

        # Test adding cards with an invalid index (out of range).
        with self.assertRaises(IndexError):
            deck.add(cards_to_add, index=4)

        # Test adding cards with an invalid index (not an integer).
        with self.assertRaises(TypeError):
            deck.add(cards_to_add, index=True)

    def test_card_removing(self):
        # Define the initial list of cards for the deck.
        initial_list = [Card(1, 1), Joker("Red"), Card(10, 2), Card("Queen", 1),
                        Joker(False), Card(7, 3), Card(10, 2), Joker("Red")]
        deck = Deck(initial_list)

        # Loop through every binary number from 0000001 to 1111111.
        for i in range(1, 2 ** 7):
            binary_i = format(i, '07b')

            # Initialize lists and variables for card removal operations.
            list_to_remove = []
            list_to_have = initial_list[:]

            indexes_to_remove = []  # Track individual indexes for removal.
            cards_to_remove = []  # Track individual cards for removal.

            # Check each bit of the binary representation to determine the removal strategy.
            if binary_i[-1] == '1':  # ......1 : Individual indexes
                list_to_remove.append(0)
                indexes_to_remove.append(0)
            if binary_i[-2] == '1':  # .....1. : Individual cards
                list_to_remove.append(Card(1, 1))
                cards_to_remove.append(Card(1, 1))
            if binary_i[-3] == '1':  # ....1.. : List of indexes
                list_to_remove.append([0, 2])
                if 0 in indexes_to_remove:
                    indexes_to_remove.append(2)
                else:
                    indexes_to_remove += [0, 2]
            if binary_i[-4] == '1':  # ...1... : List of cards
                list_to_remove.append([Card(10, 2), Joker(False)])
                cards_to_remove += [Card(10, 2), Joker(False)]
            if binary_i[-5] == '1':  # ..1.... : Tuple of indexes
                list_to_remove.append((4, -3))
                indexes_to_remove += [4, -3]
            if binary_i[-6] == '1':  # .1..... : Tuple of cards
                list_to_remove.append((Card(10, 2), Card(7, 3)))
                cards_to_remove += [Card(10, 2), Card(7, 3)]
            if binary_i[-7] == '1':  # 1...... : Deck of cards
                cards_to_remove += [Joker(True), Card("Queen", 1)]
                list_to_remove.append(Deck(cards_to_remove[-1], cards_to_remove[-2]))

            # Reverse the order of indexes to remove cards from the end of the list first.
            indexes_to_remove.reverse()

            # Remove cards and indexes from the 'list_to_have' based on the removal strategy.
            for ind in indexes_to_remove:
                list_to_have.pop(ind)
            for card in cards_to_remove:
                if card in list_to_have:
                    list_to_have.remove(card)

            test_deck = deck.copy()
            test_deck.remove(*list_to_remove)

            # Compare the cards in the test deck with the expected 'list_to_have'.
            for j in range(max(len(test_deck), len(list_to_have))):
                self.assertEqual(test_deck.cards[j], list_to_have[j])

        # Test removing no cards from the deck.
        deck.remove()
        for i in range(len(initial_list)):
            self.assertEqual(initial_list[i], deck.cards[i])

        # Test removing cards with an incorrect list containing a boolean (True).
        incorrect_list = [Card(1, 1), Joker("Red"), True]
        with self.assertRaises(TypeError):
            deck.remove(*incorrect_list)

        # Test removing cards with an incorrect list of arguments (mixed types).
        with self.assertRaises(TypeError):
            deck.remove(incorrect_list)

        # Test removing cards with a tuple containing an incorrect list (mixed types).
        with self.assertRaises(TypeError):
            deck.remove(tuple(incorrect_list))

        # Test removing cards with an invalid index (out of range).
        with self.assertRaises(IndexError):
            deck.remove(9)

        # Test removing a card that does not exist in the deck.
        with self.assertRaises(ValueError):
            deck.remove(Card(8, 4))  # Should raise a ValueError.

    def test_card_indexing(self):
        # Define the initial list of cards for the deck.
        initial_list = [Card(1, 1), Joker("Red"), Card(10, 2), Card("Queen", 1),
                        Joker(False), Card(7, 3), Card(10, 2), Joker("Red")]
        deck = Deck(initial_list)

        # Define a list of cards to be indexed in the deck.
        cards_to_index = [Card(1, 1), Card(10, 2), Joker(False), Card(7, 3)]

        # Loop through every binary number from 0001 to 1111.
        for i in range(1, 2 ** 4):
            # Generate the arguments for indexing based on the binary representation of i.
            arguments = generate_combinatory_arguments(format(i, '04b'), cards_to_index)
            # Perform indexing on the deck with the specified arguments.
            indexes = deck.index(*arguments)
            # Ensure that the retrieved indexes match the expected indexes.
            self.assertEqual((0, 2, 4, 5), indexes)

        # Test indexing with no arguments (should return None).
        self.assertIsNone(deck.index())

        # Test indexing with an incorrect list containing a boolean (True).
        incorrect_type_list = [Card(1, 1), Joker("Red"), True]
        with self.assertRaises(TypeError):
            deck.index(*incorrect_type_list)  # Should raise a TypeError.

        # Test indexing with an incorrect list of card arguments (including an invalid card).
        incorrect_card_list = [Card(1, 1), Joker("Red"), Card("King", "Hearts")]
        with self.assertRaises(ValueError):
            deck.index(*incorrect_card_list)

        # Test indexing with an incorrect list containing a boolean (True).
        with self.assertRaises(TypeError):
            deck.index(incorrect_type_list)

        # Test indexing with an incorrect list of card arguments (including an invalid card).
        with self.assertRaises(ValueError):
            deck.index(incorrect_card_list)

        # Test indexing with a tuple containing incorrect types (including a boolean and an incorrect card type).
        with self.assertRaises(TypeError):
            deck.index(tuple(incorrect_type_list))

        # Test indexing with a tuple of card arguments (including an invalid card).
        with self.assertRaises(ValueError):
            deck.index(tuple(incorrect_card_list))

        # Test indexing with a deck containing incorrect types (including a boolean in the deck).
        with self.assertRaises(TypeError):
            testing_deck = Deck(incorrect_type_list[:2])
            testing_deck.cards.append(True)
            deck.index(testing_deck)

        # Test indexing with a deck containing an incorrect card (invalid card type).
        with self.assertRaises(ValueError):
            deck.index(Deck(incorrect_card_list))

    def test_card_getter(self):
        # Define the initial list of cards for the deck.
        initial_list = [Card(1, 1), Joker("Red"), Card(10, 2), Card("Queen", 1),
                        Joker(False), Card(7, 3), Card(10, 2), Joker("Red")]
        deck = Deck(initial_list)

        # Define a list of indexes to retrieve cards from the deck.
        indexes_to_grab = [0, 2, 4, 5]
        deck_to_have = Deck(Card(1, 1), Card(10, 2), Joker(False), Card(7, 3))

        # Loop through every binary number from 001 to 111.
        for i in range(1, 2 ** 3):
            binary_i = format(i, '03b')

            # Generate the arguments for the 'get' function based on the binary representation of i.
            arguments = generate_combinatory_arguments('0' + binary_i, indexes_to_grab)

            # Retrieve cards from the deck based on the specified indexes.
            cards = deck.get(*arguments)

            # Compare the retrieved cards with the corresponding cards in 'deck_to_have'.
            for j in range(max(len(cards), len(deck_to_have))):
                self.assertEqual(cards.get(j), deck_to_have.get(j))

        # Test retrieving a specific card (Joker("Red")).
        self.assertEqual(Joker("Red"), deck.get())

        # Test retrieving cards with an incorrect list containing mixed types (int, float).
        incorrect_type_list = [0, 1, 1.5]
        with self.assertRaises(TypeError):
            deck.get(*incorrect_type_list)

        # Test retrieving cards with an incorrect list containing an out-of-range index (9).
        out_of_range_list = [0, 1, 9]
        with self.assertRaises(IndexError):
            deck.get(*out_of_range_list)

        # Test retrieving cards with an incorrect list of arguments (mixed types).
        with self.assertRaises(TypeError):
            deck.get(incorrect_type_list)

        # Test retrieving cards with an incorrect list of arguments (out-of-range index).
        with self.assertRaises(IndexError):
            deck.get(out_of_range_list)

        # Test retrieving cards with a tuple containing mixed types (int, float).
        with self.assertRaises(TypeError):
            deck.get(tuple(incorrect_type_list))  # Should raise a TypeError.

        # Test retrieving cards with a tuple containing an out-of-range index (9).
        with self.assertRaises(IndexError):
            deck.get(tuple(out_of_range_list))

    def test_deck_selection(self):
        # Create a 54 card deck.
        deck = Deck()

        # Verify that the selecting all cards in a deck matches the original deck.
        test_deck = deck.select()
        for i in range(len(deck)):
            self.assertEqual(deck.get(i), test_deck.get(i))

        # Loop through every binary number from 0001 to 1111.
        for i in range(1, 2 ** 4):
            # Generate the binary representation for arguments (4 bits).
            binary_i = format(i, '04b')

            # Define lists for ranks, suits, colors, and face_cards.
            ranks = [None]
            suits = [None]
            colors = [None]
            face_cards = [None]

            # Check the binary flags and update corresponding lists.
            if binary_i[-1] == '1':  # ...1
                ranks = [2, -2, "King", "!King", [2, 3, 4, 5], [-2, -3, -4, -5], [2, 3, -4, -5],
                         ["King", "Queen", "Jack"], ["!King", "!Queen", "!Jack"], ["King", "Queen", "!Jack"]]
            if binary_i[-2] == '1':  # ..1.
                suits = [1, -1, "Hearts", "!Hearts", [1, 2], [-3], [1, 2, -3], ["Hearts", "Diamonds"], ["!Clubs"],
                         ["Hearts", "Diamonds", "!Clubs"]]
            if binary_i[-3] == '1':  # .1..
                colors = [True, "Black"]
            if binary_i[-4] == '1':  # 1...
                face_cards = [True]

            # Iterate through different combinations of rank, suit, color, and face_card.
            for rank in ranks:
                for suit in suits:
                    for color in colors:
                        for face_card in face_cards:
                            valid_list = deck.cards[:]

                            # Prepare lists for rank and suit selection (inclusion/exclusion).
                            list_rank = [rank] if type(rank) not in [list, tuple] else list(rank)
                            list_suit = [suit] if type(suit) not in [list, tuple] else list(suit)

                            testing_ranks = list_rank[:]
                            excluded_ranks = []
                            testing_suits = list_suit[:]
                            excluded_suits = []

                            # Prepare lists for rank and suit exclusion.
                            for lists in [(testing_ranks, excluded_ranks), (testing_suits, excluded_suits)]:
                                if lists[0][0]:
                                    lists[0].reverse()
                                    done = False
                                    while not done and len(lists[0]) > 0:
                                        if type(lists[0][0]) is int and lists[0][0] < 0:
                                            lists[1].append(lists[0].pop(0))
                                        elif type(lists[0][0]) is str and lists[0][0].startswith("!"):
                                            lists[1].append(lists[0].pop(0))
                                        else:
                                            done = True

                            # Apply exclusions/inclusions to the valid list.
                            j = 0
                            while j < len(valid_list):
                                if list_rank[0] is not None and ('!' + valid_list[j].get_rank() in excluded_ranks or
                                                                 -valid_list[j].rank in excluded_ranks or
                                                                 (valid_list[j].get_rank() not in testing_ranks and
                                                                  valid_list[j].rank not in testing_ranks)):
                                    valid_list.pop(j)
                                elif list_suit[0] is not None and ('!' + valid_list[j].get_suit() in excluded_suits or
                                                                   -valid_list[j].suit in excluded_suits or
                                                                   (valid_list[j].get_suit() not in testing_suits and
                                                                    valid_list[j].suit not in testing_suits)):
                                    valid_list.pop(j)
                                elif color is not None and not valid_list[j].has_color(color):
                                    valid_list.pop(j)
                                elif face_card is not None and valid_list[j].face_card != face_card:
                                    valid_list.pop(j)
                                else:
                                    j += 1

                            # Select a deck based on specified criteria.
                            test_deck = deck.select(rank=rank, suit=suit, color=color, face_card=face_card)

                            # Ensure that all cards in the test deck are in the valid list.
                            for j in range(max(len(test_deck), len(valid_list))):
                                self.assertTrue(test_deck.get(j) in valid_list)

        # Define a function to determine input type (Individual, List, or Tuple).
        def get_input_type(elt):
            if input_type == "Individual":
                return elt
            if input_type == "List":
                return [elt]
            return tuple([elt])

        # Define lists of incorrect ranks and suits.
        incorrect_ranks = [14, -14, "Knight"]
        incorrect_suits = [5, -5, "Club"]

        # Iterate through input types (Individual, List, Tuple) and check for exceptions.
        for input_type in ["Individual", "List", "Tuple"]:
            # Check for exceptions with incorrect ranks.
            for rank in incorrect_ranks:
                with self.assertRaises(ValueError):
                    deck.select(rank=get_input_type(rank))
            # Check for exceptions with incorrect rank types.
            with self.assertRaises(TypeError):
                deck.select(rank=get_input_type(5.2))

            # Check for exceptions with incorrect suits.
            for suit in incorrect_suits:
                with self.assertRaises(ValueError):
                    deck.select(suit=get_input_type(suit))
            # Check for exceptions with incorrect suit types.
            with self.assertRaises(TypeError):
                deck.select(suit=get_input_type(5.2))

        # Check for exceptions with incorrect color values.
        with self.assertRaises(ValueError):
            deck.select(color="Green")
        # Check for exceptions with incorrect color types.
        with self.assertRaises(TypeError):
            deck.select(color=5.2)

        # Check for exceptions with incorrect face_card types.
        with self.assertRaises(TypeError):
            deck.select(face_card=5.2)


if __name__ == "__main__":
    unittest.main()
