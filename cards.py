from random import shuffle, choice, randint


class Card:
    """
    Represents a playing card.

    Attributes:
        - suit (int): The suit of the card (1 for Clubs, 2 for Spades, 3 for Diamonds, 4 for Hearts).
        - rank (int): The rank of the card (1 for Ace, 2-10 for number cards, 11 for Jack, 12 for Queen, 13 for King).
        - color (bool): The color of the card (False for black, True for red).
        - face_card (bool): True if the card is a face card (Jack, Queen, King), otherwise False.

    Class Variables:
        - __short_form_str (bool): If True, the string representation will use a short form (e.g., "A♠" for Ace of Spades).
          If False, the string representation will use the long form (e.g., "Ace of Spades").
        - __ace_worth_1 (bool): If True, aces are considered to be worth 1, and not the highest card in the deck.

    """

    # Class variable to store Unicode representations of playing cards
    __card_unicode = {
        1: {
            1: "🃑", 2: "🃒", 3: "🃓", 4: "🃔", 5: "🃕",
            6: "🃖", 7: "🃗", 8: "🃘", 9: "🃙", 10: "🃚",
            11: "🃛", 12: "🃝", 13: "🃞"
        },
        2: {
            1: "🂡", 2: "🂢", 3: "🂣", 4: "🂤", 5: "🂥",
            6: "🂦", 7: "🂧", 8: "🂨", 9: "🂩", 10: "🂪",
            11: "🂫", 12: "🂭", 13: "🂮"
        },
        3: {
            1: "🃁", 2: "🃂", 3: "🃃", 4: "🃄", 5: "🃅",
            6: "🃆", 7: "🃇", 8: "🃈", 9: "🃉", 10: "🃊",
            11: "🃋", 12: "🃍", 13: "🃎"
        },
        4: {
            1: "🂱", 2: "🂲", 3: "🂳", 4: "🂴", 5: "🂵",
            6: "🂶", 7: "🂷", 8: "🂸", 9: "🂹", 10: "🂺",
            11: "🂻", 12: "🂽", 13: "🂾"
        }
    }

    # Class variables to store possible values for suits and ranks given in methods parameters
    __suits = {"Clubs": 1, "Spades": 2, "Diamonds": 3, "Hearts": 4}
    __ranks = {"Ace": 1,
               "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10,
               "Jack": 11, "Queen": 12, "King": 13}

    # Indicates whether to use a short form string representation
    __short_form_str = False
    # Indicates whether the Ace is the highest card or if it is worth 1
    __ace_worth_1 = False

    def __init__(self, rank: int | str, suit: int | str) -> None:
        """
        Initializes a Card object with the provided rank and suit.

        Args:
            rank (int | str): The rank of the card.
                - If an integer, must be greater than or equal to 1 and less than or equal to 13.
                - If a string, must be one of the following: "Ace", "2" to "10", "Jack", "Queen", or "King".
            suit (int | str): The suit of the card.
                - If an integer, must be greater than or equal to 1 and less than or equal to 4.
                - If a string, must be one of the following: "Clubs", "Spades", "Diamonds", or "Hearts".

        Note:
            - For `rank`, 1 represents Ace, 2 to 10 represent number cards, 11 represents Jack, 12 represents Queen, and 13 represents King.
            - For `suit`, 1 represents Clubs, 2 represents Spades, 3 represents Diamonds, and 4 represents Hearts.

        Raises:
            ValueError: If the provided `rank` or `suit` values are outside the valid range or not recognized.
            TypeError: If the provided `rank` or `suit` values are not integers or strings.
        """
        if not (type(rank) in (int, str) and type(suit) in (int, str)):
            raise TypeError("Rank and suit must be integers or strings.")

        if type(rank) is str:
            if rank in self.__ranks:
                rank = self.__ranks.get(rank)
            else:
                raise ValueError("Invalid rank or suit values provided.")

        if type(suit) is str:
            if suit in self.__suits:
                suit = self.__suits.get(suit)
            else:
                raise ValueError("Invalid rank or suit values provided.")

        if 1 <= rank <= 13 and 1 <= suit <= 4:
            self.suit = suit
            self.rank = rank
            self.color = self.suit > 2
            self.face_card = self.rank > 10
        else:
            raise ValueError("Invalid rank or suit values provided.")

    def __str__(self):
        """
        Get a string representation of the card.

        Returns:
            str: A string representing the card, e.g.,
                 "Ace of Spades" or short form ("A♠") depending on the value of '__short_form_str'.
        """
        if self.__short_form_str is False:
            return self.get_rank() + " of " + self.get_suit()
        return self.get_rank_unicode() + self.get_suit_unicode()

    def _check_correct_attributes(self):
        if type(self.rank) is not int:
            raise TypeError("Wrong rank type")
        if type(self.suit) is not int:
            raise TypeError("Wrong suit type")
        if self.rank < 1 or self.rank > 13:
            raise ValueError("Wrong rank value")
        if self.suit < 1 or self.suit > 4:
            raise ValueError("Wrong suit value")
        if type(self.color) is not bool:
            raise TypeError("Wrong color type")
        if type(self.face_card) is not bool:
            raise TypeError("Wrong face_card type")

    @staticmethod
    def set_short_str_format(short: bool):
        """
        Set the string representation form for Card objects.

        Args:
            short (bool): If True, the string representation will use a short form
                (e.g., "A♠" for Ace of Spades). If False, the string representation will use
                the long form (e.g., "Ace of Spades").

        Note:
            The default string representation form is the long form.

        Raises:
            TypeError: If `short` is not a boolean value.
        """
        if type(short) is not bool:
            raise TypeError("The 'short' argument must be a boolean value.")
        Card.__short_form_str = short

    @staticmethod
    def short_form_str():
        """
        Check if the short string representation format for Card objects is currently enabled.

        Returns:
            bool: True if the short form representation is enabled, False otherwise.

        Note:
            The short form representation uses abbreviated strings (e.g., "3♠" for 3 of Spades) while
            the long form representation uses full strings (e.g., "3 of Spades").
        """
        return Card.__short_form_str

    @staticmethod
    def set_ace_worth_1(worth_1: bool):
        """
        Set the value of aces in the deck.

        Args:
            worth_1 (bool): If True, aces are considered to be worth 1, and not the highest card in the deck.
            If False, aces are considered to be the highest card in the deck.

        Note:
            By default, aces are considered to be the highest card in the deck (worth 14).

        Raises:
            TypeError: If `worth_1` is not a boolean value.
        """
        if type(worth_1) is not bool:
            raise TypeError("The 'worth_1' argument must be a boolean value.")
        Card.__ace_worth_1 = worth_1

    @staticmethod
    def get_ace_value():
        """
        Get the value associated with Ace cards.

        Returns:
            int: The value of Ace cards. If Aces are worth 1 in the Card configuration, it returns 1.
                 If Aces are considered the highest card in the deck (default), it returns 14.
        """
        return 1 if Card.__ace_worth_1 else 14

    @staticmethod
    def get_ranks():
        """
        Get a set of all possible card ranks.

        Returns:
            set: A set containing all possible card ranks.

        Note:
            The set includes standard playing card ranks (e.g., "2", "3", "4", ..., "10", "Jack", "Queen", "King", "Ace").
        """
        return set(Card.__ranks.keys())

    @staticmethod
    def get_suits():
        """
        Get a set of all possible card suits.

        Returns:
            set: A set containing all possible card suits.

        Note:
            The set includes standard playing card suits (e.g., "Hearts", "Diamonds", "Clubs", "Spades").
        """
        return set(Card.__suits.keys())

    def same_rank(self, other):
        """
        Check if this card has the same rank as another card.

        Args:
            other (Card): The other card to compare with.

        Returns:
            bool: True if both cards have the same rank, otherwise False.

        Raises:
            ValueError: If `other` is not a Card object.
        """
        if type(other) not in [Card, Joker]:
            raise ValueError("Comparisons with a card must be with another Card object.")
        return self.rank == other.rank

    def same_suit(self, other):
        """
        Check if this card has the same suit as another card.

        Args:
            other (Card): The other card to compare with.

        Returns:
            bool: True if both cards have the same suit, otherwise False.

        Raises:
            ValueError: If `other` is not a Card object.
        """
        if type(other) not in [Card, Joker]:
            raise ValueError("Comparisons with a card must be with another Card object.")
        return self.suit == other.suit

    def same_color(self, other):
        """
        Check if this card has the same color as another card.

        Args:
            other (Card): The other card to compare with.

        Returns:
            bool: True if both cards have the same color, otherwise False.

        Raises:
            ValueError: If `other` is not a Card object.
        """
        if type(other) not in [Card, Joker]:
            raise ValueError("Comparisons with a card must be with another Card object.")
        return self.color == other.color

    def has_rank(self, rank):
        """
        Check if the card has the specified rank.

        Args:
            rank (str): The rank to check.

        Returns:
            bool: True if the card has the specified rank, False otherwise.
        """
        rank = self.__ranks.get(rank, rank)
        return self.rank == rank

    def has_suit(self, suit):
        """
        Check if the card has the specified suit.

        Args:
            suit (str): The suit to check.

        Returns:
            bool: True if the card has the specified suit, False otherwise.
        """
        suit = self.__suits.get(suit, suit)
        return self.suit == suit

    def has_color(self, color):
        """
        Check if the card has the specified color.

        Args:
            color (str or bool): The color to check. If a string, use "Red" for red, "Black" for black.
            If a boolean, use True for red, False for black.

        Returns:
            bool: True if the card has the specified color, False otherwise.
        """
        if type(color) is str:
            color = color == "Red"
        return self.color == color

    def get_suit(self):
        """
        Get the suit of the card as a string.

        Returns:
            str: The suit of the card ("Clubs", "Spades", "Diamonds", or "Hearts").
        """
        self._check_correct_attributes()
        return {1: "Clubs", 2: "Spades", 3: "Diamonds", 4: "Hearts"}.get(self.suit)

    def get_rank(self):
        """
        Get the rank of the card as a string.

        Returns:
            str: The rank of the card ("Ace", "2" to "10", "Jack", "Queen", or "King").
        """
        self._check_correct_attributes()
        if self.rank == 1:
            return "Ace"
        elif self.rank > 10:
            return {11: "Jack", 12: "Queen", 13: "King"}.get(self.rank)
        return str(self.rank)

    def get_color(self):
        """
        Get the color of the card as a string.

        Returns:
            str: The color of the card ("Black" for Clubs and Spades, "Red" for Diamonds and Hearts).
        """
        self._check_correct_attributes()
        return "Red" if self.color else "Black"

    def get_rank_unicode(self):
        """
        Get the Unicode character for the rank of the card.

        Returns:
            str: The Unicode character representing the rank.
        """
        self._check_correct_attributes()
        ranks_unicode = {
            1: "A", 2: "2", 3: "3", 4: "4", 5: "5",
            6: "6", 7: "7", 8: "8", 9: "9", 10: "10",
            11: "J", 12: "Q", 13: "K"
        }
        return ranks_unicode.get(self.rank)

    def get_suit_unicode(self):
        """
        Get the Unicode symbol for the suit of the card.

        Returns:
            str: The Unicode symbol representing the suit (♣, ♠, ♦, ♥).
        """
        self._check_correct_attributes()
        suits_unicode = {1: "♣", 2: "♠", 3: "♦", 4: "♥"}
        return suits_unicode.get(self.suit)

    def get_card_unicode(self):
        """
        Get the Unicode representation of the playing card.

        Returns:
            str: The Unicode representation of the card (e.g., "🂡" for Ace of Spades).
        """
        self._check_correct_attributes()
        return self.__card_unicode.get(self.suit, {}).get(self.rank)

    def copy(self):
        """
        Create a deep copy of the card.

        Returns:
            Card: A new Card with the same attributes as the original card.

        Note:
            The 'copy' method creates a new Card with the same rank, suit, color, face card status,
            and other attributes as the original card.
        """
        copy_card = Card(1, 1)
        copy_card.rank = self.rank
        copy_card.suit = self.suit
        copy_card.color = self.color
        copy_card.face_card = self.face_card
        return copy_card

    def __lt__(self, other):
        """
        Compare this card with another card using the less than operator based on rank.

        Args:
            other (Card): The other card to compare with.

        Returns:
            bool: True if this card's rank is less than the other card's rank, considering the value of Aces.
            Otherwise, False.

        Raises:
            ValueError: If `other` is not a Card object.
        """
        if type(other) not in [Card, Joker]:
            raise ValueError("Comparisons with a card must be with another Card object.")

        other_rank = self.get_ace_value() if other.rank == 1 else other.rank
        self_rank = self.get_ace_value() if self.rank == 1 else self.rank
        return self_rank < other_rank

    def __le__(self, other):
        """
        Compare this card with another card using the less than or equal to operator based on rank.

        Args:
            other (Card): The other card to compare with.

        Returns:
            bool: True if this card's rank is less than or equal to the other card's rank, considering the value of Aces.
            Otherwise, False.

        Raises:
            ValueError: If `other` is not a Card object.
        """
        if type(other) not in [Card, Joker]:
            raise ValueError("Comparisons with a card must be with another Card object.")

        other_rank = self.get_ace_value() if other.rank == 1 else other.rank
        self_rank = self.get_ace_value() if self.rank == 1 else self.rank
        return self_rank <= other_rank

    def __eq__(self, other):
        """
        Compare this card with another card for equality.

        Args:
            other (Card): The other card to compare with.

        Returns:
            bool: True if both cards are the exact same, otherwise False.

        Raises:
            ValueError: If `other` is not a Card object.
        """
        if type(other) not in [Card, Joker]:
            raise ValueError("Comparisons with a card must be with another Card object.")
        return self.same_rank(other) and self.same_suit(other) and self.same_color(other) and self.face_card == other.face_card

    def __ne__(self, other):
        """
        Compare this card with another card for inequality.

        Args:
            other (Card): The other card to compare with.

        Returns:
            bool: True if the cards have different ranks, otherwise False.

        Raises:
            ValueError: If `other` is not a Card object.
        """
        return not self.__eq__(other)

    def __gt__(self, other):
        """
        Compare this card with another card using the greater than operator based on rank.

        Args:
            other (Card): The other card to compare with.

        Returns:
            bool: True if this card's rank is greater than the other card's rank, considering the value of Aces.
            Otherwise, False.

        Raises:
            ValueError: If `other` is not a Card object.
        """
        if type(other) not in [Card, Joker]:
            raise ValueError("Comparisons with a card must be with another Card object.")

        other_rank = self.get_ace_value() if other.rank == 1 else other.rank
        self_rank = self.get_ace_value() if self.rank == 1 else self.rank
        return self_rank > other_rank

    def __ge__(self, other):
        """
        Compare this card with another card using the greater than or equal to operator based on rank.

        Args:
            other (Card): The other card to compare with.

        Returns:
            bool: True if this card's rank is greater than or equal to the other card's rank, considering the value of Aces.
            Otherwise, False.

        Raises:
            ValueError: If `other` is not a Card object.
        """
        if type(other) not in [Card, Joker]:
            raise ValueError("Comparisons with a card must be with another Card object.")

        other_rank = self.get_ace_value() if other.rank == 1 else other.rank
        self_rank = self.get_ace_value() if self.rank == 1 else self.rank
        return self_rank >= other_rank


