import logging
import random
import re


__all__ = ["calculate_health", "roll", "example_command"]


logger = logging.getLogger("discord")
logger.setLevel(logging.DEBUG)
handler_file = logging.FileHandler(filename="commands.full.log", encoding="utf-8", mode="w")
handler_file.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
handler_file.setLevel(logging.DEBUG)
handler_file_brief = logging.FileHandler(filename="commands.log", encoding="utf-8", mode="w")
handler_file_brief.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
handler_file_brief.setLevel(logging.INFO)
logger.addHandler(handler_file)
logger.addHandler(handler_file_brief)
handler_console = logging.StreamHandler()
handler_console.setLevel(logging.ERROR)
logger.addHandler(handler_console)


async def calculate_health(message):
    text: str = message.content.lower().strip().replace("!calculate health", "").strip()
    level, die, con = map(int, text.split())
    health = die + (con * level) + random.randint((((die // 2) + 1) * (level - 1)), (die * (level - 1)))
    await message.channel.send(str(health))
    return


async def example_command(message):
    logger.debug("Command \"Test\" run")
    await message.channel.send("Response")
    return


async def roll(message):
    logger.debug("Command \"Roll\" run")
    text: str = message.content.replace(" ", "").lower().replace("!roll", "")
    text = text + "+0"
    if text.count("+") > 1:
        text = text.replace("+0", "")
    print(text)
    dice, die, bonus = map(int, re.split("[+dD]", text))
    natroll = random.randint(dice, dice * die)
    output = f"You rolled {natroll + bonus} ({natroll} + {bonus})"
    if dice == 1 and die == 20 and natroll == 20:
        output = f"You rolled a natural 20! (Total {natroll + bonus})"
    await message.channel.send(output)
    logger.debug(f"Rolled {natroll + bonus} ({natroll} + {bonus}) when rolling {dice}d{die}+{bonus}")
    return


