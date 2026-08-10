

# Import the random module to allow us to select the word list and password at random.
import random

# Create lists of 100 6-letter, 7-letter and 8-letter words that are similar enough to work well for this game.
easy_words = ['AETHER', 'ANSWER', 'AROUND', 'BADDER', 'BALDER', 'BANDED', 'BANKER', 'BANTER', 'BARBER', 'BASHED', 'BASHER', 'BATHED', 'BATHER', 'BATTER', 'BEAKER', 'BEANED', 'BEATER', 'BEAVER', 'BEDDER', 'BEFORE', 'BEHIND', 'BENDER', 'BETTER', 'BOLDER', 'BOLTER', 'BOMBER', 'BORDER', 'BOTHER', 'BOTTLE', 'BOWLER', 'BRACER', 'BRIDGE', 'BROKEN', 'BUMPER', 'BUSIER', 'BUTTON', 'CANDLE', 'CHARGE', 'CIRCLE', 'CLOSED', 'CORNER', 'CREATE', 'CREDIT', 'DANGER', 'DEADER', 'DEAFER', 'DEARER', 'DELVER', 'DEMAND', 'DENSER', 'DESIGN', 'DETECT', 'DEVICE', 'DEXTER', 'DOUBLE', 'DRIVER', 'ENERGY', 'ENGINE', 'ESCAPE', 'EVADER', 'EXPERT', 'FATHER', 'FENDER', 'GARDEN', 'GATHER', 'HEARER', 'HEIFER', 'HERDER', 'JESTER', 'JUDDER', 'KIDDER', 'LEADER', 'LEAPER', 'LEASER', 'LEVIED', 'LEVIER', 'LEVIES', 'MADDER', 'MEANER', 'MENDER', 'MINDER', 'NEATER', 'NEEDED', 'NESTED', 'PESTER', 'PEWTER', 'PONDER', 'REALER', 'REAVER', 'RENDER', 'SEEDER', 'SETTER', 'TEMPER', 'TENDER', 'TENNER', 'VENDER', 'WEDDER', 'WEEDED', 'WELDER', 'YONDER']
medium_words = ['ACTIONS', 'ANOTHER', 'ARRIVAL', 'BALANCE', 'BANDAGE', 'BANKERS', 'BANTERS', 'BARBERS', 'BARRING', 'BATTERS', 'BEACONS', 'BEATERS', 'BEATING', 'BEAVERS', 'BETTERS', 'BLAMING', 'BLUSTER', 'BOMBERS', 'BONKERS', 'BORDERS', 'BOTHERS', 'BOWLERS', 'BRACERS', 'BRIDGES', 'BROKERS', 'BURPING', 'BUTTONS', 'CANDLES', 'CHARGED', 'CHARGER', 'CIRCLED', 'CLOSERS', 'CLOSURE', 'CONNING', 'CREATED', 'CREATOR', 'CREDITS', 'DANGERS', 'DECADES', 'DEFENDS', 'DELIVER', 'DEMANDS', 'DENIERS', 'DEPUTES', 'DESIGNS', 'DETECTS', 'DEVICES', 'DISCORD', 'DRIVERS', 'DROVERS', 'DUSTERS', 'ELOPING', 'EXPERTS', 'FARMERS', 'FATHERS', 'GARDENS', 'GATHERS', 'HEARERS', 'HEIFERS', 'HERDERS', 'JESTERS', 'JUDDERS', 'KIDDERS', 'LEADERS', 'LEAPERS', 'LEASERS', 'LOOKERS', 'MARKERS', 'MEANDER', 'MENDERS', 'MILKERS', 'MINDERS', 'NESTERS', 'NETHERS', 'PESTERS', 'PEWTERS', 'PLANERS', 'PLANETS', 'POCKETS', 'PONDERS', 'READERS', 'REAVERS', 'RENDERS', 'RENTERS', 'RINGING', 'SEEDERS', 'SEEDING', 'SETTERS', 'SETTING', 'TANKERS', 'TARGETS', 'TENDERS', 'TENNERS', 'VENDERS', 'WEEDERS', 'WELDERS', 'WELDING', 'WINDOWS', 'WORKERS', 'WRITERS']
hard_words = ['ABRIDGED', 'ABSOLVED', 'ABSORBED', 'ACCEPTED', 'ACQUIRED', 'ADMITTED', 'ADVANCED', 'ADVERTED', 'AFFECTED', 'ALLOTTED', 'ANALYZED', 'ANIMATED', 'ANNULLED', 'APPROVED', 'ARRANGED', 'ASSIGNED', 'ASSUMING', 'ATTACHED', 'ATTEMPTS', 'ATTRACTS', 'AVERTING', 'BALANCED', 'BANTERED', 'BOTHERED', 'BUILDING', 'BUTTONED', 'CANDIDLY', 'CARRIAGE', 'CHARGING', 'COMBINED', 'CONCLAVE', 'CONCLUDE', 'CONSIDER', 'CONTAINS', 'CONTENTS', 'CONTROLS', 'CREATION', 'CREATIVE', 'CREDITED', 'CREDITOR', 'DECIDING', 'DECLINED', 'DECREASE', 'DEEPENED', 'DESIGNED', 'DETECTED', 'DETECTOR', 'DETESTED', 'DETRACTS', 'DISABLED', 'DISCOVER', 'EFFECTED', 'EMERGING', 'ENRICHED', 'ENROLLED', 'ERUPTING', 'EXCITING', 'EXCLUDES', 'EXECUTED', 'EXPANDED', 'EXPANDER', 'EXPELLED', 'EXPLORED', 'EXPLORER', 'EXTENDED', 'FINALISE', 'FINISHED', 'FINISHER', 'FLUSHING', 'HAPPENED', 'HEARINGS', 'HELPINGS', 'IDENTITY', 'IMAGINED', 'IMPROVED', 'INCLUDED', 'INCREASE', 'INFORMED', 'INVITING', 'INVOLVED', 'LEARNING', 'LEAVINGS', 'LOADINGS', 'LOCATING', 'PLACATED', 'RECEIVED', 'RELATION', 'RENDERED', 'REPORTED', 'REPORTER', 'RESEARCH', 'RESOLVED', 'RETRACTS', 'SHAVINGS', 'SIMPLIFY', 'SIMULATE', 'STEALING', 'STEELING', 'UNSOLVED', 'VALIDATE']


