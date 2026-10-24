STATS = {
    "vig": {
        "name": "Vigor",
        "type": "PlainStat",
        "code": "v",
    },
    "dex": {
        "name": "Destreza",
        "type": "PlainStat",
        "code": "d",
    },
    "int": {
        "name": "Inteligência",
        "type": "PlainStat",
        "code": "i",
    },
    "cha": {
        "name": "Carisma",
        "type": "PlainStat",
        "code": "c",
    },
    "hp": {
        "name": "Pontos de Vida",
        "type": "LimitedStat",
        "code": "hp",
    },
    "san": {
        "name": "Sanidade",
        "type": "LimitedStat",
        "code": "san",
    },
}

CHARACTERS = {
    "Nick": {
        "stats": {
            "vig": 5,
            "dex": 5,
            "int": 1,
            "cha": 2,
            "hp": 10,
            "san": 2,
        },
    },

    "Adalberto": {
        "stats": {
            "vig": 3,
            "dex": 0,
            "int": 4,
            "cha": 5,
            "hp": 6,
            "san": 8,
        },
    },

    "Tellarim": {
        "stats": {
            "vig": 5,
            "dex": 3,
            "int": 4,
            "cha": 3,
            "hp": 10,
            "san": 8,
        },
    },

    "Miu": {
        "stats": {
            "vig": 2,
            "dex": 5,
            "int": 4,
            "cha": 1,
            "hp": 4,
            "san": 8,
        },
    },

    "Viole": {
        "stats": {
            "vig": 4,
            "dex": 5,
            "int": 2,
            "cha": 1,
            "hp": 8,
            "san": 4,
        },
    },

    "Kai": {
        "stats": {
            "vig": 1,
            "dex": 3,
            "int": 5,
            "cha": 3,
            "hp": 2,
            "san": 10,
        },
    },

    "Josué": {
        "stats": {
            "vig": 3,
            "dex": 5,
            "int": 3,
            "cha": 1,
            "hp": 6,
            "san": 6,
        },
    },
}

PLAYERS = {
    "Adryel": {
        "user_id": 1,
        "is_gm": False,
        "characters": ["Nick",],
    },

    "Holanda": {
        "user_id": 2,
        "is_gm": False,
        "characters": ["Adalberto",],
    },

    "Vitória": {
        "user_id": 3,
        "is_gm": False,
        "characters": ["Tellarim",],
    },

    "Quel": {
        "user_id": 4,
        "is_gm": False,
        "characters": ["Miu",],
    },

    "Gleydson": {
        "user_id": 5,
        "is_gm": False,
        "characters": ["Viole",],
    },

    "Higor": {
        "user_id": 6,
        "is_gm": False,
        "characters": ["Kai",],
    },

    "Thaís": {
        "user_id": 7,
        "is_gm": False,
        "characters": ["Josué",],
    },

    "Gabriel": {
        "user_id": 8,
        "is_gm": True,
        "characters": [],
    },
}

BOARD = {
    "name": "Taverna",
    "board_id": 1,
    "users": ["Adryel", "Holanda", "Vitória", "Quel", "Gleydson", "Higor", "Thaís", "Gabriel"],
}