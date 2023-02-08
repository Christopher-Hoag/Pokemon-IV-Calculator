"""This code was written in Python v. 2.7.3 and is intended to work on such. If program is run under Python 2.6 or Python 3.3 it will not work."""

from PokemonBaseStats import *
from math import floor

print "This program will attempt to calculate a pokemon's IVs based on your input."
print

Pokemon = raw_input("Please enter a pokemon's name: ")

def PokemonChecker(Pokemon): #Checks if Pokemon's name is valid.
    global pokemon
    if Pokemon != '' and Pokemon != Pokemon.isdigit():
        PokemonList = open("PokemonBaseStats.py")
        for line in PokemonList:
            Number = line.find(' ')
            PokemonList = open("PokemonBaseStats.py")
            if Pokemon == line[:Number]:
                pokemon = Pokemon
                return
            else:
                print "Invalid Pokemon. Please try again."
                print "Also note that if there is a space or - in a pokemon's name it is replaced with a _"
                Pokemon = raw_input("Please enter a pokemon's name: ")
    else:
        pokemon = Pokemon
        return


pokemon = pokemon.lower()
pokemon = pokemon[0].upper() + pokemon[1:]

Level = raw_input("Please enter " + pokemon + "'s level: ")

def LevelChecker(Level): #Checks if Pokemon's level is valid.
    global level
    if Level.isdigit():
        level = int(Level)
        if level >= 0 and Level <= 100:
            return
    else:
        print "Pokemon level should be a number between 0 and 100."
        Level = raw_input("Please enter " + pokemon + "'s level: ")
        LevelChecker(Level)

LevelChecker(Level)

Nature = raw_input("Please enter " + pokemon + "'s nature: ")
    
def NatureCalculator(Nature): #Creates a dictionary called 'nature' depending on Nature inputted. Also checks for valid Nature.
    if Nature == '':
        Nature = raw_input("Invalid nature. Please try again: ")
        NatureCalculator(Nature)
    else:
        Nature = Nature.lower()
        Nature = Nature[0].upper() + Nature[1:]
        global nature
        if Nature == "Lonely":
            nature = {"Attack":1.10, "Defense":0.9, "Sp. Attack":1, "Sp. Defense":1, "Speed":1}
        elif Nature == "Adamant":
            nature = {"Attack":1.10, "Defense":1, "Sp. Attack":0.9, "Sp. Defense":1, "Speed":1}
        elif Nature == "Naughty":
            nature = {"Attack":1.10, "Defense":1, "Sp. Attack":1, "Sp. Defense":0.9, "Speed":1}
        elif Nature == "Brave":
            nature = {"Attack":1.10, "Defense":1, "Sp. Attack":1, "Sp. Defense":1, "Speed":0.9}
        elif Nature == "Bold":
            nature = {"Attack":0.9, "Defense":1.1, "Sp. Attack":1, "Sp. Defense":1, "Speed":1}
        elif Nature == "Impish":
            nature = {"Attack":1, "Defense":1.1, "Sp. Attack":0.9, "Sp. Defense":1, "Speed":1}
        elif Nature == "Lax":
            nature={"Attack":1, "Defense":1.1, "Sp. Attack":1, "Sp. Defense":0.9, "Speed":1}
        elif Nature == "Relaxed":
            nature = {"Attack":1, "Defense":1.1, "Sp. Attack":1, "Sp. Defense":1, "Speed":0.9}
        elif Nature == "Modest":
            nature = {"Attack":0.9, "Defense":1, "Sp. Attack":1.1, "Sp. Defense":1, "Speed":1}
        elif Nature == "Mild":
            nature = {"Attack":1, "Defense":0.9, "Sp. Attack":1.1, "Sp. Defense":1, "Speed":1}
        elif Nature == "Rash":
            nature = {"Attack":1, "Defense":1, "Sp. Attack":1.1, "Sp. Defense":0.9, "Speed":1}
        elif Nature == "Quiet":
            nature = {"Attack":1, "Defense":1, "Sp. Attack":1.1, "Sp. Defense":1, "Speed":0.9}
        elif Nature == "Calm":
            nature = {"Attack":0.9, "Defense":1, "Sp. Attack":1, "Sp. Defense":1.1, "Speed":1}
        elif Nature == "Gentle":
            nature = {"Attack":1, "Defense":0.9, "Sp. Attack":1, "Sp. Defense":1.1, "Speed":1}
        elif Nature == "Careful":
            nature = {"Attack":1, "Defense":1, "Sp. Attack":0.9, "Sp. Defense":1.1, "Speed":1}
        elif Nature == "Sassy":
            nature = {"Attack":1, "Defense":1, "Sp. Attack":1, "Sp. Defense":1.1, "Speed":0.9}
        elif Nature == "Timid":
            nature = {"Attack":0.9, "Defense":1, "Sp. Attack":1, "Sp. Defense":1, "Speed":1.1}
        elif Nature == "Hasty":
            nature = {"Attack":1, "Defense":0.9, "Sp. Attack":1, "Sp. Defense":1, "Speed":1.1}
        elif Nature == "Jolly":
            nature = {"Attack":1, "Defense":1, "Sp. Attack":0.9, "Sp. Defense":1, "Speed":1.1}
        elif Nature == "Naive":
            nature = {"Attack":1, "Defense":1, "Sp. Attack":1, "Sp. Defense":0.9, "Speed":1.1}
        elif Nature == "Bashful":
            nature = {"Attack":1, "Defense":1, "Sp. Attack":1, "Sp. Defense":1, "Speed":1}
        elif Nature == "Docile":
            nature = {"Attack":1, "Defense":1, "Sp. Attack":1, "Sp. Defense":1, "Speed":1}
        elif Nature == "Hardy":
            nature = {"Attack":1, "Defense":1, "Sp. Attack":1, "Sp. Defense":1, "Speed":1}
        elif Nature == "Quirky":
            nature = {"Attack":1, "Defense":1, "Sp. Attack":1, "Sp. Defense":1, "Speed":1}
        elif Nature == "Serious":
            nature = {"Attack":1, "Defense":1, "Sp. Attack":1, "Sp. Defense":1, "Speed":1}
        else:
            Nature = raw_input("Invalid nature. Please try again: ")
            NatureCalculator(Nature)
        