print("Welcome to Password Guesser Deluxe! \nBY ARNAV PAYAL (10729432)")

difficulty = input('Choose your diffuclty [E]asy, [M]edium, [H]ard:  ').upper()

# CHOOSE DIFF
if difficulty not in ["E", "M", "H"]:
    print("Invalid choice! Enter  E, M or H")

#DIFF DESCRIPTION
for char in difficulty:

    #EASY DIFF DESCRIPTION
    if difficulty == "E":
        diff = "Easy"
        gueses = 5 
        options = 7
        word_len = 6 
        sample = easy_words

#MED DIFF DESCRIPTION
    elif difficulty == "M":
        diff = "Medium"
        gueses = 4 
        options = 8
        word_len = 7
        sample = medium_words
        
        
#Hard DIFF DESCRIPTION
    elif difficulty == "H":
        diff = "Hard"
        gueses = 4
        options = 9
        word_len = 8
        sample = hard_words

    #DISPLAY INFO ABOUT THE DIFF
    print(f"\n{diff} diffuclty selected!")
    print(f"\nYou have {gueses} guesses to identify the password out of {options} words.")
    print(f"\nIn this difficulty, the game uses {word_len} letter words.")

    pick = random.sample(sample, options)
    

    answer = random.choice(pick)

    while True:
        #DISPLAY THE PASSWORD OPTIONS WITH THEIR  INDEX
        print("\nTHE PASSWORD IS ONE OF THESE WORDS: ")
        for i, word in enumerate(pick, 1):
                print(i, word)
    
        
        print(f"\nguesses remaining: {gueses}") 

        ask = input("ENTER YOUR CHOICE: ")

        #Check for valid input and valid range 
        if ask.isdigit():
            if int(ask) >= 1 and int(ask) <= options:
                guess_word = pick[int(ask) - 1]

            else:
                print("Pick a number from the options given!")

        else:
            print("INVALID INPUT!!")
        

        # Check if user won the game
        if guess_word == answer:
            print(f"YOU WON!!, THE WORD WAS {answer}")
            break

        #Continue the game, until user loses or wins
        else:
            print(f"YOU PICKED {guess_word}, GUESS INCORRECT!!")       
            count = 0
            for char in answer:
                if char in guess_word:
                    count += 1

            print(f"\n{count} / {word_len} letters correct")

            gueses = gueses - 1
            if gueses == 0:
                print(f"YOU LOST, THE WORD WAS {answer}")
                break



        

    

    

    
    






    









    





    
    





    


    


    




