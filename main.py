import random
import requests

import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='m.')

eightball_answers = ["Myes", "Nope" ,"100% sure", "Kinda", "Not even in your wildest dream", "idk google it ?"]
rps_choices = ["Rock", "Paper", "Scissors"]

@bot.command()
async def answer(ctx):
    choice = random.choice(eightball_answers)
    await ctx.send(choice)

@bot.command()
async def dog(ctx):
    r = requests.get("https://dog.ceo/api/breeds/image/random")
    await ctx.send(r.json()["message"])

@bot.command()
async def cat(ctx):
    r = requests.get("https://api.thecatapi.com/v1/images/search")
    await ctx.send(r.json()[0]["url"])

@bot.command()
async def raccoon(ctx):
    r = requests.get('https://some-random-api.ml/animal/raccoon')
    await ctx.send(r.json()["image"])

@bot.command()
async def fox(ctx):
    r = requests.get('https://some-random-api.ml/animal/fox')
    await ctx.send(r.json()["image"])




@bot.command()
async def repeat(ctx, *args):
    word = args[0]
    coeff = int(args[1])
    response = " ".join([word for x in range(coeff)])
    await ctx.send(response)


@bot.command()
async def rps(ctx, *args):
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
        reponse = f"Stop spitting nonsense it's rock, paper or scissors... MMMMMMMM"
    await ctx.send(response)
@bot.command()
async def calc(ctx, *args):
    op = str(args[0])
    await ctx.send(str(eval(op)))

@bot.command()
async def echo(ctx, *args):
    await ctx.send(" ".join(args))

@bot.command()
async def hey(ctx):
    await ctx.send("Hey motherfuckaaaz :mochiz:")

@bot.command()
async def gay(ctx):
    await ctx.send('no u fucker, gay ass mf mmmmmmmmmmmmmmmmmm shut ur gay bitch ass ayoub shaped asshole')

bot.run('NTg0MTYxMjgyNTk3NDUzODY1.GeTcLs.-1XAbWLSRZqUBnxX7hZx-DITffVco65QAAleFE')
