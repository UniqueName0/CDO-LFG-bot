import discord
from discord.ext import commands, tasks
import sqlite3
import time

token = "token"

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix="+", description=None, intents=intents)
bot.remove_command('help')

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)


@bot.command()
async def help(ctx):
    em = discord.Embed(title="help")
    em.add_field(name="commands", value=f'Create Game - (Game Name), (Difficulty), (Region), (Waveskip On/Off), (Password) [Optional]\n Do {bot.command_prefix}cg to use this command, followed by this information\n\n\nShort Create Game - scg (Game Name), (Region), (Password)\nDo {bot.command_prefix}cg to use this command\n\n\n{bot.command_prefix}prefix (new prefix), only usable by people with the Holy Guardian role')
    await ctx.send(embed=em)



@bot.command()
async def cg(ctx, gn, diff, server, ws, pw=None):
    if pw is None:
        pw = "no password"
    em = discord.Embed()
    em.add_field(name=f"{ctx.author.name}'s game", value=f"name:{gn}\ndifficulty:{diff}\nregion:{server}\nwave skip:{ws}\npassword:{pw}")
    if diff == "Hard" or diff == "hard":
    	dest_channel = discord.utils.get(ctx.guild.channels, name="hard")
    	await dest_channel.send(embed=em, delete_after=300)
    elif diff == "Hell" or diff == "hell":
    	dest_channel = discord.utils.get(ctx.guild.channels, name="hell")
    	await dest_channel.send(embed=em, delete_after=300)
    elif diff == "Dark" or diff == "dark":
    	dest_channel = discord.utils.get(ctx.guild.channels, name="dark")
    	await dest_channel.send(embed=em, delete_after=300)
    elif diff == "Insane" or diff == "insane":
    	dest_channel = discord.utils.get(ctx.guild.channels, name="insane")
    	await dest_channel.send(embed=em, delete_after=300)
    elif diff == "Impossible" or diff == "impossible":
    	dest_channel = discord.utils.get(ctx.guild.channels, name="impossible")
    	await dest_channel.send(embed=em, delete_after=300)
    elif diff == "Infinity" or diff == "infinity":
    	dest_channel = discord.utils.get(ctx.guild.channels, name="infinity")
    	await dest_channel.send(embed=em, delete_after=300)


@bot.command()
async def scg(ctx, gn, server, pw=None):
    if pw is None:
        pw = "no password"
    em = discord.Embed()
    em.add_field(name=f"{ctx.author.name}'s game", value=f"name:{gn}\nregion:{server}\npassword:{pw}")
    await ctx.channel.send(embed=em)
    if diff == "Hard" or diff == "hard":
    	dest_channel = discord.utils.get(ctx.guild.channels, name="hard")
    	await dest_channel.send(embed=em, delete_after=300)
    elif diff == "Hell" or diff == "hell":
    	dest_channel = discord.utils.get(ctx.guild.channels, name="hell")
    	await dest_channel.send(embed=em, delete_after=300)
    elif diff == "Dark" or diff == "dark":
    	dest_channel = discord.utils.get(ctx.guild.channels, name="dark")
    	await dest_channel.send(embed=em, delete_after=300)
    elif diff == "Insane" or diff == "insane":
    	dest_channel = discord.utils.get(ctx.guild.channels, name="insane")
    	await dest_channel.send(embed=em, delete_after=300)
    elif diff == "Impossible" or diff == "impossible":
    	dest_channel = discord.utils.get(ctx.guild.channels, name="impossible")
    	await dest_channel.send(embed=em, delete_after=300)
    elif diff == "Infinity" or diff == "infinity":
    	dest_channel = discord.utils.get(ctx.guild.channels, name="infinity")
    	await dest_channel.send(embed=em, delete_after=300)

@bot.command()
async def prefix(ctx, arg):
    if "Holy Guardian" in author.roles or "Guardian" in author.roles:
        bot.command_prefix = arg
        ctx.channel.send(f"the command prefix is now {arg}")
  
bot.run(token)
