import random
import requests
import os
from dotenv import load_dotenv

import discord
from discord.ext import commands

load_dotenv()

# Setup the bot with a custom prefix
# Default prefix is 'm.'
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='m.', intents=intents)

# List of answers in 8ball command
eightball_answers = ["Myes", "Nope" ,"100% sure", "Kinda", "Not even in your wildest dream", "idk google it ?"]
# List of possible moves in Rock, Paper & Scissors
rps_choices = ["Rock", "Paper", "Scissors"]

@bot.command()
async def answer(ctx):
    '''
    Send a random answer to a question
    '''
    choice = random.choice(eightball_answers)
    await ctx.send(choice)

#------------------------------------RANDOM PICS----------------------------------------------------------------------------------

@bot.command()
async def dog(ctx):
    '''
    Send a random image of a dog using some-random-api.ml
    '''
    r = requests.get('https://some-random-api.ml/animal/dog')
    await ctx.send(r.json()["image"])

@bot.command()
async def cat(ctx):
    '''
    Send a random image of a cat using some-random-api.ml
    '''
    r = requests.get('https://some-random-api.ml/animal/cat')
    await ctx.send(r.json()["image"])

@bot.command()
async def raccoon(ctx):
    '''
    Send a random image of a raccoon using some-random-api.ml
    '''
    r = requests.get('https://some-random-api.ml/animal/raccoon')
    await ctx.send(r.json()["image"])

@bot.command()
async def fox(ctx):
    '''
    Send a random image of a fox using some-random-api.ml
    '''
    r = requests.get('https://some-random-api.ml/animal/fox')
    await ctx.send(r.json()["image"])

@bot.command()
async def birb(ctx):
    '''
    Send a random image of a bird using some-random-api.ml
    '''
    r = requests.get('https://some-random-api.ml/animal/birb')
    await ctx.send(r.json()["image"])

@bot.command()
async def repeat(ctx, *args):
    '''
    Send a given word a number given of times

        Parameters:
            args[0] (str): The word you want to be repeated
            args[1] (str): The number of times you want thhe word to be repeated
    '''
    word = args[0]
    coeff = int(args[1])
    response = " ".join([word for x in range(coeff)])
    await ctx.send(response)

@bot.command()
async def rps(ctx, *args):
    '''
    A game of Rock, Paper & Scissors

        Parameters:
            args[0] (str): The player of choice (Rock|Paper|Scissors)
    '''
    rps_choice = ""
    rps_choice = random.choice(rps_choices)
    if args[0].lower() == rps_choice.lower():
        response = f"A DRAW ? WTF CHEATER >:("
    elif args[0].lower() == "rock":
        if rps_choice == "Scissors":
            response = f"{rps_choice} ! Wait wha- YOU STUPID ASS MF I LOST"
        else:
            response = f"{rps_choice} ! Hahaha get rekt loseeer :p"
    elif args[0].lower() == "scissors":
       if rps_choice == "Paper":
           response = f"{rps_choice} ! Wait wha- YOU STUPID ASS MF I LOST"
       else:
           response = f"{rps_choice} ! Hahaha get rekt loseeer :p"
    elif args[0].lower() == "paper":
       if rps_choice == "Rock":
           response = f"{rps_choice} ! Wait wha- YOU STUPID ASS MF I LOST"
       else:
           response = f"{rps_choice} ! Hahaha get rekt loseeer :p"
    else:
        response = f"Stop spitting nonsense it's rock, paper or scissors... MMMMMMMM"
    await ctx.send(response)

@bot.command()
async def calc(ctx, *args):
    '''
    Send the result of a simple mathematical calculus expression

        Parameters:
            args[0] (str): Pythonic calculus expression 
    '''
    op = str(args[0])
    await ctx.send(str(eval(op)))

@bot.command()
async def echo(ctx, *args):
    '''
    Rewrite a sentence/word
        
        Parameters:
            args (list<str>): The word/sentence you want to send
    '''
    await ctx.send(" ".join(args))

@bot.command()
async def hey(ctx):
    '''
    Send a simple introduction
    '''
    await ctx.send("Hey motherfuckaaaz i'm Mochiz destroyer of worlds youuuu knooow")

bot.run(os.environ.get("DISCORD_TOKEN"))
