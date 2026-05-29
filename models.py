class Stat:
    '''Uma classe representando uma estatística do personagem, como força, agilidade, etc.'''
    def __init__(self, name, value, icon = "❓", key = "?"):
        '''Inicializa a estatística com um nome e um valor. O nome deve ser uma chave válida em s.STAT.'''
        self.name = name
        self.value = value
        self.icon = icon
        self.key = key

    def __str__(self):
        '''Retorna uma string formatada que exibe o ícone, o nome e o valor da estatística. Exemplo: "💪Vigor: 10".'''
        return f"{self.icon}{self.name}: {self.value}"
    
    def __iadd__(self, value):
        '''Permite adicionar um valor à estatística usando o operador de adição. Retorna o novo valor da estatística.'''
        self.value += value
        return self
    
class NonNegativeStat(Stat):
    '''Uma subclasse de Stat que garante que o valor da estatística nunca seja negativo. Se um valor negativo for atribuído, ele será ajustado para zero.'''

    def __init__(self, name, value, icon = "❓", key = "?"):
        '''Inicializa a estatística com um nome e um valor. O valor inicial é ajustado para não ser negativo.'''
        super().__init__(name, max(0, value), icon, key)
    
    def __iadd__(self, value):
        '''Permite adicionar um valor à estatística usando o operador de adição. Retorna o novo valor da estatística.'''
        self.value = max(0, self.value + value)
        return self
    
class LimitedStat(Stat):
    '''Uma subclasse de Stat que impõe um limite máximo ao valor da estatística. Se um valor que exceda o limite for atribuído, ele será ajustado para o limite.'''
    def __init__(self, name, value, limit, icon = "❓", key = "?"):
        '''Inicializa a estatística com um nome, um valor e um limite máximo. O valor inicial é ajustado para não exceder o limite.'''
        super().__init__(name, max(0, min(value, limit)), icon, key)
        self.limit = limit

    def __str__(self):
        '''Retorna uma string formatada que exibe o ícone, o nome, o valor atual e o limite da estatística. Exemplo: "💪Vigor: 10/20".'''
        return f"{self.icon}{self.name}: {self.value}/{self.limit}"

    def __iadd__(self, value):
        '''Permite adicionar um valor à estatística usando o operador de adição. Retorna o novo valor da estatística, garantindo que ele não exceda o limite.'''
        self.value = max(0, min(self.limit, self.value + value))
        return self

    def change_limit(self, new_limit):
        '''Altera o limite máximo da estatística. Se o valor atual exceder o novo limite, ele é ajustado para o novo limite. Retorna a string formatada atualizada.'''
        self.limit = new_limit
        self.value = min(self.value, self.limit)
        return self.__str__()
    
class Character:
    '''Uma classe representando um personagem, que possui um nome e um conjunto de estatísticas.'''
    def __init__(self, name):
        '''Inicializa o personagem com um nome e um dicionário vazio de estatísticas.'''
        self.name = name
        self.stats = {}
    
    def add_stat(self, stat):
        '''Adiciona uma estatística ao personagem. O parâmetro stat deve ser uma instância de Stat ou suas subclasses.'''
        self.stats[stat.key] = stat
    
    def get_stat(self, key):
        '''Retorna a estatística associada à chave fornecida. Se a chave não existir, retorna None.'''
        return self.stats.get(key)

    def __getitem__(self, key):
        '''Permite acessar o status direto usando colchetes: personagem["v"]'''
        return self.stats.get(key)
    
    def get_value(self, key, default=0):
        '''Retorna o valor numérico do status de forma segura.'''
        stat = self.stats.get(key)
        return stat.value if stat else default

class Player:
    '''Uma classe representando um jogador, que possui um nome, um ID de usuário, um dicionário de personagens e um personagem ativo.'''

    def __init__(self, name, user_id, is_gm=False):
        '''Inicializa o jogador com um nome, um ID de usuário e um dicionário vazio de personagens. O personagem ativo é inicialmente None.'''
        self.name = name
        self.user_id = user_id
        self.is_gm = is_gm
        self.characters = {}
        self.active_character = None

    @property
    def active(self):
        '''Retorna o personagem ativo do jogador.'''
        return self.active_character

    def add_character(self, character):
        '''Adiciona um personagem ao jogador. O parâmetro character deve ser uma instância de Character. Se for o primeiro personagem adicionado, ele se torna o personagem ativo.'''
        self.characters[character.name] = character
        if not self.active_character:
            self.active_character = character

    def select_character(self, character_name):
        '''Seleciona um personagem como o personagem ativo do jogador com base no nome fornecido. Retorna True se a seleção for bem-sucedida, ou False se o personagem não existir.'''
        if character_name in self.characters:
            self.active_character = self.characters[character_name]
            return True
        return False