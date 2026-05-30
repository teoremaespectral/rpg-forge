from controller import System
from setup import StatList

class Text:

    @staticmethod
    def roll_failure():
        '''Texto indicando os formatos corretos para as rolagens'''
        text = "⚠️ *Erro na Rolagem de Dados!*\n\n"
        text += "Certifique-se de que seu personagem está ativo e use um dos formatos:\n"
        text += "• `[atributo] [dados]d[lados] [modificador]` (Ex: `v 2d6 +3`)\n"
        text += "• `[atributo] [modificador]` (Ex: `v +3` para usar 1d20 padrão)\n"
        text += "• `[atributo]` (Ex: `v` para rolar apenas 1d20 seco)"
        return text

    @staticmethod
    def roll_success(character, stat, dice_number, dice_sides, modifier, rolls, total):
        '''Texto descrevendo a rolagem. Omite os dados e o modificador se forem o padrão'''
        # Nome visual do atributo com inicial maiúscula (ex: "v" -> "V")
        stat_display = stat.upper()
        
        text = f"🎲 *Rolagem de {character.name}*\n"
        text += f"📋 Teste de *{stat_display}*\n"
        text += "—" * 15 + "\n"
        text += f"🔢 Dados sorteados: `{rolls}`\n"
        
        # Só exibe a fórmula se ela não for o 1d20 padrão sem modificador
        if dice_number != 1 or dice_sides != 20 or modifier != 0:
            mod_sign = f"+{modifier}" if modifier >= 0 else f"{modifier}"
            text += f"⚙️ Fórmula: `{dice_number}d{dice_sides}{mod_sign}`\n"
            
        text += f"💥 *Total Final:* `{total}`"
        return text

    @staticmethod
    def change_stat_failure():
        '''Texto indicando o formato correto para modificações de atributos'''
        text = "⚠️ *Erro ao modificar atributo!*\n\n"
        text += "O comando deve seguir o formato:\n"
        text += "`[Atributo] [Modificação]`\n"
        text += "Exemplos: `hp -5` ou `v +2`"
        return text

    @staticmethod
    def change_stat_success(stat_string):
        '''Texto indicando que o atributo foi modificado com sucesso'''
        # Como o seu system.change_stat() já devolve o __str__() do próprio Stat modificado,
        # nós apenas envelopamos ele com um cabeçalho bonito!
        return f"✨ *Atributo Modificado!*\n\n{stat_string}"

    @staticmethod
    def change_character_failure(character_list):
        '''Texto expondo a lista de personagens do jogador'''
        text = "⚠️ *Personagem não encontrado!*\n\n"
        text += "Escolha um dos seus personagens disponíveis:\n"
        for char in character_list:
            text += f"• `{char.name}`\n"
        return text

    @staticmethod
    def change_character_success(new_character):
        '''Texto indicando que o personagem foi modificado com sucesso'''
        return f"👤 *Troca de Personagem!*\n\nAgora você está controlando: **{new_character.name}**"

    @staticmethod
    def character_info(character):
        '''Dá a ficha do personagem, indicando todos os seus atributos. Separa atributos primários de secundários'''
        text = f"📜 Ficha de {character.name} \n"

        primary = []
        secondary = []
        general = []

        for stat in character.stats.values():
            try:
                stat_info = StatList(stat.name.lower())
                role = stat_info.config.get("role", "general")

            except ValueError:
                role = "general"

            if role == "primary":
                primary.append(stat)

            elif role == "secondary":
                secondary.append(stat)

            elif role == "general":
                general.append(stat)

        if primary:
            for stat in primary:
                text += str(stat) + "\n"
            text += "\n"

        if secondary:
            for stat in secondary:
                text += str(stat) + "\n"
            text += "\n"

        if general:
            for stat in general:
                text += str(stat) + "\n"

        return text
    
    @staticmethod
    def character_info_failure():
        '''Texto indicando que não há personagem ativo para se retornar informações'''
        text = "❌ Você não possui nenhum personagem ativo no momento."
        return text
    
    @staticmethod
    def not_player():
        '''Texto indicando que a solicitação partiu de um usuário que não é jogador'''
        text = "❌ Jogador não identificado."
        return text


class MessageFactory:
    '''Responsável por transformar dados puros do sistema em strings formatadas para o usuário.'''

    def __init__(self, system):
        self.system = system

    def roll_message(self, roll_data):
        '''Monta o visual do resultado dos dados'''
        if roll_data == False:
            return Text.roll_failure()
        
        character = roll_data["character"]
        stat = roll_data["stat"]
        dice_number = roll_data["dice_number"]
        dice_sides = roll_data["dice_sides"]
        modifier = roll_data["modifier"]
        rolls = roll_data["rolls"]
        total = roll_data["total"]
        
        return Text.roll_success(character, stat, dice_number, dice_sides, modifier, rolls, total)
    
    def change_character(self, user_id, success):
        '''Gera a resposta para a troca de personagem ativo.'''
        player = self.system.game.get(user_id)

        if not player:
            return Text.not_player()
            
        if success:
            return Text.change_character_success(player.active)
        else:
            return Text.change_character_failure(player.characters.values())

    def change_stat(self, result_string):
        '''Gera a resposta para alteração de atributos.'''
        if not result_string:
            return Text.change_stat_failure()
            
        return Text.change_stat_success(result_string)

    def character_info(self, user_id):
        '''Gera o visual completo da ficha do personagem ativo.'''
        player = self.system.game.get(user_id)
        if not player or not player.active:
            return Text.character_info_failure()
            
        return Text.character_info(player.active)