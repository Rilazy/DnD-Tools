#!/usr/bin/python3
import logging
from commands import *
import discord


logger = logging.getLogger("discord")
logger.setLevel(logging.DEBUG)
handler_file = logging.FileHandler(filename="main.full.log", encoding="utf-8", mode="w")
handler_file.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
handler_file.setLevel(logging.DEBUG)
handler_file_brief = logging.FileHandler(filename="main.log", encoding="utf-8", mode="w")
handler_file_brief.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
handler_file_brief.setLevel(logging.INFO)
logger.addHandler(handler_file)
logger.addHandler(handler_file_brief)
handler_console = logging.StreamHandler()
handler_console.setLevel(logging.ERROR)
logger.addHandler(handler_console)


async def help(message):
    logger.debug("Command \"Help\" run")
    text: str = message.content.strip().lower()
    text = text.replace("!help", "").strip()
    output = ""
    for command in commands:
        if text.find(command) != -1:
            output = output + commands[command][1]
    if output:
        await message.channel.send(output)
    else:
        await message.channel.send(f"Commands: {commandList}\nFor help with a "
                                   f"specific command, type \"!help [command]\", example:\n`!help help`")
    return


commands = {
    "test": (example_command, "Test: \n> "
                              "This command is a test command, as well as the template for additional commands in the "
                              "code. While you are free to call this command if you'd like, it's quite useless except "
                              "for those purposes.\n"),
    "help": (help, "Help:\n> "
                   "The \"Help\" command displays information about any commands named elsewhere in your message.\n"),
    "calculate health": (calculate_health, "Calculate Health:\n> "
                                           "Generates a random maximum hit point value for a new character. Formatting "
                                           "is:\n> `!calculate health [level] [hit die] [constitution modifier]`"),
    "roll": (roll, "Roll: \n> "
                   "Rolls dice using standard tabletop format, just type it exactly how you'd say it, for example:\n"
                   "`!roll 2d8+3` to roll 2d8 and add 3\n"
                   "Rolling with advantage coming soon!")
}


commandList = ""
for i in commands:
    commandList = commandList + i + ", "
commandList = commandList.strip(", ")


client = discord.Client()


@client.event
async def on_ready():
    logger.info('Logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    logger.info('Message from {0.author}: {0.content}'.format(message))
    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')
        # logger.debug(f"Sent message: \"Hello!\" to channel: \"{message.channel}\" in response to message: \"{
        # message.content}\" from user \"{message.author}\"")
        return
    print(message.content.strip().lower())
    for command in commands:
        if message.content.strip().lower().startswith(f"!{command}"):
            await commands[command][0](message)
            logger.info(f"Executing command \"{command}\" in response to message \"{message.content}\" from"
                        f" \"{message.author}\"")
            break


client.run('ODAyNzQ0Nzg3MzQ1NDczNTM2.YAzsVw.pi5G2gtTjeDjHhhw8rosHOjKUo0')