class Joker(Card):
    """
    Represents a Joker card.

    Attributes:
        - color (int): The color of the Joker card (0 for black, 1 for red).
    """

    def __init__(self, color: bool | str) -> None:
        """
        Initializes a Joker card.

        Args:
            color (int | str): The color of the Joker card.
                - If an integer, use False for black or True for red.
                - If a string, use "Black" for black or "Red" for red.

        Raises:
            ValueError: If an invalid color value is provided.
        """
        super().__init__(1, 1)
        if type(color) is str:
            if color in ("Red", "Black"):
                color = color == "Red"
            else:
                raise ValueError("Invalid color value for Joker card. Use 'Black' or 'Red' for color.")
        if type(color) is bool:
            self.suit = 0  # Suit 0 represents Joker
            self.rank = 0  # Rank 0 represents Joker
            self.face_card = True
            self.color = color
        else:
            raise TypeError("Invalid color value for Joker card. Use False for black or True for red.")

    def __str__(self):
        """
        Get a string representation of the Joker card.

        Returns:
            str: A string representing the Joker card, e.g., "Black Joker" or "Red Joker".
        """
        if Card.short_form_str() is False:
            return self.get_suit() + " " + self.get_rank()
        return self.get_suit_unicode() + self.get_rank_unicode()

    def _check_correct_attributes(self):
        if type(self.rank) is not int:
            raise TypeError("Wrong rank type")
        if type(self.suit) is not int:
            raise TypeError("Wrong suit type")
        if self.rank != 0:
            raise ValueError("Wrong rank value")
        if self.suit != 0:
            raise ValueError("Wrong suit value")
        if type(self.color) is not bool:
            raise TypeError("Wrong color type")
        if type(self.face_card) is not bool:
            raise TypeError("Wrong face_card type")
        if not self.face_card:
            raise ValueError("Wrong face_card value")

    @staticmethod
    def set_short_str_format(short: bool):
        """
        Set the string representation form for Card objects.

        Args:
            short (bool): If True, the string representation will use a short form
                (e.g., "RJ" for Red Joker). If False, the string representation will use
                the long form (e.g., "Black Joker").

        Note:
            The default string representation form is the long form.

        Raises:
            ValueError: If `short` is not a boolean value.
        """
        Card.set_short_str_format(short)

    def get_rank(self):
        """
        Get the rank of the Joker card.

        Returns:
            str: The rank, which is always "Joker".
        """
        return "Joker"

    def get_suit(self):
        """
        Get the suit of the Joker card. (aka the color)

        Returns:
            str: The 'suit' of the card ("Black" for Black Joker, "Red" for Red Joker).
        """
        self._check_correct_attributes()
        return self.get_color()

    def get_rank_unicode(self):
        """
        Get the Unicode character for the rank of the Joker card.

        Returns:
            str: The Unicode character representing the rank, which is "J".
        """
        return "J"

    def get_suit_unicode(self):
        """
        Get the Unicode symbol for the "suit", or in this case, the color of the Joker card.

        Returns:
            str: The Unicode symbol representing the color, which is "B" for black Joker or "R" for red Joker.
        """
        self._check_correct_attributes()
        return "R" if self.color else "B"

    def get_card_unicode(self):
        """
        Get the Unicode representation of the Joker card.

        Returns:
            str: The Unicode representation of the Joker card ("🃏" for black Joker, "🂿" for red Joker).
        """
        self._check_correct_attributes()
        return "🂿" if self.color else "🃏"

    def copy(self):
        """
        Create a deep copy of the Joker card.

        Returns:
            Joker: A new Joker card with the same attributes as the original card.

        Note:
            The 'copy' method creates a new Joker card with the same rank, suit (color), face card status,
            and color attributes as the original card.
        """
        copy_joker = Joker(True)
        copy_joker.rank = self.rank
        copy_joker.suit = self.suit
        copy_joker.color = self.color
        copy_joker.face_card = self.face_card
        return copy_joker


