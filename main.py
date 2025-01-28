import random
import os
import requests
import discord
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
    await ctx.send("""Exploration is one of the most important activities in the game. The most important landmarks on Hyrule are Skyview Towers, Dragon's Tears Geoglyphs, Shrines, Chasms, Villages, Stables, Great Fairy Fountains,Caves and Cherry Trees. There is a dedicated section for each landmark.""")


@bot.command()
async def dragon_tears(ctx):
    await ctx.send("""Here is a list with the name, closest tower, and coordinates of each Dragon's Tear, and a map with their locations:

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
    await ctx.send("""There are 15 Skyview Towers across Hyrule. Interaction with their launch pads will reveal the corresponding regional maps. Many of them are not operational when discovered, and a short quest must be completed to gain acces to them. Here is a list with the name and coordinates of each Skyview Tower, as well as map with their locations:

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
    await ctx.send("""
NORTHERNMOST LATITUDES
-> Tauyosipun Shrine (-4539,2881,0262) - Type: Puzzle -  Shrine Quest: None
-> Otak Shrine (-4391,3714,0212) - Type: Proving Grounds - Shrine Quest: None
-> Eutoum Shrine (-3506,3570,0387) - Type: Proving Grounds - Shrine Quest: None
-> Rutafu-um Shrine (-2996,3102,0515) - Type: Rauru’s Blessing - Shrine Quest: The Northwest Hebra Cave Crystal
-> Sisuran Shrine (-2560,3353,0245) - Type: Rauru’s Blessing - Shrine Quest: The North Hebra Mountains Crystal
-> Orochium Shrine (-1636,2641,0239) - Type: Puzzle - Shrine Quest: None
-> Oshozan-u Shrine (-1405,3677,0288) - Type: Puzzle - Shrine Quest: None
-> Mayausiy Shrine (-1165,2602,-0083) - Type: Puzzle - Shrine Quest: None
-> Mayaotaki Shrine (-0823,3535,0235) - Type: Rauru’s - Shrine Quest: None
-> Minetak Shrine (0393,3485,0068) - Type: Rauru’s Blessing - Shrine Quest: None
-> Kikakin Shrine (-0395,2736,0287) - Type: Puzzle - Shrine Quest: None
-> Sikukuu Shrine (0699,2793,0226) - Type: Puzzle - Shrine Quest: None
-> Mayak Shrine (1270,3733,0106) - Type: Puzzle - Shrine Quest: None
-> Jiotak Shrine (1833,3179,0258) - Type: Rauru’s Blessing - Shrine Quest: None
-> Marakuguc Shrine (1761,2508,0437) - Type: Puzzle - Shrine Quest: None
    """)
    await ctx.send("""
-> Isisim Shrine (1841,2841,0363) - Type: Proving Grounds - Shrine Quest: None
-> Sibajitak Shrine (2399,3274,0402) - Type: Puzzle - Shrine Quest: None
-> Kimayat Shrine (2863,3637,0241) - Type: Proving Grounds - Shrine Quest: None
-> Sitsum Shrine (2369,25950790) - Type: Puzzle - Shrine Quest: None
-> Kamatukis Shrine (3431,3355,0071) - Type: Puzzle - Shrine Quest: None
-> Momosik Shrine  (2959,2758,0524) - Type: Rauru’s Blessing - Shrine Quest: The Death Caldera Crystal
-> Jochi-iu Shrine  (4346,2875,0165) - Type: Puzzle - Shrine Quest: None
-> Igashuk Shrine (4654,3712,0131) - Type: Rauru’s Blessing - Shrine Quest: None
-> Rasiwak Shrine  (4664,3262,0002) - Type: Puzzle - Shrine Quest: None   
    """)
    await ctx.send("""
NORTHERLY LATITUDES
-> Wao-os Shrine (-4059,1990,0183) - Type: Puzzle - Shrine Quest: The White’s Bird Guidance
-> Ikatak Shrine (-3950,1138,0112) - Type: Rauru’s Blessing  - Shrine Quest: The Gisa Crater Crystal
-> Gatakis Shrine (-3650,1805,0168) - Type:  Puzzle - Shrine Quest: None
-> Sahirow Shrine (-3354,2387,0361) - Type: Puzzle - Shrine Quest: None
-> Oromuwak Shrine (-3079,1617,0243) - Type: Puzzle - Shrine Quest: None
-> Nouda  Shrine (-2318,2201,0173) - Type: Proving Grounds - Shrine Quest: None
-> Iun-orok Shrine (-3538,0850,-0133) - Type: Puzzle - Shrine Quest: None
-> Runakit Shrine (-2530,1170,0178) - Type: Puzzle - Shrine Quest: None
-> Kiuyoyou Shrine (-1106,2086,0104) - Type: Puzzle - Shrine Quest: None
-> Taki-ihaban Shrine (-1830,1194,0147) - Type: Rauru’s Blessing - Shrine Quest: None
-> Tenmaten Shrine (-0593,1551,-0014) - Type Rauru’s Blessing: - Shrine Quest: None
-> Musanokir Shrine (0408,2133,0144) - Type: Puzzle  - Shrine Quest: None
->  Pupunke Shrine (0620,2211,0164) - Type: Rauru’s Blessing - Shrine Quest:
-> Sakunbomar Shrine (0166,2319,0179) - Type: Rauru’s Blessing - Shrine Quest: None Shall Pass?
    """)
    await ctx.send("""
-> Ninjis Shrine (0353,1891,0178) - Type: Rauru’s Blessing - Shrine Quest: Maca’s Special Place
-> Serutabomac Shrine (-0179,1170,0280) - Type: Puzzle  - Shrine Quest: None
-> Sepapa Shrine (0222,1085,0028) - Type: Puzzle - Shrine Quest: None
-> Rein-iz Shrine (0755,0824,0082) - Type: Puzzle - Shrine Quest: None
-> Ekochiu Shrine (1062,1279,0045) - Type: Puzzle - Shrine Quest: None
-> Timawak Shrine (1799,1638,0311) - Type: Puzzle  - Shrine Quest: None
-> Moshapin Shrine (2678,1905,0131) - Type: Rauru’s Blessing  - Shrine Quest: The Lake Intenoch Cave Crystal
-> Mayachideg Shrine (3061,1823,0216) - Type: Proving Grounds - Shrine Quest: None
-> Domizun Shrine (3305,1443,0426) - Type: Puzzle  - Shrine Quest: None
-> Kisinona Shrine (2567,1245,0173) - Type: Puzzle - Shrine Quest: None
-> Gatanisis Shrine (4498,0825,0095) - Type: Puzzle - Shrine Quest: None
-> Sinatanika Shrine (3842,2300,0048) - Type: Combat Training - Shrine Quest: None
-> Jochi-ihiga Shrine (3809,1219,0090) - Type: Rauru’s Blessing - Shrine Quest: Rock for Sale
-> Rasitakiwak Shrine (4166,1323,0229) - Type: Proving Grounds - Shrine Quest: None 
-> Gemimik Shrine (4513,2116,0001) - Type: Puzzle - Shrine Quest: None
    """)
    await ctx.send("""
MIDDLE LATITUDES
-> Otutsum Shrine (-4468,-0670,0509)  - Type: Rauru’s Blessing - Shrine Quest: None
-> Gasas Shrine (-4152,0098,0040) - Type: Puzzle  - Shrine Quest: None
-> Makurukis Shrine (-2847,0629,0233) - Type: Combat Training - Shrine Quest: None
-> Turakawak Shrine (-3496,-0197,0066) - Type: Puzzle - Shrine Quest: None
-> Sinakawak Shrine (-1413,0756,0089) - Type: Puzzle - Shrine Quest: None
-> Ishodag Shrine (-0880,0422,0049) - Type: Puzzle  - Shrine Quest: None
-> Susuyai Shrine (-0785,-0434,0018) - Type: Puzzle - Shrine Quest: None
-> Sonapan Shrine (-1920,-0359,0228) - Type: Puzzle - Shrine Quest: None
-> Jiosin Shrine (-0240,-0370,0027) - Type: Puzzle - Shrine Quest: None
-> Kyononis Shrine (-0205,0451,0021) - Type: Combat Training - Shrine Quest: None
-> Yamiyo Shrine (0332,0470,0029) - Type: Combat Training - Shrine Quest: None
-> Morok Shrine (1182,-0779,0133) - Type: Puzzle - Shrine Quest: None
-> Jonsau Shrine (1744,0017,0025) - Type: Puzzle - Shrine Quest: None 
-> Tukarok Shrine (0915,-0250,0034) - Type: Puzzle - Shrine Quest: None
-> Jojon Shrine (1202,0329,0027) - Type: Proving Grounds - Shrine Quest: None
-> Maoikes Shrine (2275,0147,0079) - Type: Rauru’s Blessing - Shrine Quest: None
-> Joniu Shrine (2918,0506,0155) - Type: Rauru’s Blessing - Shrine Quest: The Ralis Channel Crystal
-> Kurakat Shrine (2362,-0511,0156) - Type: Rauru’s Blessing - Shrine Quest: Dyeing to Find It
-> Mogawak Shrine (3299,0424,0112) - Type: Puzzle - Shrine Quest: None
-> Apogek Shrine (3887,-0217,0164) - Type: Puzzle - Shrine Quest: None
-> Yomizuk Shrine (4413,-0614,0034) - Type: Rauru’s Blessing - Shrine Quest: None
-> Ihen-a Shrine (3787,0577,0486) - Type: Puzzle - Shrine Quest: None
    """)
    await ctx.send("""
SOUTHERLY LATITUDES
-> Kudanisar Shrine (-4168,-2144,0050) - Type: Puzzle - Shrine Quest: None
-> Mayamats Shrine (-4637,-1514,0452) - Type: Puzzle - Shrine Quest: None
-> Suariwak Shrine (-2523,-1770,0131) - Type: Rauru’s Blessing - Shrine Quest: The Yiga Clan Exam
-> Turakamik Shrine (-2658,-2236,0067) - Type: Puzzle - Shrine Quest: None
-> Rotsumamu Shrine (-3407,-1362,0335) - Type: Puzzle - Shrine Quest: None
-> Tsutsu-um Shrine (-1423,-1349,0068) - Type: Puzzle - Shrine Quest: None
-> Usazum Shrine (-2139,-0873,0093) - Type: Rauru’s Blessing - Shrine Quest: The Satori Mountain Crystal
-> Tadarok Shrine (-1082,-2187,0129) - Type: Puzzle - Shrine Quest: None
-> Rakakudaj Shrine (-2036,-1854,0065) - Type: Rauru’s Blessing - Shrine Quest: The Gerudo Canyon Crystal
-> Riogok Shrine (-1440,-1616,0089) - Type: Puzzle - Shrine Quest: None
-> Susub Shrine (0348,-2051,-0026) - Type: Rauru’s Blessing - Shrine Quest: None
-> Kamizun Shrine (-0177,-1557,0023) - Type: Proving Grounds - Shrine Quest: None
-> Teniten Shrine (-0075,-1115,0021) - Type: Combat Training - Shrine Quest: None
-> Kyokugon Shrine (-0710,-1550,0006) - Type: Puzzle - Shrine Quest: None
-> Mayachin Shrine (-0705,-0869,0031) - Type: Puzzle - Shrine Quest: None
-> Tajikats Shrine (0344,-1009,0016) - Type: Puzzle - Shrine Quest: None  
    """)
    await ctx.send("""
-> Jiukoum Shrine (0867,-2279,0141) - Type: Puzzle - Shrine Quest: None
-> Makasura Shrine (1770,-1051,0166) - Type: Puzzle - Shrine Quest: None
-> Eshos Shrine (1566,-1944,0157) - Type: Combat Training - Shrine Quest: None
-> Jochisiu Shrine (0931,-1902,0030) - Type: Rauru’s Blessing - Shrine Quest: Keys Born of Water
-> O-ogim Shrine (2755,-1090,0100) - Type: Rauru’s Blessing - Shrine Quest: The Lanayru Road Crystal
-> Zakusu Shrine (3527,-1482,0168) - Type: Proving Grounds - Shrine Quest: The High Srping and the Light Rings
-> Jogou Shrine (3346,-1187,0057) - Type: Rauru’s Blessing - Shrine Quest: None
-> Zanmik Shrine (3469,-2179,0148) - Type: Puzzle - Shrine Quest: None
-> Anedamimik Shrine (4231,-2178,-0012) - Type: Puzzle - Shrine Quest: None
-> Jikais Shrine (4266,-1674,0182) - Type: Puzzle - Shrine Quest: None
-> Mayahisik Shrine (3730,-2058,0189) - Type:Rauru’s Blessing  - Shrine Quest: None    
    """)
    await ctx.send("""
 SOUTHERNMOST LATITUDES
-> Karahatag Shrine (-3726,-3625,0043) - Type: Puzzle - Shrine Quest: None
-> Miryotanog Shrine (-4679,-3086,0054) - Type: Proving Grounds - Shrine Quest: None
-> Irasak Shrine (-4159,-3824,0028) - Type: Rauru’s Blessing - Shrine Quest: None
-> Soryotanog Shrine (-3881,.2961,0123) - Type: Puzzle - Shrine Quest: None
-> Chichim Shrine (-3211,-3007,-0049) - Type: Rauru’s Blessing - Shrine Quest: None
-> Siwakama Shrine (-2445,-3345,0041) - Type: Puzzle - Shrine Quest: None
-> Mayatat Shrine (-3290,-2512,0024) - Type: Puzzle - Shrine Quest: None
-> Motsusis Shrine (-1795,-3485,0045) - Type: Rauru’s Blessing - Shrine Quest: None
-> Kitawak Shrine (-1529,-2928,0321) - Type: Puzzle - Shrine Quest: None
-> En-oma Shrine (0104,-2517,-0087) - Type: Rauru’s Blessing - Shrine Quest: The Lake Hylia Crystal
-> Ishokin Shrine (-0565,-3524,0129) - Type: Rauru’s Blessing- Shrine Quest: Ride the Giant Horse
-> Utsushok Shrine (0669,-3358,0072) - Type: Puzzle - Shrine Quest: None
-> Joju-u-u Shrine (1516,-3576,0142) - Type: Puzzle - Shrine Quest: None
-> Utojis Shrine (1217,-2542,0096) - Type: Rauru’s Blessing - Shrine Quest: Legend of the Soaring Spear
-> Tokiy Shrine (2304,-2377,-0028) - Type: Rauru’s Blessing  - Shrine Quest: The Oakle’s Navel Cave Crystal
-> Bamitok Shrine (3094,-3209,0082) - Type: Rauru’s Blessing - Shrine Quest: None
-> Sifumin Shrine (2826,-3271,0078) - Type: Proving Grounds - Shrine Quest: None
-> Mara-ri Shrine (4632,-3712,0018) - Type: Rauru’s Blessing - Shrine Quest: Seeking the Pirate Hideout   
    """)
    await ctx.send("""
HEBRA SKY
-> Ijo-o Shrine (-3860,2682,0702) - Type: Puzzle - Shrine Quest: None
-> Mayaumekis Shrine (-2947,3051,0897) - Type: Puzzle - Shrine Quest: None
-> Kahatanaum Shrine (-3294,3430,1347) - Type:  Blessing - Shrine Quest: None
-> Taninoud Shrine (-1801,3406,0949) - Type: Rauru’s Blessing - Shrine Quest: The East Hebra Sky Crystal
-> Tenbez Shrine (-0969,3535,1011) - Type: Puzzle - Shrine Quest: None
-> Ga-ahisas Shrine (-3596,0962,1719) - Type: Rauru’s Blessing - Shrine Quest: None
-> Taunhiy Shrine (-2400,0824,0615) - Type: Combat Training - Shrine Quest: None
-> Ganos Shrine (-3370,0466,1695) - Type: Rauru’s Blessing - Shrine Quest: The Tabantha Sky Crystal
ELDIN SKY
-> Kadaunar Shrine (1882,1202,1251) - Type: Puzzle - Shrine Quest: None
AKKALA SKY
-> Mogisari Shrine (4655,3500,1010) - Type: Puzzle - Shrine Quest: None
-> Natak Shrine (3671,1484,1158) - Type: Rauru’s Blessing - Shrine Quest: The Sokkala Sky Crystal 
-> Gikaku Shrine (4509,2165,1155) - Type: Rauru’s Blessing - Shrine Quest: The Sky Mine Crystal
CENTRAL HYRULE SKY
-> Mayam Shrine (0341,2814,1821) - Type: Rauru’s Blessing - Shrine Quest: The North Hyrule Sky Crystal
->  Simosiwak Shrine (0163,1972,0759) - Type: Proving Grounds - Shrine Quest: None
-> Jinodok Shrine (-1257,-1487,1008) - Type: Rauru’s Blessing - Shrine Quest: The South Hyrule Sky Crystal
     """)
    await ctx.send("""
LANAYRU SKY
-> Igoshon Shrine (3480,0664,1325) - Type: Puzzle - Shrine Quest: None
-> Jirutagumac Shrine (2916,0533,0951) - Type: Puzzle - Shrine Quest: None
-> Mayanas Shrine (4613,-0947,1790) - Type: Puzzle - Shrine Quest: The South Lanayru Sky Crystal
GERUDO SKY
-> Rakashog Shrine (-1716,-2118,1149) - Type: Puzzle - Shrine Quest: None
-> Mayasiar Shrine (-3545,-0320,1965) - Type: Rauru’s Blessing - Shrine Quest: None
-> Siyamotsus Shrine (-1795,-3295,1011) - Type: Puzzle - Shrine Quest: None
FARON SKY
-> Joku-usin Shrine (1074,-3347,0786) - Type: Proving Grounds - Shrine Quest: None
-> Joku-u Shrine (1375,-3339,0429) - Type: Rauru’s Blessing - Shrine Quest: None
NECLUDA SKY
-> Josiu Shrine (1759,-1208,0924) - Type: Rauru’s Blessing - Shrine Quest: The North Necluda Sky Crystal
-> Ukoojisi Shrine (1467,-2168,0585) - Type: Rauru’s Blessing - Shrine Quest: The West Necluda Sky Crystal
-> Yansamin Shrine (2350,-1782,1475) - Type: Proving Ground - Shrine Quest: None
-> Kumamayn Shrine (2856,-2857,1212) - Type: Rauru’s Blessing - Shrine Quest: The Necluda Sky Crystal    
    """)

    with open('/Users/a8a/Downloads/Jose Luis/shrines_map.png', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)
    with open('/Users/a8a/Downloads/Jose Luis/shrinessky_map.png', 'rb') as f:
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
    await ctx.send("""There are 4 Great Fairy Fountains across Hyrule. In them, you can upgrade your armor pieces in exchange for certain objects. They are initially locked, and a short quest must be done to unlock each of them. There is also Malanya Spring, wich will allow you to improve your horses stats, and to bring them back to life when they die. Here is a list with the name and coordinates of each Great Fairy Fountain, as well as map with their locations:

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
    await ctx.send("""There are 10 Villages across Hyrule. They are the main population centers, and within them, shops, goddess statues, cooking pots and other objects and places can be found. Here is a list with the name and coordinates of each Village, as well as map with their locations:

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
    await ctx.send("""There are 3 types of quests in the game: Main Quests, Side Quests, and Side Adventures. Main Quests are those in which the main storyline happens, and thus, they are considered necessary to complete to finish the game, although some of them can be skipped when in speed runs. Side Quests are usually simple quests, although there are a few exceptions. It is not necessary to complete them in order to finish the game, but it is recommended to complete them as they provide valuable objects. Side Adventures are longer than Side Quests but shorter than Main Quests. It is not necessary to complete them to finish the game, but just like Side Quest, it is recommended to complete them as they provide valuable objects. There is a dedicated section for each type of quest.""")    

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
 """)
    await ctx.send("""
HEBRA
-> Potential Princess Sightings! - Quest Vendor: Traysi (-3258,1763,0119)
-> The Hornist's Dramatic Escape - Quest Vendor: Eustus (-3648,0756,0118)
-> Serenade to Mija - Quest Vendor: Mastro (-1630,2589,0234)
-> Zelda's Golden Horse - Quest Vendor: Penn (-1641,2582,0233)
-> Bring Peace to Hebra! - Quest Vendor: Flaxel (-1791,2301,0238)
 """)
    await ctx.send("""
ELDIN
->  Bring Peace to Eldin!- Quest Vendor: Toren (2369,3059,0448)
->  For Our Princess- Quest Vendor: Penn (2583,1154,0148)
 """)
    await ctx.send("""
AKKALA
-> Mattison´s Independence - Quest Vendor: Hudson (3936,1590,0129)
-> The All-Clucking Cucco - Quest Vendor: Penn (3163,1716,0201)
-> Bring Peace to Akkala! - Quest Vendor: Toren (3005,1126,0281)
-> The Search for Koltin - Quest Vendor: N/A (Unlocked automatically)
-> A Monstrous Collection (x5) - Quest Vendor: Kilton (3960,1642,0128)
 """)
    await ctx.send("""
NECLUDA
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
 """)
    await ctx.send("""
FARON
-> The Flute Player's Plan - Quest Vendor: Pyper (0528,-3395,0056)
-> Bring Peace to Faron! - Quest Vendor: Flaxel (-0021,-324,0007)
-> An Eerie Voice - Quest Vendor: Penn (0504,-3444,0047)
 """)
    await ctx.send("""
GERUDO
-> The Blocked Well - Quest Vendor: Penn (-2817,-2235,0029)
-> Infiltrating the Yiga Clan - Quest Vendor:  Mimos (-3687,-1365,0331)
-> The Yiga Clan Exam - Quest Vendor: Yiga Blademaster (-2479,-1794,0137)
 """)
    await ctx.send("""
GREAT HYRULE FOREST
-> Investigate Typhlo Ruins - Quest Vendor: Kazul (0373,3095,0174)
-> The Owl Protected by Dragons - Quest Vendor: Kazul (0373,3095,0174)
-> The Corridor Between Two Dragons - Quest Vendor: Kazul (0373,3095,0174)
-> The Six Dragons - Quest Vendor: Kazul (0373,3095,0174)
-> The Long Dragon - Quest Vendor: Kazul (0373,3095,0174)
 """)
    await ctx.send("""
DEPTHS
-> Master Kohga of the Yiga Clan (x4) - Quest Vendor: Kohga (-0803,-1928,-0520)
 """)
    await ctx.send("""
SKY
->  Legend of the Great Sky Island - Quest Vendor: Steward Construct (0453,-0802,1540)
 """)
    await ctx.send("""
ADDITIONAL ADVENTURES
-> Hino's Cages, Bubbul Gems, Addison's Signboards
                  """)   
    
#############################################################################################
                                    #BESTIARY#

bot.run(settings['TOKEN'])
