'''
File: palace.py
Project: Palace

Author: Talin Sharma @TalinTheDev
Date: 6/15/2022
License: Apache 2.0

Summary:
This file holds the functions required for the recreation of the Palace game.
'''

from colorama import init, Fore  # For colored text
from time import sleep  # For pausing the game
from random import shuffle, choice  # For shuffling the deck
from .helpers import clear, forEach  # For clearing the screen

init(autoreset=True)  # Initialize colorama

# Define Constants
RANKS = ["2", "3", "4", "5", "6", "7", "8",
         "9", "10", "Jack", "Queen", "King", "Ace"]
PLAYER_HAND = {"Face Down": [], "Face Up": [], "Hand": []}
CPU_HAND = {"Face Down": [], "Face Up": [], "Hand": []}
DECK = []
TOP_CARD = ""
TOP_CARD_COUNT = 1


def Palace():
    clear()
    print("Welcome to the recreation of the Palace Game made by @TalinTheDev!")
    print("Palace is a fun and easy game to play. Use te menu to start!")

    # List out menu options and prompt user to select one
    print("Menu:\n1. Start Game\n2. Exit\n3. How to Play\n")
    choice = input("Enter your choice: ")
    while choice not in ["1", "2", "3"]:
        choice = input("Invalid choice. Enter your choice: ")
    clear()
    sleep(0.5)
    match choice:
        case "1":
            print("Starting game...")
            sleep(0.5)
            clear()
            playGame()
        case "2":
            print("Exiting...")
            sleep(0.5)
            clear()
            exit()
        case "3":
            print("How to play:\n")
            howToPlay()

# Play the game


def playGame():
    # Define constants
    PLAYER_COUNT = 2
    DECK = makeDeck()
    TOP_CARD = DECK.pop()
    PLAYER_HAND, CPU_HAND = dealCards(DECK)  # Deal cards to players
    # Create a dictionary of indices for the RANKS
    indices = {i: e for e, i in enumerate(RANKS)}
    # Sort the CPU's hand by rank
    CPU_HAND["Hand"].sort(key=lambda e: indices[e], reverse=True)

    CPU_HAND = createFaceUpHand()
    PLAYER_HAND = askFaceUpHand()

    FIRST_Player = choice(["Player", "CPU"])  # Randomly select who goes first
    print("Dealing Cards...")
    sleep(0.5)
    clear()
    showHands()

    print(FIRST_Player + " goes first!")
    clear()
    while win() == False:
        if FIRST_Player == "Player":
            # Player's turn
            showHands()
            playerPlay()
        elif FIRST_Player == "CPU":
            # CPU's turn
            showHands()
            cpuPlay()
    exit()


# Make a deck of cards
def makeDeck():
    for rank in RANKS:
        for i in range(1, 5):
            DECK.append(rank)

    # Shuffle the deck
    shuffle(DECK)
    return DECK

# Deal cards to players


def dealCards(DECK):
    for i in range(1, 4):
        PLAYER_HAND["Face Down"].append(DECK.pop())
        CPU_HAND["Face Down"].append(DECK.pop())

    for i in range(1, 7):
        PLAYER_HAND["Hand"].append(DECK.pop())
        CPU_HAND["Hand"].append(DECK.pop())

    return PLAYER_HAND, CPU_HAND


# Show the player's hand
def showHand(hand, handType):
    handOutput = ""
    for i in hand[handType]:
        handOutput += str(i) + ", "
    return handOutput

# Chooses cpu's face up cards based on order in RANKS


def createFaceUpHand():
    hand = CPU_HAND
    for i in range(1, 4):
        if(CPU_HAND["Hand"][:1] == "2" or CPU_HAND["Hand"][:1] == "10"):
            hand["Face Up"].append(CPU_HAND["Hand"].pop(i + 1))
        hand["Face Up"].append(CPU_HAND["Hand"].pop())

    return hand

# Ask the player to choose cards for their face up hand


def askFaceUpHand():
    hand = PLAYER_HAND
    print("These are the cards in your hand: ")
    for index, card in enumerate(PLAYER_HAND["Hand"]):
        print(str(index + 1) + ". " + card)
    faceUpHand = input("\nChoose three cards to put in your face up hand: ")
    faceUpHand = map(int, faceUpHand)
    x = 0
    for i in faceUpHand:
        hand["Face Up"].append(PLAYER_HAND["Hand"].pop(i-1-x))
        x += 1
    return hand

# CPU Play


def cpuPlay():
    print("CPU's Turn!")
    sleep(0.5)
    clear()

# Player Play


def playerPlay():
    print("Player's Turn!")
    sleep(0.5)
    clear()
    showHands()
    playedCard = input("Play a card: ")

# Check if someone won


def win():
    if len(PLAYER_HAND["Hand"]) == 0 and len(PLAYER_HAND["Face Up"]) == 0 and len(PLAYER_HAND["Face Down"]) == 0:
        clear()
        print("Player wins!\n\nGood Job!")
        return True
    elif len(CPU_HAND["Hand"]) == 0 and len(CPU_HAND["Face Up"]) == 0 and len(CPU_HAND["Face Down"]) == 0:
        clear()
        print("CPU wins!\n\nGood Try!")
        return True
    else:
        return False


def showHands():
    print("CPU's Face Up HAND: " + showHand(CPU_HAND, "Face Up"))
    print("Player's Face Up HAND: " + showHand(PLAYER_HAND, "Face Up"))
    print("Player's Hand: " + showHand(PLAYER_HAND, "Hand"))
    print("Current Top Card: " + TOP_CARD + " (" + str(TOP_CARD_COUNT) + ")")
