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

class System:
    '''Classe que mantém e adiministra o sistema de RPG'''

    def __init__(self):
        if self.is_new():
            self.game = SystemFactory().create()
            self.save()
        else:
            self.game = self.load()
    
    def is_new(self):
        pass

    def load(self):
        pass

    def save(self):
        pass

    def change_current_character(self, user_id, character_name):
        '''Altera o personagem ativo do jogador identificado por user_id para o personagem com o nome character_name. Retorna True se a alteração for bem-sucedida, ou False se o jogador ou o personagem não existirem.'''
        player = self.game.get(user_id)
        if not player:
            return False
        
        change = player.select_character(character_name)
        self.save()
        return change

    def change_stat(self, user_id, stat_key, modifier):
        '''Altera o valor de uma estatística específica para o personagem ativo do jogador identificado por user_id. O valor da estatística é modificado pelo valor do modifier fornecido. Retorna a string formatada atualizada da estatística após a modificação.'''
        player = self.game.get(user_id)
        if not player:
            return ""
        
        active_character = player.active
        if not active_character:
            return ""
        
        stat = active_character.stats.get(stat_key)
        if not stat:
            return ""
        
        stat += modifier
        self.save()
        return stat.__str__()

class Dispatcher:
    '''Classe responsável por capturar comandos e interações dos jogadores e direcioná-los para as funções apropriadas no sistema.'''

    def __init__(self, system):
        self.system = system

    def roll(self, user_id, message):
        '''Recebe uma mensagem do tipo [atributo] [número de dados]d[número de lados] [modificador opcional] e realiza uma rolagem de dados para o personagem ativo do jogador identificado por user_id. Retorna um dicionário contendo os resultados da rolagem, ou False se a rolagem não puder ser realizada.'''
        # Exemplo de mensagem: "v 2d6 +3"
        # Exemplos abreviados: "v +3" ou "v 2d6" ou mesmo "v"

        parts = message.split()
        player = self.system.game.get(user_id)
        if not player or not player.active:
            return False

        try:
            stat_key = parts[0]
            dice_number, dice_sides, modifier = 1, 20, 0

            if len(parts) > 1:
                dice_part = parts[1]
                if 'd' in dice_part:
                    dice_number, dice_sides = map(int, dice_part.split('d'))
                else:
                    modifier = int(dice_part)

            if len(parts) > 2:
                modifier = int(parts[2])

            return RollEngine().roll(player.active, stat_key, dice_number, dice_sides, modifier)
        
        except (ValueError, IndexError):
            return False

    def change_current_character(self, user_id, message):
        '''Recebe uma mensagem com um nome de personagem. Retorna o sucesso da operação'''
        return self.system.change_current_character(user_id, message)
    
    def change_stat(self, user_id, message):
        '''Recebe uma mensagem composta de [Atributo] [Modificação]. Retorna o sucesso da operação'''
        try:
            stat_key, modifier = message.split()
            modifier = int(modifier)
            return self.system.change_stat(user_id, stat_key, modifier)
        
        except (ValueError, IndexError):
            return False

