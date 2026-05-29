from enum import Enum

class StatList(Enum):
    """Guarda os nomes das estatísticas e suas respectivas configurações."""
    VIGOR = "vigor"
    DESTREZA = "destreza"
    INTELIGENCIA = "inteligencia"
    CARISMA = "carisma"
    VIDA = "vida"
    SANIDADE = "sanidade"
    CAOS = "caos"

    @property
    def config(self):
        """Retorna o dicionário de configurações específico deste status."""
        MAP_CONFIG = {
            StatList.VIGOR:        {"icon": "💪", "key": "v",  "type": "standard",     "role": "primary"},
            StatList.DESTREZA:     {"icon": "🎻", "key": "d",  "type": "standard",     "role": "primary"},
            StatList.INTELIGENCIA: {"icon": "🧩", "key": "i",  "type": "standard",     "role": "primary"},
            StatList.CARISMA:      {"icon": "🧲", "key": "c",  "type": "standard",     "role": "primary"},
            StatList.VIDA:         {"icon": "❤️", "key": "hp", "type": "limited",      "role": "secondary"},
            StatList.SANIDADE:     {"icon": "🧠", "key": "st", "type": "limited",      "role": "secondary"},
            StatList.CAOS:         {"icon": "🌀", "key": "ch", "type": "non_negative", "role": "general"}
        }
        return MAP_CONFIG[self]

class CharacterList(Enum):
    '''Guarda os nomes dos personagens pré-definidos e suas respectivas configurações.'''
    NICK = "Nick"
    ADALBERTO = "Adalberto Gil"
    TELLARIM = "Tellarim Rugleffar"
    MIU = "Miu"
    VIOLE = "Viole"
    KAI = "Kai Pirinha"
    JOSUE = "Josué"

    @property
    def config(self):
        '''Retorna o dicionário de configurações específico deste personagem.'''
        MAP_CONFIG = {
            CharacterList.NICK: {
                "stats": {
                    StatList.VIGOR: 5,
                    StatList.DESTREZA: 5,
                    StatList.INTELIGENCIA: 1,
                    StatList.CARISMA: 2,
                    StatList.VIDA: 10,
                    StatList.SANIDADE: 2,
                },
            },
            CharacterList.ADALBERTO: {
                "stats": {
                    StatList.VIGOR: 3,
                    StatList.DESTREZA: 0,
                    StatList.INTELIGENCIA: 4,
                    StatList.CARISMA: 5,
                    StatList.VIDA: 6,
                    StatList.SANIDADE: 8,
                },
            },
            CharacterList.TELLARIM: {
                "stats": {
                    StatList.VIGOR: 5,
                    StatList.DESTREZA: 3,
                    StatList.INTELIGENCIA: 4,
                    StatList.CARISMA: 3,
                    StatList.VIDA: 10,
                    StatList.SANIDADE: 8,
                },
            },
            CharacterList.MIU: {
                "stats": {
                    StatList.VIGOR: 2,
                    StatList.DESTREZA: 5,
                    StatList.INTELIGENCIA: 4,
                    StatList.CARISMA: 1,
                    StatList.VIDA: 4,
                    StatList.SANIDADE: 8,
                },
            },
            CharacterList.VIOLE: {
                "stats": {
                    StatList.VIGOR: 4,
                    StatList.DESTREZA: 5,
                    StatList.INTELIGENCIA: 2,
                    StatList.CARISMA: 1,
                    StatList.VIDA: 8,
                    StatList.SANIDADE: 4,
                },
            },
            CharacterList.KAI: {
                "stats": {
                    StatList.VIGOR: 1,
                    StatList.DESTREZA: 3,
                    StatList.INTELIGENCIA: 5,
                    StatList.CARISMA: 3,
                    StatList.VIDA: 2,
                    StatList.SANIDADE: 10,
                },
            },
            CharacterList.JOSUE: {
                "stats": {
                    StatList.VIGOR: 3,
                    StatList.DESTREZA: 5,
                    StatList.INTELIGENCIA: 3,
                    StatList.CARISMA: 1,
                    StatList.VIDA: 6,
                    StatList.SANIDADE: 6,
                },
            },
        }
        return MAP_CONFIG[self]

class PlayerList(Enum):
    '''Guarda os nomes dos jogadores pré-definidos e suas respectivas configurações.'''
    GABRIEL = "Gabriel"
    ADRYEL = "Adryel"
    HOLANDA = "Holanda"
    VITORIA = "Vitoria"
    QUEL = "Quel"
    GLEYDSON = "Gleydson"
    HIGOR = "Higor"
    THAIS = "Thais"

    @property
    def config(self):
        '''Retorna o dicionário de configurações específico deste jogador.'''
        MAP_CONFIG = {
            PlayerList.GABRIEL: {"user_id": 123456789, "is_gm": True},
            PlayerList.ADRYEL: {"user_id": 987654321, "is_gm": False, "characters": [CharacterList.NICK]},
            PlayerList.HOLANDA: {"user_id": 111111111, "is_gm": False, "characters": [CharacterList.ADALBERTO]},
            PlayerList.VITORIA: {"user_id": 222222222, "is_gm": False, "characters": [CharacterList.TELLARIM]},
            PlayerList.QUEL: {"user_id": 333333333, "is_gm": False, "characters": [CharacterList.MIU]},
            PlayerList.GLEYDSON: {"user_id": 444444444, "is_gm": False, "characters": [CharacterList.VIOLE]},
            PlayerList.HIGOR: {"user_id": 555555555, "is_gm": False, "characters": [CharacterList.KAI]},
            PlayerList.THAIS: {"user_id": 666666666, "is_gm": False, "characters": [CharacterList.JOSUE]},
        }
        return MAP_CONFIG[self]