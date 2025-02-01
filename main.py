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
    await ctx.send("""Shirens are special landmarks that you will encounter during your travels. Completing their challenges will gradually enable you to make Link more powerful. There are a total of 152 shrines across the surface and the sky of Hyrule. Here is a list with their region, coordinates, the challenge type, and the shrine quest that must be completed to unlock them. There is also a map with their relative positions.  """)   
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
async def trees(ctx):  
     await ctx.send("""There is a total of 8 cherry trees all across Hyrule. If you deposit one or more apples in the dish at their base, Satori, the Lord of the Mountain will appear, and all surrounding non-discovered caves will glow for some minutes, making this a great way to look out for new areas. Here is a list with the coordinates of each tree, as well as a map with their relative positions:
-> Cherry-blossom tree 1 (0317, 0542, 0035)	
-> Cherry-blossom tree 2 (-4050, 1690, 0207)	
-> Cherry-blossom tree 3 (-2299, -0341, 0356)
-> Cherry-blossom tree 4 (-2315, -2158, 0258)	
-> Cherry-blossom tree 5 (0799, -3502, 0070)	
-> Cherry-blossom tree 6 (1239, 2957, 0424)	
-> Cherry-blossom tree 7 (2531, -0005, 0153)	
-> Cherry-blossom tree 8 (3358,-2479,0288)
     """)
    with open('/Users/a8a/Downloads/Jose Luis/tress_map.png', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)


