import setup as s

class Stat:
    '''Uma classe representando uma estatística do personagem, como força, agilidade, etc.'''
    def __init__(self, name, value, icon = "❓", key = "?"):
        '''Inicializa a estatística com um nome e um valor. O nome deve ser uma chave válida em s.STAT.'''
        self.name = name
        self.value = value
        self.icon = icon
        self.key = key

    @property
    def display(self):
        '''Retorna uma string formatada que exibe o ícone, o nome e o valor da estatística. Exemplo: "💪Vigor: 10".'''
        return f"{self.icon}{self.name}: {self.value}"
    
    def change(self, value):
        '''Adiciona um valor à estatística e retorna a string formatada atualizada. O valor pode ser positivo ou negativo. Exemplo: se a estatística for "Vigor" com valor 10 e o valor passado for -2, a nova exibição será "💪Vigor: 8".'''
        self.value += value
        return self.display
    
class NonzeroStat(Stat):
    '''Uma subclasse de Stat que garante que o valor da estatística nunca seja negativo. Se um valor negativo for atribuído, ele será ajustado para zero.'''

    def __init__(self, name, value, icon = "❓", key = "?"):
        '''Inicializa a estatística com um nome e um valor. O valor inicial é ajustado para não ser negativo.'''
        super().__init__(name, max(0, value))
    
    def change(self, value):
        '''Adiciona um valor à estatística e garante que o valor resultante não seja negativo. Retorna a string formatada atualizada.'''
        self.value = max(0, self.value + value)
        return self.display
    
class LimitedStat(Stat):
    '''Uma subclasse de Stat que impõe um limite máximo ao valor da estatística. Se um valor que exceda o limite for atribuído, ele será ajustado para o limite.'''
    def __init__(self, name, value, limit, icon = "❓", key = "?"):
        '''Inicializa a estatística com um nome, um valor e um limite máximo. O valor inicial é ajustado para não exceder o limite.'''
        super().__init__(name, max(0, min(value, limit)), icon, key)
        self.limit = limit

    @property
    def display(self):
        '''Retorna uma string formatada que exibe o ícone, o nome, o valor atual e o limite da estatística. Exemplo: "💪Vigor: 10/20".'''
        return f"{self.icon}{self.name}: {self.value}/{self.limit}"

    def change(self, value):
        '''Adiciona um valor à estatística e garante que o valor resultante não exceda o limite. Retorna a string formatada atualizada.'''
        self.value = max(0, min(self.limit, self.value + value))
        return self.display
    
    def change_limit(self, new_limit):
        '''Altera o limite máximo da estatística e ajusta o valor atual se ele exceder o novo limite. Retorna a string formatada atualizada.'''
        self.limit = new_limit
        self.value = min(self.value, self.limit)
        return self.display