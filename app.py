from fastapi import FastAPI  # for creating the web app
from pydantic import BaseModel  # pydandtic = data validation and settings management lib using type annotations
from random import choice
import uvicorn  # runs the web app using Uvicorn server

app = FastAPI()

races = [
    "Human",
    "Elf",
    "Dwarf",
    "Halfling",
    "Half-Elf",
    "Half-Orc",
]
classes = [
    "Fighter",
    "Wizard",
    "Cleric",
    "Rogue",
    "Ranger",
    "Paladin",
    "Bard",
    "Druid",
    "Monk",
    "Barbarian",
]


class Dice:
    def __init__(self, sides):
        self.sides = sides

    def roll(self, times=1):
        from random import randint

        # underscore often used as a variable name when the variable value isn't actually used in the code. 
        # e.g. its an unimportant, throwaway variable
        rolls = []
        for _ in range(times):
            roll = randint(1, self.sides)
            rolls.append(roll)

        return sum(rolls)

class Hero(BaseModel):
    name: str
    race: str
    character_class: str
    strength: int
    dexterity: int
    constitution: int
    intelligence: int
    wisdom: int
    charisma: int

def generate_random_stats():
    dice = Dice(6)
    stats = {}
    for stat in [
        "Strength",
        "Dexterity",
        "Constitution",
        "Intelligence",
        "Wisdom",
        "Charisma",
    ]:
        stats[stat] = dice.roll(3, times=6)
    return stats


# create hero endpoint
@app.post("/create_hero/")
async def create_hero(hero: Hero):
    return hero


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
