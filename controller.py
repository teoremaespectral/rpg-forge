from models import Stat, NonNegativeStat, LimitedStat, Character, Player
from setup import StatList, CharacterList, PlayerList
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

    def generate_stat(self, stat_name, value):
        '''Gera uma instância de Stat, NonNegativeStat ou LimitedStat com base na configuração definida em StatList. O tipo de estatística é determinado pela chave "type" no dicionário de configuração. Retorna a instância da estatística criada.'''
        stat = stat_name.config
        stat_type = stat.get("type", "standard")

        if stat_type == "standard":
            return Stat(stat_name.value, value, stat.get("icon", "❓"), stat.get("key", "?"))
        
        elif stat_type == "limited":
            return LimitedStat(stat_name.value, value, value, stat.get("icon", "❓"), stat.get("key", "?"))
        
        elif stat_type == "non_negative":
            return NonNegativeStat(stat_name.value, value, stat.get("icon", "❓"), stat.get("key", "?"))
        
    def generate_character(self, character_name):
        '''Gera uma instância de Character com base na configuração definida em CharacterList. O personagem é criado com um conjunto de estatísticas geradas a partir dos valores definidos no dicionário de configuração. Retorna a instância do personagem criado.'''
        character_config = character_name.config
        character = Character(character_name.value)

        for stat_name, stat_value in character_config.get("stats", {}).items():
            stat_instance = self.generate_stat(stat_name, stat_value)
            character.add_stat(stat_instance)

        return character
    
    def generate_player(self, player_name):
        '''Gera uma instância de Player com base na configuração definida em PlayerList. O player é criado com um personagem gerado a partir do nome do personagem definido no dicionário de configuração. Retorna a instância do player criado.'''
        player_config = player_name.config
        user_id, is_gm = player_config.get("user_id"), player_config.get("is_gm", False)
        player = Player(player_name.value, user_id, is_gm)
        for character in player_config.get("characters", []):
            character_instance = self.generate_character(character)
            player.add_character(character_instance)
        return player
    
    def create(self):
        '''Cria o sistema de RPG, gerando jogadores e personagens com base nas configurações definidas em PlayerList e CharacterList. Retorna um dicionário contendo os jogadores criados.'''
        system = {}
        for player_name in PlayerList:
            player_instance = self.generate_player(player_name)
            system[player_instance.user_id] = player_instance
        return system