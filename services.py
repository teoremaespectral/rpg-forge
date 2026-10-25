from domain import Stat, Character, User, Board
import setup

class Manager:
    def __init__(self):
        self.STATS = setup.STATS
        self.CHARACTERS = setup.CHARACTERS
        self.USERS = setup.USERS
        self.BOARD = setup.BOARD

        self.board = self.make_board()

    def make_board(self):
        characters = []
        for char_name, char_data in self.CHARACTERS.items():
            stats = []
            for stat_name, stat_value in char_data["stats"].items():
                stat_info = self.STATS[stat_name]
                stat = Stat(name=stat_info["name"], value=stat_value)
                stats.append(stat)
            character = Character(name=char_name, stats=stats)
            characters.append(character)

        users = []
        for user_name, user_data in self.USERS.items():
            user_characters = [char for char in characters if char.name in user_data["characters"]]
            user = User(username=user_name, user_id=user_data["user_id"], is_gm=user_data["is_gm"], characters=user_characters)
            users.append(user)

        board = Board(name=self.BOARD["name"], board_id=self.BOARD["board_id"], users=users)
        return board