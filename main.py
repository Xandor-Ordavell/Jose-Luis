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

#####################################################################################################
                                #LANDMARKS#

@bot.command()
async def landmarks(ctx):  
    await ctx.send("""Exploration is one of the most important activities on the game. The most important landmarks on Hyrule are Skyview Towers, Dragon's Tears Geoglyphs, Shrines, Chasms, Light Roots, Villages, Stables, Great Fairy Fountains,Caves and Cherry Trees. There is a dedicated section for each landmark.""")


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


@bot.command()
async def towers(ctx):  
    await ctx.send("""There are 15 Skyview Towers across Hyrule. Interactiong with their launch pads will reveal the corresponding regional maps. Many of them are not operational when discovered, and a short quest must be completed to gain acces to them. Here is a list with the name and coordinates of each Skyview Tower, as well as map with their locations:

-> Pikida Stonegrove Skyview Tower (-2311,3062,0423)
-> Gerudo Highlands Skyview Tower (-3961,-1306,0402)
-> Rospro Pass Skyview Tower (-3680,2346,0213)
-> Lindor's Brow Skyview Tower (-1910,1245,0277)
-> Lookout Landing Skyview Tower (-0299,0143,0005)
-> Hyrule Field Skyview Tower (-0761,-1019,0044)
-> Gerudo Canyon Skyview Tower (-2439,-2183,0287)
-> Sahasra Slope Skyview Tower (1341,-1178,0146)
-> Popla Foothills Skyview Tower (0605,-2127,0078)
-> Rabella Wetlands Skyview Tower (2420,-2755,0202)
-> Upland Zorana Skyview Towers (2866,0581,0359)
-> Mount Lanayru Skyview Tower (3848,-1315,0519)                    
-> Ulri Mountain Skyview Tower  (3499,2026,0168)
-> Eldin Canyon Skyview Tower (1642,1191,0205)
-> Thyplo Ruins Skyview Tower (0344,3142,0160)      
                    """)
    with open('/Users/a8a/Downloads/Jose Luis/towers_map.png', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)


@bot.command()
async def shrines(ctx):  
    with open('/Users/a8a/Downloads/Jose Luis/shrines_map.png', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)
    with open('/Users/a8a/Downloads/Jose Luis/shrinessky_map.png', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)


@bot.command()
async def roots(ctx):  
    with open('/Users/a8a/Downloads/Jose Luis/lightroots_map.png', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)


@bot.command()
async def stables(ctx): 
    await ctx.send("""There are 14 Stables and 2 Mini Stables (one on Lookout Landing an the other on the Digdogg Suspension Bridge) across Hyrule. In them you can keep up to 7 horses and sleep for 20 or 40 ruppes. Most interactions in them give reward points, wich can be then exchanged for certain objects. Here is a list with the name and coordinates of each Stable, as well as map with their locations:

->  Snowfield Stable (-1655,2572,0263)
->  Tabantha Bridge Stable (-2932,0548,0200)
->  Gerudo Canyon Stable (-2804,-2226,0060)
->  New Serenne Stable (-1361,0724,0072)
->  Outskirt Stable (-1449,-1269,0062)
->  Woodland Stable (1062,1135,0053)
->  Wetland Stable (0888,-0174,0057)
->  Riverside Stable (0339,-1095,0026)
->  Highland Stable (0530,-3451,0082)
->  Lakeside Stable (1552,-3538,0092)
->  Dueling Peaks Stable (1756,-1924,0040)
->  Foothill Stable (2613,1144,0135)                    
->  South Akkala Stable (3149,1691,0220)
->  East Akkala Stable (4231,2746,0156)    
                    """) 
    with open('/Users/a8a/Downloads/Jose Luis/stables_map.png', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)


@bot.command()
async def chasms(ctx):  
    with open('/Users/a8a/Downloads/Jose Luis/chasms_map.png', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)


@bot.command()
async def fountains(ctx):  
    await ctx.send("""There are 4 Great Fairy Fountains across Hyrule. In them you can upgrade your armour pieces in exchange of certain objects. They are initially locked, and a short quest must be done to unlock each of them. There is also Malanya Spring, wich will allow you to improve your horses stats, and to bring them back to life when they die. Here is a list with the name and coordinates of each Great Fairy Fountain, as well as map with their locations:

->  Great Fairy Mija (-1460,2995,0288)
->  Great Fairy Kaysa  (-1557,-1231,0063)
->  Great Fairy Cotera (1768,-2180,-0013)
->  Great Fairy Tera  (0916,1386,0068)
                   """)   
    with open('/Users/a8a/Downloads/Jose Luis/fountains_map.png', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)


