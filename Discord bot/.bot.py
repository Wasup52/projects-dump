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
token = "SECRET" # Your token here (https://discord.com/developers/applications)

bot = commands.Bot(command_prefix="!")

# with open(".Les zouaves_logs-id;697782644146044987.json") as f:
#     logs = json.load(f)


@bot.command(pass_context=True, aliases=["bgnls"])
async def bougnouls(ctx):
    channel = ctx.message.author.voice.channel
    if not channel:
        await ctx.send("You are not connected to a voice channel")
        return
    voice = get(bot.voice_clients, guild=ctx.guild)
    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()

    voice = get(bot.voice_clients, guild=ctx.guild)
    voice.play(discord.FFmpegPCMAudio("Discord bot\\bgnls.mp3"))
    voice.volume = 100
    voice.is_playing()

    duration = eyed3.load("bgnls.mp3").info.time_secs
    time.sleep(duration)

    if voice and voice.is_connected():
        await voice.disconnect()


@bot.command(pass_context=True)
async def tg(ctx):
    channel = ctx.message.author.voice.channel
    if not channel:
        await ctx.send("You are not connected to a voice channel")
        return
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


@bot.command(pass_context=True)
async def menfou(ctx):
    channel = ctx.message.author.voice.channel
    if not channel:
        await ctx.send("You are not connected to a voice channel")
        return
    voice = get(bot.voice_clients, guild=ctx.guild)
    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()

    voice = get(bot.voice_clients, guild=ctx.guild)
    voice.play(discord.FFmpegPCMAudio("Discord bot\\menfou.mp3"))
    voice.volume = 100
    voice.is_playing()

    duration = eyed3.load("menfou.mp3").info.time_secs
    time.sleep(duration + 0.5)

    if voice and voice.is_connected():
        await voice.disconnect()


@bot.command(pass_context=True)
async def allo(ctx):
    channel = ctx.message.author.voice.channel
    if not channel:
        await ctx.send("You are not connected to a voice channel")
        return
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


@bot.command(pass_context=True)
async def salope(ctx):
    channel = ctx.message.author.voice.channel
    if not channel:
        await ctx.send("You are not connected to a voice channel")
        return
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


@bot.command(pass_context=True)
async def miam(ctx):
    channel = ctx.message.author.voice.channel
    if not channel:
        await ctx.send("You are not connected to a voice channel")
        return
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


@bot.command(pass_context=True, aliases=["tgjean"])
async def jan(ctx):
    channel = ctx.message.author.voice.channel
    if not channel:
        await ctx.send("You are not connected to a voice channel")
        return
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


@bot.command(pass_context=True)
async def fuck(ctx):
    channel = ctx.message.author.voice.channel
    if not channel:
        await ctx.send("You are not connected to a voice channel")
        return
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


@bot.command(pass_context=True)
async def devise(ctx):
    channel = ctx.message.author.voice.channel
    if not channel:
        await ctx.send("You are not connected to a voice channel")
        return
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


@bot.command(pass_context=True)
async def arabes(ctx):
    channel = ctx.message.author.voice.channel
    if not channel:
        await ctx.send("You are not connected to a voice channel")
        return
    voice = get(bot.voice_clients, guild=ctx.guild)
    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()

    voice = get(bot.voice_clients, guild=ctx.guild)
    voice.play(discord.FFmpegPCMAudio("Discord bot\\plein-le-cul-des-arabes.mp3"))
    voice.volume = 75
    voice.is_playing()

    duration = eyed3.load("plein-le-cul-des-arabes.mp3").info.time_secs
    time.sleep(duration)

    if voice and voice.is_connected():
        await voice.disconnect()


@bot.command(pass_context=True)
async def cercueil(ctx):
    channel = ctx.message.author.voice.channel
    if not channel:
        await ctx.send("You are not connected to a voice channel")
        return
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


@bot.command(pass_context=True)
async def hoho(ctx):
    channel = ctx.message.author.voice.channel
    if not channel:
        await ctx.send("You are not connected to a voice channel")
        return
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


@bot.command(pass_context=True)
async def fls(ctx):
    channel = ctx.message.author.voice.channel
    if not channel:
        await ctx.send("You are not connected to a voice channel")
        return
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


@bot.command(pass_context=True)
async def ban(ctx):
    channel = ctx.message.author.voice.channel
    if not channel:
        await ctx.send("You are not connected to a voice channel")
        return
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


@bot.command(pass_context=True)
async def bn(ctx):
    channel = ctx.message.author.voice.channel
    if not channel:
        await ctx.send("You are not connected to a voice channel")
        return
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


bot.run(token)
