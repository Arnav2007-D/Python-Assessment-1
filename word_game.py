# Name: Arnav Payal
# Student Number: 10729432

# This file is provided to you as a starting point for the "word_game.py" program of the Assignment
# of Programming Principles in Semester 2, 2026.  It provides you with suitable lists of words for the game.
# Use this file as the basis of your work.  You are not required to reference it.

# Import the random module to allow us to select the word list and password at random.
import random
# Create lists of 100 6-letter, 7-letter and 8-letter words that are similar enough to work well for this game.
easy_words = ['AETHER', 'ANSWER', 'AROUND', 'BADDER', 'BALDER', 'BANDED', 'BANKER', 'BANTER', 'BARBER', 'BASHED', 'BASHER', 'BATHED', 'BATHER', 'BATTER', 'BEAKER', 'BEANED', 'BEATER', 'BEAVER', 'BEDDER', 'BEFORE', 'BEHIND', 'BENDER', 'BETTER', 'BOLDER', 'BOLTER', 'BOMBER', 'BORDER', 'BOTHER', 'BOTTLE', 'BOWLER', 'BRACER', 'BRIDGE', 'BROKEN', 'BUMPER', 'BUSIER', 'BUTTON', 'CANDLE', 'CHARGE', 'CIRCLE', 'CLOSED', 'CORNER', 'CREATE', 'CREDIT', 'DANGER', 'DEADER', 'DEAFER', 'DEARER', 'DELVER', 'DEMAND', 'DENSER', 'DESIGN', 'DETECT', 'DEVICE', 'DEXTER', 'DOUBLE', 'DRIVER', 'ENERGY', 'ENGINE', 'ESCAPE', 'EVADER', 'EXPERT', 'FATHER', 'FENDER', 'GARDEN', 'GATHER', 'HEARER', 'HEIFER', 'HERDER', 'JESTER', 'JUDDER', 'KIDDER', 'LEADER', 'LEAPER', 'LEASER', 'LEVIED', 'LEVIER', 'LEVIES', 'MADDER', 'MEANER', 'MENDER', 'MINDER', 'NEATER', 'NEEDED', 'NESTED', 'PESTER', 'PEWTER', 'PONDER', 'REALER', 'REAVER', 'RENDER', 'SEEDER', 'SETTER', 'TEMPER', 'TENDER', 'TENNER', 'VENDER', 'WEDDER', 'WEEDED', 'WELDER', 'YONDER']


print("Welcome to Password Guesser Deluxe! \nBY ARNAV PAYAL (10729432)")

difficulty = input('Choose your diffuclty [E]asy, [M]edium, [H]ard:  ').upper()

if difficulty not in ["E", "M", "H"]:
    print("Invalid choice! Enter  E, M or H")

#DIFF DESCRIPTION

    #EASY DIFF DESCRIPTION
    if difficulty == "E":
        diff = "Easy"
        gueses = 5 
        word_len = 6 
        sample = easy_words
#MED DIFF DESCRIPTION
    elif difficulty == "M":
        diff = "Medium"
        gueses = 4 
        options = 8
        word_len = 7