@bot.command()
async def villages(ctx): 
    await ctx.send("""There are 10 Villages across Hyrule. They are the main population centers, and within them shops, goddess statues, cooking pots and other objects and places can be found. Here is a list with the name and coordinates of each Village, as well as map with their locations:

->  Rito Village (-3621,1800,0090)
->  Gerudo Town (-3866,-2942,-0002)
->  Korok Forest (0419,2140,-0119)
->  Lookout Landing (-0254,0102,0004)
->  Goron City (1657,2440,0327)
->  Kakariko Village (1817,-0988,0105)
->  Tarrey Town (3966,1611,0114)
->  Zora's Domain(3331,0545,0124)
->  Hateno Village (3545,-2090,0218)
->  Lurelin Village (3007,-3474,0023)
                   """)    
    with open('/Users/a8a/Downloads/Jose Luis/village_map.png', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)


@bot.command()
async def trees(ctx):   
    with open('/Users/a8a/Downloads/Jose Luis/tress_map.png', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

@bot.command()
async def caves(ctx):   
    with open('/Users/a8a/Downloads/Jose Luis/caves_map.png', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)


#############################################################################################
                                    #QUESTS#

@bot.command()
async def quests(ctx): 
    await ctx.send("""There are 3 types of quests in the game: Main Quests, Side Quests, and Side Adventures. Main Quests are those in which the main storyline happens, and thus, they are considered necessary to complete to finish the game, although some of them can be skipped when in speed runs.
                   Side Quests are usually simple quests, although there are a few exceptions. It is not necessary to complete them in order to finish the game, but it is recommended to complete them as they provide valuable objects. Side Adventures are longer than Side Quests but shorter than Main Quests.
                   It is not necessary to complete them to finish the game, but just like Side Quest, it is recommended to complete them as they provide valuable objects. There is a dedicated section for each type of quest.""")    

@bot.command()
async def main_quests(ctx): 
    await ctx.send("""There are a total of 23 Main Quests in the game, making up the main storyline. Here is a list of all the Main Quests organized chronologically (Note that most of them can be completed in different orders, but this is the recommended oath, as the difficulty of the quests increases this way):

-> Find Princess Zelda
-> The Closed Door
-> To the Kingdom of Hyrule
-> Crisis at Hyrule Castle
-> Regional Phenomena
-> Camera Work in the Depths
-> Impa and the Geoglyphs
-> The Dragon's Tears
-> Tulin of Rito Village
-> A Mystery in the Depths
-> Yunobo of Goron City
-> The Sludge- Covered Statue
-> The Broken Slate
-> Clues To The Sky
-> Restoring the Zora Armor
-> Sidon of the Zora's Domain
-> Riju of Gerudo Time
-> Secret of the Ring Ruins
-> Find the fifth Sage
-> Guidance from Ages Past
-> Trail of the Master Sword
-> Recovering the Hero's Sword
-> Destroy Ganondorf 
                  """)   

@bot.command()
async def side_adventures(ctx): 
    await ctx.send("""There are a total of 56 Side Aventures in the game. Many of them are not available at the start of the game, and other quests must be completed to unlock them. Here is a list of all the Side Adventures organized by geographical regions, and with the respective quest vendor:

CENTRAL HYRULE
-> Hetsu's Concerns - Quest Vendor: Hetsu 
-> The Hunt for Bubbul Gems! - Quest Vendor: Kilton (1222,1207,0020)
-> Bring Peace to Hyrule Field! - Quest Vendor: Hoz (-0433,-0490,0025)
-> A Call from the Depths - Quest Vendor: Mysterious Voice
-> The Beast and the Princess - Quest Vendor: Penn (-1348,0734,0085)
-> The Beckoning Woman - Quest Vendor: Penn (-1413,-1295,0031)
-> Gourmets Gone Missing - Quest Vendor: Penn (0387,-1045,0015) 
-> White Goats Gone Missing - Quest Vendor: Penn (-2910,0524,0169)
-> The Missing Farm Tools - Quest Vendor: Penn (0876,-0159,0025) 
-> Who Goes There? - Quest Vendor: Jerrin (-0256,0107,0008) 
-> A Deal with the Statue - Quest Vendor: Horned Statue (-0234,0157,0004)
-> Messages from an Ancient Era - Quest Vendor: Wortsworth (-0268,0066,0018)
-> Serenade to a Great Fairy - Quest Vendor: Penn (1047,1149,0022)
-> Serenade to Kaysa - Quest Vendor: Mastro (-1406,-1264,0032)

HEBRA
-> Potential Princess Sightings! - Quest Vendor: Traysi (-3258,1763,0119)
-> The Hornist's Dramatic Escape - Quest Vendor: Eustus (-3648,0756,0118)
-> Serenade to Mija - Quest Vendor: Mastro (-1630,2589,0234)
-> Zelda's Golden Horse - Quest Vendor: Penn (-1641,2582,0233)
-> Bring Peace to Hebra! - Quest Vendor: Flaxel (-1791,2301,0238)

ELDIN
->  Bring Peace to Eldin!- Quest Vendor: Toren (2369,3059,0448)
->  For Our Princess- Quest Vendor: Penn (2583,1154,0148)

AKKALA
-> Mattison´s Independence - Quest Vendor: Hudson (3936,1590,0129)
-> The All-Clucking Cucco - Quest Vendor: Penn (3163,1716,0201)
-> Bring Peace to Akkala! - Quest Vendor: Toren (3005,1126,0281)
-> The Search for Koltin - Quest Vendor: N/A (Unlocked automatically)
-> A Monstrous Collection (x5) - Quest Vendor: Kilton (3960,1642,0128)

Necluda
-> Princess Zelda Kidnapped?!- Quest Vendor: Penn (1758,-1925,0040) 
-> Bring Peace to Necluda! - Quest Vendor: Hoz (2261,-1838,0011)
-> Honey, Bee Mine - Quest Vendor: Beetz (2167,-1380,0109) 
-> Serenade to Cotera - Quest Vendor: Mastro (-1755,-1958,0010)
-> Hateno Village Research Lab - Quest Vendor: Robbie (-0249,0136,0019)
-> Presenting: Sensor +! - Quest Vendor: Robbie (3781,-2123,0251)
-> Presenting: The Travel Medallion! - Quest Vendor: Robbie (3781,-2123,0251)
-> Presenting: Hero's Path Mode! - Quest Vendor: Robbie (3781,-2123,0251)
-> Filling Out the Compendium - Quest Vendor: Robbie (3781,-2123,0251)
-> Team Cece or Team Reede? - Quest Vendor: Cece (3354,-2125,0121)
-> A Letter to Koyin - Quest Vendor: Koyin (3632,-2051,0174)
-> Reede's Secret - Quest Vendor: Clavia (3422,-2092,0130)
-> Cece's Secret - Quest Vendor: Sophie (3357,-2139,0120)
-> A New Signature Food - Quest Vendor: Reede (3429,-2082,0131)
-> The Mayoral Election - Quest Vendor: Sophie (3357,-2139,0120)
-> Ruffian Infested Village - Quest Vendor: Rozel (2782,-3272,0083)
-> Lurelin Village Restoration Project - Quest Vendor: Bolson (2875,-3443,0000)

FARON
-> The Flute Player's Plan - Quest Vendor: Pyper (0528,-3395,0056)
-> Bring Peace to Faron! - Quest Vendor: Flaxel (-0021,-324,0007)
-> An Eerie Voice - Quest Vendor: Penn (0504,-3444,0047)

GERUDO
-> The Blocked Well - Quest Vendor: Penn (-2817,-2235,0029)
-> Infiltrating the Yiga Clan - Quest Vendor:  Mimos (-3687,-1365,0331)
-> The Yiga Clan Exam - Quest Vendor: Yiga Blademaster (-2479,-1794,0137)

GREAT HYRULE FOREST
-> Investigate Typhlo Ruins - Quest Vendor: Kazul (0373,3095,0174)
-> The Owl Protected by Dragons - Quest Vendor: Kazul (0373,3095,0174)
-> The Corridor Between Two Dragons - Quest Vendor: Kazul (0373,3095,0174)
-> The Six Dragons - Quest Vendor: Kazul (0373,3095,0174)
-> The Long Dragon - Quest Vendor: Kazul (0373,3095,0174)

DEPTHS
-> Master Kohga of the Yiga Clan (x4) - Quest Vendor: Kohga (-0803,-1928,-0520)

SKY
->  Legend of the Great Sky Island - Quest Vendor: Steward Construct (0453,-0802,1540)

ADDITIONAL ADVENTURES
-> Hino's Cages, Bubbul Gems, Addison's Signboards
                  """)   
    
#############################################################################################
                                    #BESTIARY#