NatureCalculator(Nature)

HP = input("Please enter " + pokemon + "'s HP: ")
Attack = input("Please enter " + pokemon + "'s Attack: ")
Defense = input("Please enter " + pokemon + "'s Defense: ")
SpAttack = input("Please enter " + pokemon + "'s Sp. Attack: ")
SpDefense = input("Please enter " + pokemon + "'s Sp. Defense: ")
Speed = input("Please enter " + pokemon + "'s Speed: ")

HPEV = input("Please enter " + pokemon + "'s HP EVs: ")
AttackEV = input("Please enter " + pokemon + "'s Attack EVs: ")
DefenseEV = input("Please enter " + pokemon + "'s Defense EVs: ")
SpAttackEV = input("Please enter " + pokemon + "'s Sp. Attack EVs: ")
SpDefenseEV = input("Please enter " + pokemon + "'s Sp. Defense EVs: ")
SpeedEV = input("Please enter " + pokemon + "'s Speed EVs: ")

HPIV = -(((HPEV+8*eval(pokemon)["HP"]+400)*level-400*HP+4000)/(4*Level))
AttackIV = floor((-8*eval(pokemon)["Attack"]*level*nature["Attack"]-AttackEV*level*nature["Attack"]-2000*nature["Attack"]+400*Attack)/(4*level*nature["Attack"]))
DefenseIV = floor((-8*eval(pokemon)["Defense"]*level*nature["Defense"]-DefenseEV*level*nature["Defense"]-2000*nature["Defense"]+400*Defense)/(4*level*nature["Defense"]))
SpAttackIV = floor((-8*eval(pokemon)["Sp. Attack"]*level*nature["Sp. Attack"]-SpAttackEV*level*nature["Sp. Attack"]-2000*nature["Sp. Attack"]+400*SpAttack)/(4*level*nature["Sp. Attack"]))
SpDefenseIV = floor((-8*eval(pokemon)["Sp. Defense"]*level*nature["Sp. Defense"]-SpDefenseEV*level*nature["Sp. Defense"]-2000*nature["Sp. Defense"]+400*SpDefense)/(4*level*nature["Sp. Defense"]))
SpeedIV = floor((-8*eval(pokemon)["Speed"]*level*nature["Speed"]-SpeedEV*level*nature["Speed"]-2000*nature["Speed"]+400*Speed)/(4*level*nature["Speed"]))

print
print "Your {} has:".format(pokemon)
print "{} HP IVs".format(HPIV)
print "{} Attack IVs".format(AttackIV)
print "{} Defense IVs".format(DefenseIV)
print "{} Sp. Attack IVs".format(SpAttackIV)
print "{} Sp. Defense IVs".format(SpDefenseIV)
print "{} Speed IVs".format(SpeedIV)
print
print "These are just approximations; the higher the level of the pokemon the more accurate these are."
raw_input('Press enter to exit')
