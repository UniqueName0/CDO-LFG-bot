import discord
from discord.ext import commands, tasks
import sqlite3
import time

token = 'ODExOTQ5NDk5MDA5OTkwNjY3.YC5o5Q.pj4i1RKvHUkHZW57AfLnD4-GpCM'

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix="!", description=None, intents=intents)
bot.remove_command('help')

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)


@bot.command()
async def help(ctx):
    em = discord.Embed(title="help")
    em.add_field(name="commands", value='create game - !cg (game name) (difficulty) (server, make sure this is one word, like saying "us-east" instead of "us east") (waveskip, you could just say on or off) (password, if there is one)\n\nthe simpler command for creating a game - !scg (game name) (region) (password)')
    await ctx.send(embed=em)



@bot.command()
async def cg(ctx, gn, diff, server, ws, pw=None):
    if pw is None:
        pw = "no password"
    game_channel = discord.utils.get(ctx.guild.channels, name="games")
    em = discord.Embed()
    em.add_field(name=f"{ctx.author.name}'s game", value=f"name:{gn}\ndifficulty:{diff}\nregion:{server}\nwave skip:{ws}\npassword:{pw}")
    await ctx.channel.send(embed=em)


@bot.command()
async def scg(ctx, gn, server, pw=None):
    if pw is None:
        pw = "no password"
    game_channel = discord.utils.get(ctx.guild.channels, name="games")
    em = discord.Embed()
    em.add_field(name=f"{ctx.author.name}'s game", value=f"name:{gn}\nregion:{server}\npassword:{pw}")
    await ctx.channel.send(embed=em)

bot.run(token)
