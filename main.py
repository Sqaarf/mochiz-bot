import random
import requests
import os
from dotenv import load_dotenv

import discord
from discord import app_commands
from discord.ext import commands

load_dotenv()

# Setup the bot with a custom prefix
# Default prefix is 'm.'

bot = commands.Bot(command_prefix='m.', intents=discord.Intents.all())

@bot.event
async def on_ready():
    print("Bot is Up and Ready !")
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} command(s)")
    except Exception as e:
        print(e)



# List of answers in 8ball command
eightball_answers = ["Myes", "Nope" ,"100% sure", "Kinda", "Not even in your wildest dream", "idk google it ?"]
# List of possible moves in Rock, Paper & Scissors
rps_choices = ["Rock", "Paper", "Scissors"]

@bot.tree.command(name="answer")
async def answer(interaction: discord.Interaction):
    '''
    Send a random answer to a question
    '''
    choice = random.choice(eightball_answers)
    await interaction.response.send_message(choice)

#------------------------------------RANDOM PICS----------------------------------------------------------------------------------

@bot.command()
async def dog(interaction: discord.Interaction):
    '''
    Send a random image of a dog using some-random-api.ml
    '''
    r = requests.get('https://some-random-api.ml/animal/dog')
    await interaction.response.send_message(r.json()["image"])

@bot.command()
async def cat(interaction: discord.Interaction):
    '''
    Send a random image of a cat using some-random-api.ml
    '''
    r = requests.get('https://some-random-api.ml/animal/cat')
    await interaction.response.send_message(r.json()["image"])

@bot.command()
async def raccoon(interaction: discord.Interaction):
    '''
    Send a random image of a raccoon using some-random-api.ml
    '''
    r = requests.get('https://some-random-api.ml/animal/raccoon')
    await interaction.response.send_message(r.json()["image"])

@bot.command()
async def fox(interaction: discord.Interaction):
    '''
    Send a random image of a fox using some-random-api.ml
    '''
    r = requests.get('https://some-random-api.ml/animal/fox')
    await interaction.response.send_message(r.json()["image"])

@bot.command()
async def birb(interaction: discord.Interaction):
    '''
    Send a random image of a bird using some-random-api.ml
    '''
    r = requests.get('https://some-random-api.ml/animal/birb')
    await interaction.response.send_message(r.json()["image"])

@bot.tree.command(name="repeat")
async def repeat(interaction: discord.Interaction, word: str, coeff: int):
    '''
    Send a given word a number given of times

        Parameters:
            args[0] (str): The word you want to be repeated
            args[1] (str): The number of times you want thhe word to be repeated
    '''
    response = " ".join([word for x in range(coeff)])
    await interaction.response.send_message(response)

@bot.tree.command(name="rps")
async def rps(interaction: discord.Interaction, choice: str):
    '''
    A game of Rock, Paper & Scissors

        Parameters:
            args[0] (str): The player of choice (Rock|Paper|Scissors)
    '''
    rps_choice = ""
    rps_choice = random.choice(rps_choices)
    if choice.lower() == rps_choice.lower():
        response = f"A DRAW ? WTF CHEATER >:("
    elif choice.lower() == "rock":
        if rps_choice == "Scissors":
            response = f"{rps_choice} ! Wait wha- YOU STUPID ASS MF I LOST"
        else:
            response = f"{rps_choice} ! Hahaha get rekt loseeer :p"
    elif choice.lower() == "scissors":
       if rps_choice == "Paper":
           response = f"{rps_choice} ! Wait wha- YOU STUPID ASS MF I LOST"
       else:
           response = f"{rps_choice} ! Hahaha get rekt loseeer :p"
    elif choice.lower() == "paper":
       if rps_choice == "Rock":
           response = f"{rps_choice} ! Wait wha- YOU STUPID ASS MF I LOST"
       else:
           response = f"{rps_choice} ! Hahaha get rekt loseeer :p"
    else:
        response = f"Stop spitting nonsense it's rock, paper or scissors... MMMMMMMM"
    await interaction.response.send_message(response)

@bot.tree.command(name="calc")
async def calc(interaction: discord.Interaction, expression: str):
    '''
    Send the result of a simple mathematical calculus expression

        Parameters:
            args[0] (str): Pythonic calculus expression 
    '''
    await interaction.response.send_message(str(eval(expression)))

@bot.tree.command(name="echo")
async def echo(interaction: discord.Interaction, text: str):
    '''
    Rewrite a sentence/word
        
        Parameters:
            args (list<str>): The word/sentence you want to send
    '''
    await interaction.response.send_message(text)

@bot.tree.command(name="hey")
async def hey(interaction: discord.Interaction):
    '''
    Send a simple introduction
    '''
    await interaction.response.send_message("Hey motherfuckaaaz i'm Mochiz destroyer of worlds youuuu knooow")

bot.run(os.environ.get("DISCORD_TOKEN"))
