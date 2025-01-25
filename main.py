import random
import os
import requests
import discord
import requests
from discord.ext import commands
from settings import settings

intents = discord.Intents.default()
intents.message_content = True
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)


@bot.command()
async def clear(ctx):
    await ctx.channel.purge()
    await ctx.send("Chat cleared", delete_after = 2)
    await ctx.send("Hello, my name is José Luis, your The Legend of Zelda : Tears of the Kingdom personal assistant. Feel free to ask me anything about the game.")

@bot.command()
async def hello(ctx):
    await ctx.send("Hello, my name is José Luis, your The Legend of Zelda : Tears of the Kingdom personal assistant. Feel free to ask me anything about the game.")

@bot.command()
async def dragon_tears(ctx):
    await ctx.send("""Here is a list with the name, closest tower and coordinates of each Dragon's Tear, and a map with their locations:
-> Dragon's Tear # 1 - Rauru Geoglyph (-1412,0966,0123) - (Where Am I?) - Closest Tower: Lindor's Brow
-> Dragon's Tear # 2 - ​​Forgotten Temple Geoglyph ( -2551,1885,0319) - (An Unfamiliar World) - Closest Tower: Lindor's Brow
-> Dragon's Tear # 3 - ​​Purah Pad Geoglyph (1828,0737,0089) - (Mineru's Counsel) - Closest Tower: Eldin Canyon
-> Dragon's Tear # 4 - Fish Geoglyph (0694,-1319,0053) - (The Gerudo Assault) - Closest Tower: Sahasra Slope
-> Dragon's Tear # 5 - Ganondorph Geoglyph (-3178,-1699,0418) - (A Show of Fealty) - Closest Tower: Gerudo Highlands
-> Dragon's Tear # 6 - Queen Geoglyph (-3096,-0076,0211) - (Zelda and Sonia) - Closest Tower: Gerudo Highlands
-> Dragon's Tear # 7 - ​​Scimitar Geoglyph (3325,-3566,0004) - (Sonia Is Caught by Treachery) - Closest Tower: Rabella Wetlands
-> Dragon's Tear # 8 - ​​Demon King Geoglyph (-1863,3621,0236) - (Birth of the Demon King) - Closest Tower: Pikida Stonegrove
-> Dragon's Tear # 9 - Sacred Stone Geoglyph (4468,-0305,0074)- (The Sages' Vow) - Closest Tower: Mount Lanayru
-> Dragon's Tear # 10 - ​​Memorial Stone Geoglyph (-0649,-2682,0068) - (A King's Duty) - Closest Tower: Popla Foothills
-> Dragon's Tear # 11 - ​​Master Sword Geoglyph (0891,2951,0362) - (A Master Sword in Time) - Closest Tower: Typhlo Ruins
-> Dragon's Tear # 12 -  The Last Dragon Tear (4534,2134,0000) - (The Dragon's Tears) -  Closest Tower: Ulri Mountains 
                   """)
    with open('/Users/a8a/Downloads/Jose Luis/tears_map.png', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)



bot.run(settings['TOKEN'])