@bot.command()
async def fountains(ctx):  
    await ctx.send("""There are 4 Great Fairy Fountains across Hyrule. In them, you can upgrade your armor pieces in exchange for certain objects. They are initially locked, and a short quest must be done to unlock each of them. There is also Malanya Spring, wich will allow you to improve your horse's stats, and bring them back to life when they die. Here is a list with the name and coordinates of each Great Fairy Fountain, as well as map with their locations:

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
async def chasms(ctx):  
    await ctx.send("""There are a total of 36 chasms, deep fissures glowing red with hazardous Gloom, serving as gateways to the Depths beneath Hyrule. Here is a list with all the chasms coordinates, as well as a map with their relative positions
-> Birida Lookout Chasm (-3686, -1860, 0045)
-> Chasm Under Zora's Domain (3272, 0442, -0009)
-> Death Mountain Chasm (2535, 2603, 0644)
-> Deku Tree Chasm (0418, 2193, 0153)
-> Drenan Highlands Chasm (-0071, 2984, 0136)
-> East Akkala Plains Chasm (4030, 2181, -0083)
-> East Gerudo Chasm (-2491, -3068, 0018)
-> East Hill Chasm (1974, -0846, 0125)
-> Elma Knolls Chasm (-0457, 1722, 0178)
-> Eventide Island Chasm (4507, -3459, -0005)
-> Forest of Time Chasm (-0128, -1658, -0020)
-> Gerudo Summit Chasm (-4203, -0638, 0644)
-> Great Plateau East Chasm (-0453, -1993, 0078)
-> Great Plateau North Chasm (-0665, -1510, 0060)
-> Great Plateau South Chasm (-0933, -2318, 0172)
-> Great Plateau West Chasm (-1432, -1993, 0234)
-> Hills of Baumer Chasm (0222, -2119, 0010)
-> Hyrule Castle Chasm (-0254, 1012, -0194)
-> Hyrule Castle Moat East Chasm (0170, 0882, -0036)
-> Hyrule Castle Moat West Chasm (-0923, 0667, 0002)
-> Hyrule Field Chasm (-0255, -0300, 0010)
-> Hyrule Ridge Chasm (-2644, 1126, 0152)
-> Lake Hylia Chasm (-0332, -2598, -0039)
-> Lanayru Wetlands Chasm (1727, 0162, 0007)
-> Lomei Labyrinth Chasm (4655, 3697, 0038)
-> Meda Mountain Chasm (2514, -2381, 0141)
-> Minshi Woods Chasm (1059, 1668, 0159)
-> Naydra Snowfield Chasm (3605, -1344, 0128)
-> North Lomei Chasm (-0814, 3535, 0228)
-> Rito Village Chasm (-3571, 1803, 0129)
-> Skull Lake Chasm (3247, 3442, -0031)
-> South Akkala Plains Chasm (3297, 1287, 0135)
-> South Lomei Chasm (-1795, -3462, 0055)
-> Tingel Island Chasm (4708, 1308, 0129)
-> Tobio's Hollow Chasm (1305, -2397, 0073)
-> Yiga Clan Hideout Chasm (-3430, -1333, 0287)
    """)
    with open('/Users/a8a/Downloads/Jose Luis/chasms_map.png', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

@bot.command()
async def caves(ctx): 
    await ctx.send("""There are 147 caves across Hyrule, both on the surface and in the sky. These caves are home to Bubbulfrogs and other precious items, and many of them have multiple entrances for different exploration paths. Here is a list with the cave entrance coordinates, and a map with their locations:
SURFACE
-> Ulria Grotto South Cave - Cave entrance (4122,0662,0197)
-> Ulria Grotto East Cave - Cave entrance (4505,0705,0107) (4273,0774,0154)
-> Tarrey Town Tunnel - Cave entrance (3926,1576,0117)
-> Construction Site Cave - Cave entrance (3679,1538,0085) (3735,1534,0092)
-> Akkala Citadel Ruins Cave - Cave entrance (3244,1457,0301)
-> Skull Lake Cave - Cave entrance (3322,3424,0180)
-> North Akkala Beach Cave - Cave entrance (4651,3585,-0038) (4646,3207,0019)
-> Akkala Citadel Ruins Summit Cave - Cave entrance (3293,1492,0400)
-> Ranch Ruins Cave - Cave entrance (0037,-0199,0031) (0006,-0158,0042)
-> Great Plateau Foothill Cave - Cave entrance (-0832,-1488,0039)
-> Royal Hidden Passage - Cave entrance (-0326,0803,0065) (-0254,0129,0020) (-0254,0767,0039)
-> Ancient Tree Stump Cave - Cave entrance (-1112,-0432,0035)
-> Whistling Hill Cave - Cave entrance (-0072,-1046,0029)
-> Passeri Greenbelt Cave - Cave entrance (-0512,0128,0032)
-> Coliseum Ruins Cave - Cave entrance (-1167,-1311,0034)
-> Sage Temple Cave - Cave entrance (-1405,-0257,0008)
-> Death Mountain East Tunnel - Cave entrance (2768,2778,0524)
-> Death Mountain West Tunnel - Cave entrance (2239,2682,0524)
-> Lake Darman Monster Den - Cave entrance (2373,3052,0450)
-> Isle of Rabac Gallery - Cave entrance (1555,3103,0398)
-> Goronbi River Cave - Cave entrance (1423,2103,0292)
-> Southern Mine - Cave entrance (1801,1983,0327)
-> Gorko Tunnel - Cave entrance (2016,2039,0426)
""")
    await ctx.send("""
-> West Restaurant Cave - Cave entrance (1643,1730,0286)
-> East Restaurant Cave - Cave entrance (1854,1720,0299)
-> Lizard's Burrow - Cave entrance (2206,3075,0411)
-> Lake Intenoch Cave - Cave entrance (2485,1793,0167)
-> YunoboCo HQ East Cave - Cave entrance (1765,2837,0405)
-> YunoboCo HQ South Cave - Cave entrance (1714,2719,0406)
-> Death Mountain Foothill Cave - Cave entrance (1950,2687,0431)
-> Lake Ferona Cave - Cave entrance (1930,1272,0132) (1932,1305,0177)
-> Cephla Lake Cave - Cave entrance (2594,1330,0161)
-> Foothill Monster Den - Cave entrance (2275,1520,0167)
-> Floria River Upstream Excavation - Cave entrance (0810,-2972,0023)
-> Pagos Woods Excavation Site - Cave entrance (0672,-3109,0036)
-> Tobio's Hollow Cave - Cave entrance (1170,-2444,0186)
-> Cora Lakefront Cave - Cave entrance (-0256,-2940,-0006) (-0171,-3067,-0001)
-> Finra Woods Excavation Site - Cave entrance (0569,-2982,0025)
-> Sarjon Woods Cave - Cave entrance (1203,-3171,0037)
-> Lake Hylia Whirlpool Cave - Cave entrance (0126,-2501,-0076)
-> Popla Foothills Excavation Site - Cave entrance (0609,-2210,0062)
-> Puffer Beach Overhead Cave - Cave entrance (0284,-3851,0045)
-> River of the Dead Waterfall Cave - Cave entrance (-1092,-2163,0153)
-> Shrine of Resurrection - Cave entrance (-1062,-1830,0152)
-> Gerudo Sanctuary - Cave entrance (-3763,-2699,0027) (-3763,-2421,0027)
-> Valley of Silent Statues - Cave entrance (-3827,-2650,0047)
-> Quicksand Lake Cave - Cave entrance (-3239,-2940,-0052)
-> Mount Nabooru Cave - Cave entrance (-1967,-2060,0042) (-1796,-1961,0043)
-> Stalry Plateau Cave - Cave entrance (-1528,-2223,-0008)
-> East Gerudo Ruins Cave - Cave entrance (-2696,-2809,-0054)
-> Central Gerudo Cave - Cave entrance (-3679,-3255,-0006)
-> Mount Nabooru South Cave - Cave entrance (-1727,-2183,0017)
-> Lower Spectacle Rock Cave - Cave entrance (-1744,-2394,0001)
-> Spectacle Rock Cave - Cave entrance (-2216,-2395,0255)
-> Ancient Prison Ruins - Cave entrance (-3099,-3064,-0038)
-> South Gerudo Cave - Cave entrance (-2939,-3858,-0024)
""")
    await ctx.send("""
-> Koukot Plateau Cave - Cave entrance (-2259,-1759,0068) (-2174,-1842,0137)
-> Ancient Altar Ruins - Cave entrance (-2536,-3626,-0035) (-2519,-3672,-0035) (-2584,-3638,-0035) (-2571,-3744,-0038) (-2531,-3769,-0034) (-2481,-3758,-0034) (-2521,-3725,-0034) (-2565,-3682,-0035) (-2452,-3677,-0033) (-2481,-3633,-0033) (-2478,-3710,-0034)
-> Oasis Source - Cave entrance (-3355,-2694,0008)
-> Gerudo Great Skeleton - Cave entrance (-4814,-3875,0011)
-> West Gerudo Underground Ruins - Cave entrance (-4673,-1986,0021)
-> Yiga Blademaster Station - Cave entrance (-2434,-1820,0155)
-> Gerudo Canyon Mine - Cave entrance (-2611,-2605,0123) (-2677,-2403,0090)
-> Taafei Hill Cave - Cave entrance (-2457,-1799,0185)
-> Statue of the Eighth Heroine Cave - Cave entrance (-4385,-0537,0478)
-> Meadela's Mantle Cave - Cave entrance (-3983,-1245,0431)
-> Mystathi's Shelf Cave - Cave entrance (-3882,-0727,0572)
-> Mount Dunsel Cave - Cave entrance (3224,-3018,0071) (3291,-3296,0076)
-> Mount Floria Cave - Cave entrance (1960,-2612,0082) (1790,-2986,0091)
-> Corta Lake Cave - Cave entrance (1677,-3039,0174)
-> Rodai Lakefront Tunnel - Cave entrance (1896,-3111,0142)
-> Calora Lake Cave - Cave entrance (1959,-3033,0202) (2010,-3164,0186)
-> Rassla Lake Cave - Cave entrance (1814,-3738,0129)
-> Eventide Island Cave - Cave entrance (4753,-3782,0006)
-> Ubota Point Cave - Cave entrance (1447,-3484,0088)
-> Atun Valley Cave - Cave entrance (2454,-3193,0076)
-> Byroad to Lanayru Wetlands - Cave entrance (1617,-1260,0019) (1588,-0812,0018)
-> Kakariko Village Cave - Cave entrance (1947,-0982,0167)
-> Cucco Hideaway - Cave entrance (1877,-1160,0207)
-> Sahasra Slope Cave - Cave entrance (1373,-1197,0140) (1328,-1156,0144)
-> Dueling Peaks North Cave - Cave entrance (1194,-1854,0167)
-> Dueling Peaks South Cave - Cave entrance (1183,-1948,0253)
-> Sturnida Springs Cave - Cave entrance (-4041,2671,0035)
-> Icefall Foothills Cave - Cave entrance (-4429,3760,0232)
-> Lake Kilsie Cave - Cave entrance (-3931,2861,-0005)
-> Hebra Headspring Cave - Cave entrance (-2900,2510,0393)
""")
    await ctx.send("""
-> Pikida Stonegrove Northwest Cave - Cave entrance (-2642,3268,0257) (-2414,3136,0378)
-> Hebra Great Skeleton - Cave entrance (-3815,3595,0263)
-> Hebra Mountains Northwest Cave - Cave entrance (-2996,3226,0543)
-> Brightcap Cave - Cave entrance (-3006,1635,0208)
-> Rospro Pass Cave - Cave entrance (-3560,2488,0235)
-> Talonto Peak Cave - Cave entrance (-3215,2462,0352)
-> Hebra South Summit Cave - Cave entrance (-3398,2499,0320) (-3227,2535,0446)
-> Tabantha Hills Cave - Cave entrance (-2841,1772,0231)
-> Mount Drena Foothill Cave - Cave entrance (-1372,2861,0207)
-> Kopeeki Drifts Cave - Cave entrance (-2396,2277,0179)
-> West Lake Totori Cave - Cave entrance (-3959,2029,0209)
-> North Biron Snowshelf Cave - Cave entrance (-3960,3245,0245)
-> East Biron Snowshelf Cave - Cave entrance (-3555,3088,0281) (-3989,3063,0148)
-> Rauru Hillside Cave - Cave entrance (0676,1390,0057)
-> Pico Pond Cave - Cave entrance (1247,1232,0037)
-> Yiga Clan Maritta Branch - Cave entrance (-0644,2040,0164)
-> Deplian Badlands Cave - Cave entrance (0307,3579,0098)
-> North Hyrule Plain Cave - Cave entrance (-1234,0770,0088) (-1188,0645,0083)
-> Tamio River Downstream Cave - Cave entrance (-2922,-0804,0020)
-> Lindor's Brow Cave - Cave entrance (-1735,1166,0237)
-> Satori Mountain Foothill Cave - Cave entrance (-2199,-0808,0128)
-> Thundra Plateau Cave - Cave entrance (-2268,0899,0097)
-> Tanagar Canyon East Cave - Cave entrance (-2049,1632,-0043)
-> Satori Mountain Cave - Cave entrance (-2151,-0361,0283)
-> Crenel Peak Cave - Cave entrance (1145,0247,0069) (1350,0296,0041)
-> Luto's Channel - Cave entrance (3094,-0051,0090)
-> Oren Bridge Cave - Cave entrance (2910,-0066,0093)
""")
    await ctx.send("""
-> Tabahl Woods Cave - Cave entrance (2675,0287,0100) (2606,0227,0087) (2680,0218,0103)
-> Boné Pond East Cave - Cave entrance (2185,0142,0049) (2254,0014,0028) (2215,0100,0083) (2261,0108,0121)
-> Upland Zorana Mountainside Cave - Cave entrance (2570,0518,0173) (2634,0526,0198)
-> Upland Zorana Byroad - Cave entrance (2864,0346,0236) (2700,0480,0211)
-> Horon Lagoon Cave - Cave entrance (4244,-0256,-0004)
-> Tarm Point Cave - Cave entrance (4473,-0827,0043)
-> Ralis Channel - Cave entrance (2959,0254,0211) (2912,0170,0167)
-> Upland Zorana Summit Cave - Cave entrance (2851,0478,0331)
-> Crenel Hills Cave - Cave entrance (0494,0731,0052)
-> Rebonae Bridge Cave - Cave entrance (0846,0031,0028)
-> Reservoir Lakefront Cavern - Cave entrance (3810,0420,0218)
-> Ploymus Mountain Cave - Cave entrance (3661,0539,0276)
-> Upland Zorana Foothill Cave - Cave entrance (3147,0668,0186)
-> Cave Under Zora's Domain - Cave entrance (3241,0374,0087)
-> Lanayru Road South Cave - Cave entrance (2698,-1315,0122)
-> Mapla Point Cave - Cave entrance (4585,-2246,0010)
-> Oakle's Navel Cave - Cave entrance (2504,-2107,0019)
""")
    await ctx.send("""
-> Lanayru Road East Cave - Cave entrance (3074,-1138,0102) (3476,-0968,0004)
-> Robred Dropoff Cave - Cave entrance (2493,-1478,0024)
-> Walnot Mountain Cave - Cave entrance (4226,-1739,0189) (3934,-2069,0137)
-> Deepback Bay Cave - Cave entrance (4213,-2263,0012)
-> Cape Cales Cliffbase Cave - Cave entrance (3650,-3211,0006)
-> Retsam Forest Cave - Cave entrance (3757,-2067,0223) (3749,-2027,0199)
-> Fort Hateno Cave - Cave entrance (2243,-1690,0035)
-> Gisa Crater Cave - Cave entrance (-3866,1012,0084) (-3931,1091,0084)
-> Ancient Columns Cave - Cave entrance (-3465,0449,0262)
-> Tanagar Canyon West Cave - Cave entrance (-3308,0790,-0088)
-> Komo Shoreline Cave - Cave entrance (0487,-3831,0020)
-> Pristine Sanctum - Cave entrance (3708,0609,0349) (3622,0583,0179)
-> Ancient Zora Waterworks - Cave entrance(3607,0122,0011)  
""")
    await ctx.send("""
SKY
-> Bottomless Cave - Cave entrance (0712,-1449,1472) (0739,-1358,1527)
-> Pit Cave	- Cave entrance (0632,-1639,1469) (0587,-1625,1429)
-> Pondside Cave - Cave entrance (0171,-1634,1365) (0260,-1558,1349)
-> Mining Cave - Cave entrance (0380,-1632,1398) (0490,-1626,1356)
""")
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

@bot.command()
async def soldier_construct(ctx): 
    await ctx.send("""
    SOLDIER CONSTRUCT I
    HP: 15    ATK: 2      
    ELEMENTAL PROPERTIES: May use elemental weapons
    COMMON WEAPONS: All Zonai Weapons
    ITEM DROPS: Zonaite (Depth's only), Zonai Charge, Soldier Construct Horn, Arrow x5 (30%)(Archers only)
    TYPICAL HABITAT: Sky islands, shrines, Zonai ruins
    
    SOLDIER CONSTRUCT II
    HP: 72      ATK: 11     
    ELEMENTAL PROPERTIES: May use elemental weapons
    COMMON WEAPONS: All Zonai Weapons
    ITEM DROPS: Zonaite (Depth's only), Zonai Charge, Soldier Construct II Horn, Arrow x5 (40%)(Archers only)
    TYPICAL HABITAT: Sky islands, shrines, Zonai ruins

    SOLDIER CONSTRUCT III
    HP: 160      ATK: 27      
    ELEMENTAL PROPERTIES: May use elemental weapons
    COMMON WEAPONS: All Zonai Weapons
    ITEM DROPS: Zonaite (Depth's only), Zonai Charge, Soldier Construct III Horn, Arrow x5 (40%)(Archers only)
    TYPICAL HABITAT: Sky islands, shrines, Zonai ruins

    SOLDIER CONSTRUCT IV
    HP: 720     ATK: 42      
    ELEMENTAL PROPERTIES: May use elemental weapons
    COMMON WEAPONS: All Zonai Weapons
    ITEM DROPS: Zonaite (Depth's only), Zonai Charge, Soldier Construct IV Horn, Arrow x5 (40%)(Archers only)
    TYPICAL HABITAT: Sky islands, shrines, Zonai ruins
        """)

@bot.command()
async def captain_construct(ctx):
    await ctx.send("""

    CAPTAIN CONSTRUCT I
    HP: 80     ATK: 4     
    ELEMENTAL PROPERTIES: May use elemental weapons
    COMMON WEAPONS: All Zonai Weapons
    ITEM DROPS: Zonaite (Depth's only), Zonai Charge, Captain Construct I Horn, Arrow x5 (30%)
    TYPICAL HABITAT: Sky islands, shrines, Zonai ruins

    CAPTAIN CONSTRUCT II
    HP: 200      ATK: 15      
    ELEMENTAL PROPERTIES: May use elemental weapons
    COMMON WEAPONS: All Zonai Weapons
    ITEM DROPS: Zonaite (Depth's only), Zonai Charge, Captain Construct II Horn, Arrow x5 (40%)
    TYPICAL HABITAT: Sky islands, shrines, Zonai ruins

    CAPTAIN CONSTRUCT III
    HP: 380      ATK: 30     
    ELEMENTAL PROPERTIES: May use elemental weapons
    COMMON WEAPONS: All Zonai Weapons
    ITEM DROPS: Zonaite (Depth's only), Zonai Charge, Captain Construct III Horn, Arrow x5 (40%)
    TYPICAL HABITAT: Sky islands, shrines, Zonai ruins

    CAPTAIN CONSTRUCT IV
    HP: 1200     ATK: 36     
    ELEMENTAL PROPERTIES: May use elemental weapons
    COMMON WEAPONS: All Zonai Weapons
    ITEM DROPS: Zonaite (Depth's only), Zonai Charge, Captain Construct I Horn, Arrow x5 (40%)
    TYPICAL HABITAT: Sky islands, shrines, Zonai ruins
    """)

@bot.command()
async def bokoblin(ctx): 

@bot.command()
async def boss_bokoblin(ctx): 

@bot.command()
async def horroblin(ctx): 

@bot.command()
async def moblin(ctx): 

@bot.command()
async def lizalfos(ctx): 

@bot.command()
async def stal(ctx): 

@bot.command()
async def chcuchu(ctx): 

@bot.command()
async def like_like(ctx): 

@bot.command()
async def keese(ctx): 

@bot.command()
async def wizzrobe(ctx): 

@bot.command()
async def gibdo(ctx): 

@bot.command()
async def other_enemies(ctx): 

bot.run(settings['TOKEN'])
