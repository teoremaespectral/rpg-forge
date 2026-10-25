#Stats

class Stat:
    def __init__(self, id: str, name: str, code: str, value: int):
        self.id = id
        self.name = name
        self.code = code
        self.value = value

#Characters

class Character:
    def __init__(self, name: str, stats: list[Stat] = None):
        self.name = name
        self.stats = stats if stats is not None else []

    def get_name(self) -> str:
        return self.name

    def get_stat_by_code(self, code: str) -> tuple[str, int]:
        for stat in self.stats:
            if stat.code == code:
                return stat.name, stat.value
        raise ValueError("Atributo não encontrado.")

#Users

class User:
    def __init__(self, username: str, user_id: int, is_gm: bool = False, characters: list[Character] = None):
        self.username = username
        self.user_id = user_id
        self.is_gm = is_gm
        self.characters = characters if characters is not None else []
        self.current_character = self.characters[0] if self.characters else None

    def get_current_character(self) -> Character:
        if not self.current_character:
            raise ValueError("Usuário não possui personagem atual.")
        return self.current_character


#Board

class Board:
    def __init__(self, name: str, board_id: int, users: list[User] = None):
        self.name = name
        self.board_id = board_id
        self.users = users if users is not None else []

    def get_user_by_id(self, user_id: int) -> User:
        for user in self.users:
            if user.user_id == user_id:
                return user
        raise ValueError("Usuário não encontrado.")