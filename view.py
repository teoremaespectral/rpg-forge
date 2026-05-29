from controller import System

class Text:

    @staticmethod
    def roll_failure():
        '''Texto indicando os formatos corretos para as rolagens'''
        texto = "⚠️ *Erro na Rolagem de Dados!*\n\n"
        texto += "Certifique-se de que seu personagem está ativo e use um dos formatos:\n"
        texto += "• `[atributo] [dados]d[lados] [modificador]` (Ex: `v 2d6 +3`)\n"
        texto += "• `[atributo] [modificador]` (Ex: `v +3` para usar 1d20 padrão)\n"
        texto += "• `[atributo]` (Ex: `v` para rolar apenas 1d20 seco)"
        return texto

    @staticmethod
    def roll_success(character, stat, dice_number, dice_sides, modifier, rolls, total):
        '''Texto descrevendo a rolagem. Omite os dados e o modificador se forem o padrão'''
        # Nome visual do atributo com inicial maiúscula (ex: "v" -> "V")
        stat_display = stat.upper()
        
        texto = f"🎲 *Rolagem de {character.name}*\n"
        texto += f"📋 Teste de *{stat_display}*\n"
        texto += "—" * 15 + "\n"
        texto += f"🔢 Dados sorteados: `{rolls}`\n"
        
        # Só exibe a fórmula se ela não for o 1d20 padrão sem modificador
        if dice_number != 1 or dice_sides != 20 or modifier != 0:
            mod_sign = f"+{modifier}" if modifier >= 0 else f"{modifier}"
            texto += f"⚙️ Fórmula: `{dice_number}d{dice_sides}{mod_sign}`\n"
            
        texto += f"💥 *Total Final:* `{total}`"
        return texto

    @staticmethod
    def change_stat_failure():
        '''Texto indicando o formato correto para modificações de atributos'''
        texto = "⚠️ *Erro ao modificar atributo!*\n\n"
        texto += "O comando deve seguir o formato:\n"
        texto += "`[Atributo] [Modificação]`\n"
        texto += "Exemplos: `hp -5` ou `v +2`"
        return texto

    @staticmethod
    def change_stat_success(stat_string):
        '''Texto indicando que o atributo foi modificado com sucesso'''
        # Como o seu system.change_stat() já devolve o __str__() do próprio Stat modificado,
        # nós apenas envelopamos ele com um cabeçalho bonito!
        return f"✨ *Atributo Modificado!*\n\n{stat_string}"

    @staticmethod
    def change_character_failure(character_list):
        '''Texto expondo a lista de personagens do jogador'''
        texto = "⚠️ *Personagem não encontrado!*\n\n"
        texto += "Escolha um dos seus personagens disponíveis:\n"
        for char in character_list:
            texto += f"• `{char.name}`\n"
        return texto

    @staticmethod
    def change_character_success(new_character):
        '''Texto indicando que o personagem foi modificado com sucesso'''
        return f"👤 *Troca de Personagem!*\n\nAgora você está controlando: **{new_character.name}**"

    @staticmethod
    def character_info(character):
        '''Dá a ficha do personagem, indicando todos os seus atributos. Separa atributos primários de secundários'''
        texto = f"🌟 *FICHA DE PERSONAGEM: {character.name.upper()}*\n"
        texto += "—" * 20 + "\n\n"
        
        # Listas para separar os tipos de atributos dinamicamente
        primarios = []
        secundarios = []
        outros = []
        
        # Varre os status reais guardados no objeto Character
        for stat in character.stats.values():
            # Acessamos o setup dele pelo tipo do Enum para saber o papel (role)
            # Se você não salvou o papel no objeto, podemos deduzir pelo nome/tipo
            if stat.name.lower() in ["vigor", "destreza", "inteligencia", "carisma"]:
                primarios.append(str(stat))
            elif stat.name.lower() in ["vida", "sanidade"]:
                secundarios.append(str(stat))
            else:
                outros.append(str(stat))
                
        texto += "⚔️ *Atributos Primários:*\n"
        texto += "\n".join([f"• {s}" for s in primarios]) + "\n\n"
        
        texto += "❤️ *Atributos Secundários:*\n"
        texto += "\n".join([f"• {s}" for s in secundarios]) + "\n\n"
        
        if outros:
            # Para coisas como o "Caos"
            texto += "🌀 *Gerais:*\n"
            texto += "\n".join([f"• {s}" for s in outros]) + "\n"
            
        return texto


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
            return "❌ Jogador não registrado."
            
        if success:
            return Text.change_character_success(player.active)
        else:
            # Passa a lista de personagens que ele possui para ele escolher o certo
            return Text.change_character_failure(player.characters.values())

    def change_stat(self, user_id, result_string):
        '''Gera a resposta para alteração de atributos.'''
        # Se o dispatcher retornar False, result_string vira um booleano ou string vazia
        if not result_string:
            return Text.change_stat_failure()
            
        return Text.change_stat_success(result_string)

    def character_info(self, user_id):
        '''Gera o visual completo da ficha do personagem ativo.'''
        player = self.system.game.get(user_id)
        if not player or not player.active:
            return "❌ Você não possui nenhum personagem ativo no momento."
            
        return Text.character_info(player.active)