class Deck:
    """
    Represents a deck of playing cards.

    Attributes:
        cards (list of Card): The list of Card objects in the deck.
    """

    def __init__(self, *cards):
        """
        Initialize a deck of cards.

        Args:
            *cards: Accepts a variable number of Card objects and/or lists/tuples of Card objects to be added to the deck.
                If no cards are provided, a standard 54-card French-suited playing card deck with Jokers will be created.
        """
        if cards:
            flattened_list = _flatten_nested_collections(cards)
            for card in flattened_list:
                if type(card) not in [Card, Joker]:
                    raise TypeError("Only Card objects can be provided")
            self.cards = flattened_list
        else:
            self.cards = self.generate_standard_deck()

    @staticmethod
    def generate_standard_deck():
        """
        Generate a standard French-suited playing card deck with 54 cards, including 2 Jokers.

        Returns:
            list of Card: A list of 54 Card objects representing the standard deck.
        """
        cards = [Card(rank, suit) for suit in Card.get_suits() for rank in Card.get_ranks()]
        jokers = [Joker("Black"), Joker("Red")]
        return cards + jokers

    def __str__(self):
        """
        Get a string representation of the deck.

        Returns:
            str: A string representing the deck, showing each card in the deck.
        """
        return 'D' + str([str(c) for c in self.cards]).replace("'", "")

    def __len__(self):
        """
        Get the number of cards in the deck.

        Returns:
            int: The number of cards currently in the deck.
        """
        return len(self.cards)

    def __getitem__(self, item):
        """
        Get a card or a subset of cards from the deck.

        Args:
            item (int or slice): The index or slice to retrieve the card(s).

        Returns:
            Card or list of Card: If 'item' is an integer, returns the card at that index. If 'item' is a slice,
            returns a list of cards from the specified slice.

        Raises:
            IndexError: If the index is out of range.
            TypeError: If 'item' is not an integer or a slice.
        """
        if type(item) is slice:
            start = len(self) + item.start if item.start < 0 else item.start
            if not (0 <= start < len(self)):
                raise IndexError("Starting index out of range.")
            stop = len(self) + item.stop if item.stop < 0 else item.stop
            if not (0 <= stop <= len(self)):
                raise IndexError("Stopping index out of range.")
            return Card(self.cards[item])
        elif type(item) is int:
            item = len(self) + item if item < 0 else item
            if not (0 <= item < len(self)):
                raise IndexError("Index out of range.")
            return self.cards[item]
        else:
            raise TypeError("Deck indices must be integers or slices")

    def __setitem__(self, key, value):
        """
        Set a card in the deck.

        Args:
            key (int): The index at which to set the card.
            value (Card or Joker): The card or Joker object to set in the deck.

        Raises:
            IndexError: If the index is out of range.
            TypeError: If 'value' is not a Card or Joker object.
        """
        if type(value) not in [Card, Joker]:
            raise TypeError("Only Card objects can be provided")
        key = len(self) + key if key < 0 else key
        if not (0 <= key < len(self)):
            raise IndexError("Index out of range.")
        self.cards[key] = value

    def __iter__(self):
        """
        Iterate over the cards in the deck.

        Returns:
            iter: An iterator over the cards in the deck.
        """
        return iter(self.cards)

    def __contains__(self, item):
        """
        Check if a card is in the deck.

        Args:
            item (Card): The card to check for.

        Returns:
            bool: True if the card is in the deck, False otherwise.
        """
        return item in self.cards

    def __hash__(self):
        """
        Calculate the hash value of the deck.

        Returns:
            int: The hash value of the deck.
        """
        return hash(tuple(self.cards))

    def __add__(self, other_deck):
        """
        Concatenate two decks.

        Args:
            other_deck (Deck): The deck to concatenate with.

        Returns:
            Deck: A new deck containing the cards from both decks.
        """
        if type(other_deck) is not Deck:
            raise TypeError("Can only concatenate with another Deck.")
        return Deck(self.cards + other_deck.cards)

    def __mul__(self, num):
        """
        Repeat the deck a specified number of times.

        Args:
            num (int): The number of times to repeat the deck.

        Returns:
            Deck: A new deck containing the cards repeated 'num' times.
        """
        if type(num) is not int or num < 0:
            raise ValueError("The number of repetitions must be a non-negative integer.")
        return Deck(self.cards * num)

    def __eq__(self, other_deck):
        """
        Check if two decks are equal.

        Args:
            other_deck (Deck): The deck to compare with.

        Returns:
            bool: True if the decks are equal, False otherwise.
        """
        if type(other_deck) is not Deck:
            return False
        return self.cards == other_deck.cards

    def __ne__(self, other_deck):
        """
        Check if two decks are not equal.

        Args:
            other_deck (Deck): The deck to compare with.

        Returns:
            bool: True if the decks are not equal, False otherwise.
        """
        return not self.__eq__(other_deck)

    def add(self, *cards, index=None):
        """
        Add one or more cards to the deck. Cards can be added at a specified index or at the end.

        Args:
            *cards: Variable number of Card objects and/or lists/tuples of Card objects to be added to the deck.
            index (int, optional): The index at which to insert the cards. If None, cards are added at the end.
        """
        if index is not None:
            if type(index) is not int:
                raise TypeError("Index must be an integer")
            if index < -len(self) or index > len(self):
                raise IndexError("Index out of range.")

        if cards:
            cards = _flatten_nested_collections(cards)
            for card in cards:
                if type(card) not in [Card, Joker]:
                    raise TypeError("Only Card objects can be provided")
            if index is None:
                self.cards.extend(cards)
            else:
                self.cards[index:index] = cards

    def remove(self, *cards_or_indexes):
        """
        Remove one or more cards from the deck. Cards or indices can be specified as arguments, or a list/tuple of Card objects/indices can be provided.

        Args:
            *cards_or_indexes: Variable number of Card objects, indices, lists/tuples of Card objects, and/or lists/tuples of indices to be removed.

        Note:
            - Indexes are treated before Card objects.
            - If both a card and its index are provided, it will not generate an error.
            - When specifying multiple indexes, they will be deleted correctly, no matter the order they are given
            (e.g., if you put index 1 and 2, it will first delete the 2nd index and then the 1st, avoiding the deletion of the wrong element).
            - Identical indexes will only be deleted once.
            - Identical cards will be deleted multiple times only if there are multiple corresponding cards.

        Raises:
            IndexError: If an index provided is out of range.
            ValueError: If a Card is not found in the deck or if an invalid argument is provided.
        """
        if cards_or_indexes:
            cards_or_indexes = _flatten_nested_collections(cards_or_indexes)
            indexes_to_remove = []
            cards_to_remove = []
            for elt in cards_or_indexes:
                if type(elt) is int:
                    # Handle integers (indexes)
                    elt = len(self) + elt if elt < 0 else elt
                    if 0 <= elt < len(self):
                        if elt not in indexes_to_remove:
                            indexes_to_remove.append(elt)
                    else:
                        raise IndexError("Index out of range.")
                elif type(elt) in [Card, Joker]:
                    # Handle Card objects
                    if elt in self.cards:
                        cards_to_remove.append(elt)
                    else:
                        raise ValueError("Card not found in the deck.")
                else:
                    raise TypeError("Invalid argument. Use integers or Card objects.")

            # Sort indexes in reverse order for safe removal
            indexes_to_remove.sort(reverse=True)
            for i in indexes_to_remove:
                if 0 <= i < len(self):
                    self.cards.pop(i)

            # Remove cards from the deck
            for c in cards_to_remove:
                if c in self.cards:
                    self.cards.remove(c)

    def shuffle(self):
        """
        Shuffle the deck of cards randomly using the `random.shuffle` function.
        """
        shuffle(self.cards)

    def sort_by_suit(self):
        """
        Sort the deck of cards by suit.
        """
        self.cards = sorted(self.cards, key=lambda card: (card.suit, card.rank if card.rank != 1 else card.get_ace_value()))

    def sort_by_rank(self):
        """
        Sort the deck of cards by rank.
        """
        self.cards = sorted(self.cards, key=lambda card: (card.rank if card.rank != 1 else card.get_ace_value(), card.suit))

    def index(self, *cards):
        """
        Retrieve and return the indexes of Card objects in the deck that match the specified cards.

        Args:
            *cards: Variable number of Card objects to search for in the deck.

        Returns:
            int or tuple of ints: An integer representing the index of the specified Card if only one Card is found,
            or a tuple of integers representing the indexes of matching Cards in the deck if multiple Cards are found.

        Raises:
            ValueError: If any of the provided cards are not found in the deck.
        """
        if not cards:
            return
        card_indexes = []
        cards = _flatten_nested_collections(cards)
        for card in cards:
            if type(card) not in [Card, Joker]:
                raise TypeError("Only Card objects can be provided")
            elif card in self.cards:
                card_indexes.append(self.cards.index(card))
            else:
                raise ValueError("Card not found in the deck.")
        return card_indexes[0] if len(card_indexes) == 1 else tuple(card_indexes)

    def get(self, *indexes):
        """
        Retrieve and return Card objects from the deck at the specified indexes.

        Args:
            *indexes: Variable number of integers, and/or lists/tuples of integers representing the indexes of the cards to be retrieved.

        Returns:
            Card or Deck of Cards: A single Card object if only one index is provided, or a Deck of unique Card objects
            at the specified indexes in the deck if multiple indexes are provided. If no indexes are provided, it returns
            the last card in the deck.

        Raises:
            IndexError: If any of the provided indexes are out of range.
            TypeError: If an invalid argument is provided.
        """
        if len(indexes) == 0:
            return self.cards[-1]
        retrieved_cards = []
        indexes = _flatten_nested_collections(indexes)
        for item in indexes:
            if type(item) is int:
                item = len(self) + item if item < 0 else item
                if 0 <= item < len(self):
                    retrieved_cards.append(self.cards[item])
                else:
                    raise IndexError("Index out of range.")
            else:
                raise TypeError("Invalid argument. Use integers, lists of integers, or tuples of integers.")

        return retrieved_cards[0] if len(retrieved_cards) == 1 else Deck(retrieved_cards)

    def get_random(self, amount=1):
        """
        Get a specified number of random cards from the deck.

        Args:
            amount (int, optional): The number of random cards to retrieve from the deck. Default is 1.

        Returns:
            Card or Deck of Cards: A single Card object if the amount is 1, or a deck of unique Card objects
            if the amount is higher.
        """
        possible_cards = self.cards[:]
        cards = []
        while amount > 0 and len(possible_cards) > 0:
            card = choice(possible_cards)
            possible_cards.remove(card)
            cards.append(card)
            amount -= 1
        return cards[0] if len(cards) == 1 else Deck(cards)

    def draw(self, *indexes):
        """
        Remove and return Card objects from the deck at the specified indexes.

        Args:
            *indexes: Variable number of integers representing the indexes of the cards to be removed. If no indexes are provided,
            it returns the last card in the deck.

        Returns:
            Card or Deck of Cards: A Card object representing the removed card if only one card is removed,
            or a deck of Card objects representing the removed cards if multiple cards are removed.

        Raises:
            IndexError: If any of the provided indexes are out of range.
        """
        retrieved_cards = self.get(*indexes)
        self.remove(*indexes)
        return retrieved_cards if type(retrieved_cards) is Card else Deck(retrieved_cards)

    def draw_random(self, amount=1):
        """
        Remove and return a specified number of random cards from the deck.

        Args:
            amount (int, optional): The number of random cards to draw from the deck. Default is 1.

        Returns:
            Card or Deck of Cards: A single randomly selected Card object if the amount is 1, or a Deck of unique
            randomly selected Card objects if the amount is higher.
        """
        cards = []
        while amount > 0 and len(self) > 0:
            card = self.draw(randint(0, len(self) - 1))
            cards.append(card)
            amount -= 1
        return cards[0] if len(cards) == 1 else Deck(cards)

    def copy(self):
        """
        Create a deep copy of the deck, including copying all cards.

        Returns:
            Deck: A new deck with copies of all cards from the original deck.
        """
        return Deck([card.copy() for card in self.cards])

    def select(self, rank=None, suit=None, color=None, face_card=None):
        """
        Select cards from the deck based on specified criteria.

        Args:
            rank (int, str, list, tuple, optional): Card ranks to include. Prefix with "!" or use negative integers to exclude ranks.
            suit (int, str, list, tuple, optional): Card suits to include. Prefix with "!" or use negative integers to exclude suits.
            color (bool, str, optional): Card color to include.
            face_card (bool, optional): Whether to include face cards.

        Returns:
            Deck of Card: Selected cards from the deck based on the provided criteria.
        """
        selected_cards = self.cards

        # Helper function to separate exclusions from inclusions
        def separate_exclusions(criteria):
            excl = []
            for ind in range(len(criteria) - 1, -1, -1):
                if type(criteria[ind]) is str and criteria[ind].startswith("!"):
                    # Remove the exclamation mark and add to exclusions
                    excl.append(criteria.pop(ind)[1:])
                elif type(criteria[ind]) is int and criteria[ind] < 0:
                    # Convert rank/suit index back to positive and add to exclusions
                    excl.append(-criteria.pop(ind))
            return excl

        # Filter by rank
        if rank is not None:
            rank = [rank] if type(rank) in (int, str) else list(rank)
            exclusions = separate_exclusions(rank)

            def get_test_card():
                if r in Card.get_ranks() or (type(r) is int and 1 <= r <= 13):
                    return Card(r, 1)
                if r == "Joker" or r == 0:
                    return Joker(False)
                if type(r) not in [int, str]:
                    raise TypeError("Incorrect rank type provided")
                raise ValueError("Invalid rank values provided")

            # Apply exclusions
            for r in exclusions:
                selected_cards = [card for card in selected_cards if not card.same_rank(get_test_card())]

            # Apply inclusions
            filtered_cards = []
            for r in rank:
                filtered_cards += [card for card in selected_cards if card.same_rank(get_test_card())]
            selected_cards = filtered_cards

            del filtered_cards, r, get_test_card, exclusions, rank

        # Filter by suit
        if suit is not None:
            suit = [suit] if type(suit) in (int, str) else list(suit)
            exclusions = separate_exclusions(suit)

            def get_test_card():
                if s in Card.get_suits() or (type(s) is int and 1 <= s <= 4):
                    return Card(1, s)
                if s == 0:
                    return Joker(False)
                if type(s) not in [int, str]:
                    raise TypeError("Incorrect suit type provided")
                raise ValueError("Invalid suit values provided")

            # Apply exclusions
            for s in exclusions:
                selected_cards = [card for card in selected_cards if not card.same_suit(get_test_card())]

            # Apply inclusions
            filtered_cards = []
            for s in suit:
                filtered_cards += [card for card in selected_cards if card.same_suit(get_test_card())]
            selected_cards = filtered_cards

            del filtered_cards, s, get_test_card, exclusions, suit

        # Filter by color
        if color is not None:
            if type(color) is str and color not in ["Black", "Red"]:
                raise ValueError("Invalid color values provided")
            elif type(color) not in [bool, str]:
                raise TypeError("Incorrect color type")
            selected_cards = [card for card in selected_cards if card.has_color(color)]

        # Filter by face_card
        if face_card is not None:
            if type(face_card) is not bool:
                raise TypeError("Incorrect color type")
            selected_cards = [card for card in selected_cards if card.face_card == face_card]

        return Deck(selected_cards)


def _flatten_nested_collections(collection):
    """
    Flatten a nested collection (list or tuple) into a single list.

    Args:
        collection (list or tuple): The nested collection to be flattened.

    Returns:
        list: A flat list containing all the elements from the nested collection.
    """
    return [item for arg in collection for item in (arg if type(arg) in (list, tuple) else
                                                    [arg] if type(arg) is not Deck else
                                                    arg.cards)]
