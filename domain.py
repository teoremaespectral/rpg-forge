#Stats

class Stat:
    def __init__(self, name: str, value: int):
        self.name = name
        self.value = value

#Characters

class Character:
    def __init__(self, name: str, stats: list[Stat] = dict().copy()):
        self.name = name
        self.stats = stats

#Users

class User:
    def __init__(self, username: str, user_id: int, is_gm: bool = False, characters: list[Character] = dict().copy()):
        self.username = username
        self.user_id = user_id
        self.is_gm = is_gm
        self.characters = characters


#Board

class Board:
    def __init__(self, name: str, board_id: int, users: list[User] = dict().copy()):
        self.name = name
        self.board_id = board_id
        self.users = users