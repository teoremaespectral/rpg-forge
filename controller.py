from models import Stat, NonNegativeStat, LimitedStat, Character, Player
#from setup import 
from random import randint

class RollEngine:
    '''Uma classe responsável por realizar rolagens de dados para um personagem com base em uma estatística específica.'''

    def roll(self, character, stat_key, dice_number = 1, dice_sides = 20, modifier = 0):
        stat = character.stats.get(stat_key)
        if not stat:
            return False
                
        rolls = [randint(1, dice_sides) for _ in range(dice_number)]
        total = stat.value + sum(rolls) + modifier

        return {
            "rolls": rolls,
            "total": total
        }

class SystemFactory:
    '''Uma classe responsável por criar sistemas de RPG a partir de dados fornecidos por setup.py.'''

    pass