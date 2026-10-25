from domain import Stat, Character, User, Board
from random import randint
import setup
import re

class RollEngine:

    @staticmethod
    def roll(num_dice: int = 1, num_sides: int = 20):
        if num_dice < 1:
            raise ValueError("A quantidade de dados deve ser positiva.")

        if num_sides < 1:
            raise ValueError("O número de lados deve ser positivo.")

        rolls = [randint(1, num_sides) for _ in range(num_dice)]
        return sum(rolls), rolls

    @staticmethod
    def parse_roll_command(command: str):
        regex = (
            r"^(?:(?P<qtd>\d+)d(?P<lados>\d+))?"
            r"(?P<modificador>[+-]\d+)?"
            r"(?:\s+(?P<stat_code>[a-zA-ZÀ-ÿ]+))?$"
        )

        match = re.match(regex, command.lower().strip())

        if not match:
            raise ValueError("Comando de rolagem inválido.")

        num_dice = int(match.group("qtd")) if match.group("qtd") else 1
        num_sides = int(match.group("lados")) if match.group("lados") else 20
        modifier = int(match.group("modificador")) if match.group("modificador") else 0
        stat_code = match.group("stat_code") if match.group("stat_code") else None

        return num_dice, num_sides, modifier, stat_code

class MessageMaker:
    @staticmethod
    def create_roll_message(roll_result: dict, character_name: str = None, stat_name: str = None, stat_value: int = 0):
        rolls = roll_result["rolls"]
        modifier = roll_result["modifier"]
        total = roll_result["total"]

        message = f"{character_name} fez um teste de {stat_name}!\n" if character_name and stat_name else ""
        message += f"Dados: {rolls}\n"
        message += f"{stat_name} de {character_name}: {stat_value}\n" if character_name and stat_name else ""
        message += f"Modificador: {modifier}\n" if modifier != 0 else ""
        message += f"Total: {total}\n"

        return message

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
            for stat_id, stat_value in char_data["stats"].items():
                stat_info = self.STATS[stat_id]
                stat = Stat(id=stat_id, name=stat_info["name"], code=stat_info["code"], value=stat_value)
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

    def execute_roll(self, command: str, user_id: int):
        num_dice, num_sides, modifier, stat_code = RollEngine.parse_roll_command(command)
        total, rolls = RollEngine.roll(num_dice, num_sides)

        user = self.board.get_user_by_id(user_id)
        character = user.get_current_character()
        character_name = character.get_name()
        stat_name, stat_value = character.get_stat_by_code(stat_code) if stat_code else (None, 0)

        roll_result = {
            "rolls": rolls,
            "modifier": modifier,
            "total": total + modifier + stat_value + stat_value
        }

        message = MessageMaker.create_roll_message(roll_result, character_name, stat_name, stat_value)

        return message