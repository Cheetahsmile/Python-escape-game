startingStory = "\n\n\nWhile walking to the airport, a woman saw that the old drink store was finally open\n\n"

monsterNames = [
    "Deadbeat Dad",
    "Daniel",
    "Mo",
    "Existential",
    "Bumba",
    "Evil pocket watch"
    # "Cruella",
    # "Jack Daniels",
    # "Koopa"
]

monsterQuestions = [
    "What cat looks like a rat",
    "What's the best color in the world",
    "Razia and Aqueelah and James and Perry and Makaela and Maggie are friends T/F",
    "What cat looks like a rat",
    "What's the best color in the world",
    "Razia and Aqueelah and James and Perry and Makaela and Maggie are friends T/F"
]

answers = [
    "Spynx",
    "Pink",
    "True",
    "Spynx",
    "Pink",
    "True"
]

# This function will display the starting story when I call it
def showStartingStory():
    print( startingStory )

showStartingStory() # call it

index = 0
for question in monsterQuestions:
    userAnswer = input( f"{monsterNames[ index ]} says {question}?: " )
    
    if userAnswer == answers[ index ]:
        print( "You win!!! Good luck on your journey" )
    else:
        print(  "You lose. Better luck next time" )
        break;
    index += 1

if index > 5:
    print( "Congrats!!! YOU'RE FREEE" )
else:
    print( "Damn you suck!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!" )
        

       