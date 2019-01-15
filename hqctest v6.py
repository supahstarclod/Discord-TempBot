import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
from datetime import datetime, date, time

Client = discord.Client()
client = commands.Bot(command_prefix = "^")

#@client.event
#async def on_ready():
    #print("Bot is ready!")

###########################################################

@client.event
async def on_ready():
#async def on_message(message):
    #if message.content == "^ping":
        #await client.send_message(message.channel, "Pong!")
    #-------------------------
    def get_channel(channels, channel_name):
        count = 0
        for channel in client.get_all_channels():
            if channel.name == channel_name:
                if count == 0:
                    return channel
        count += 1
        return message.channel
    #-------------------------
    arr = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]]

    owners_only = get_channel(client.get_all_channels(), 'owners_only')
    general = get_channel(client.get_all_channels(), 'general')
    
    #if message.content.startswith('^stats'):
    if True:
        #mesg = await client.send_message(owners_only, 'Calculating...') #
        
        m = 4
        d = 22
        y = 2017
        
        #array = message.content.split(" ")
        #if not len(arr) == 1:
            #m = int(array[1])
            #d = int(array[2])
            #y = int(array[3]) + 2000
        month = m
        day = d
        year = y
        if m >= 3 and m < 11: #DST on
            aH = 6
            bH = 7
        else: #DST off
            aH = 7
            bH = 8
        flagS = False
        flagE = False
        flag = False
        total = 0
        print(datetime.utcnow())
        while m <= (12):
            while d <= int(arr[1][m - 1]):
            #while d < (3):
                ymdA = datetime(y, m, d, aH, 59, 59)
                if flagS == True:
                    aH -= 1
                    flagS = False
                if m == 3 and d >= 8 and d <= 14 and ymdA.isoweekday() == 7:
                    bH -= 1
                    flagS = True
                    #print('on')
                if flagE == True:
                    aH += 1
                    flagE = False
                if m == 11 and d >= 1 and d <= 7 and ymdA.isoweekday() == 7:
                    bH += 1
                    flagE = True
                    #print('off')
                #print(ymdA)
                if m == 12 and d == 31:
                    if y == 2018:
                        m = 13
                        ymdB = datetime(2019, 1, 1, bH, 0, 0)
                    else:
                        ymdB = datetime(y + 1, 1, 1, bH, 0, 0)
                elif d + 1 > int(arr[1][m - 1]):
                    ymdB = datetime(y, m + 1, 1, bH, 0, 0)
                    #print(ymdB)
                else:
                    ymdB = datetime(y, m, d + 1, bH, 0, 0)
                    #print(ymdB)
                counter = 0
                warria = 0
                louie = 0
                grord = 0
                wario = 0
                resh = 0
                floor = 0
                bumb = 0
                cclod = 0
                newguy = 0
                bright = 0
                waffles = 0
                zoom = 0
                reach = 0
                caffie = 0
                async for msg in client.logs_from(general, limit=3000000, before=ymdB, after=ymdA, reverse=True):
                    #if msg.author.id == "172002275412279296": #tatsu
                    if msg.author.id == "216291435287150592": #scoobs
                        warria += 1
                    if msg.author.id == "257628832016760835": #takeshi
                        louie += 1
                    if msg.author.id == "272510372441882637": #skiff
                        grord += 1
                    if msg.author.id == "195732311046619136": #bored
                        wario += 1
                    if msg.author.id == "231583299007545345": #knight
                        resh += 1
                    if msg.author.id == "170632068571725825": #thomas
                        floor += 1
                    if msg.author.id == "221289975843389440": #trifly
                        bumb += 1
                    if msg.author.id == "195735680196804609": #spaceman
                        cclod += 1
                    if msg.author.id == "158742705470570505": #fetus
                        newguy += 1
                    if msg.author.id == "304369656188370954": #pablo
                        bright += 1
                    if msg.author.id == "153542331335704576": #pop
                        waffles += 1
                    if msg.author.id == "212990272517308416": #guymane
                        zoom += 1
                    if msg.author.id == "284096433131487232": #beck
                        reach += 1
                    if msg.author.id == "207496001471250432": #caffie
                        caffie += 1
                    counter = warria + louie + grord + wario + resh + floor + bumb + cclod + newguy + bright + waffles + zoom + reach + caffie
                    total += counter
                #print('{}/{}/{} {}'.format(str(m), str(d), str(y - 2000), str(counter)))
                print('{}/{}/{} {} {} {} {} {} {} {} {} {} {} {} {} {} {} | {}'.format(str(m), str(d), str(y - 2000), str(warria), str(louie), str(grord), str(wario), str(resh), str(floor), str(bumb), str(cclod), str(newguy), str(bright), str(waffles), str(zoom), str(reach), str(caffie), str(counter)))
                if m == 12 and d == 31 and y != 2018:
                    m = 0
                    flag = True
                d += 1
            m += 1
            d = 1
            if flag == True:
                y += 1
                flag = False
        print ('total: {}'.format(str(total)))
        #await client.edit_message(mesg, '{} has {} messages in #{} from {}/{}/{} to 1/1/19.'.format(message.author, str(total), owners_only, str(month), str(day), str(year))) #
        


client.run("NTE2NDc2MzAxMjcyNjc4NDI0.DvcQRA.52QaEmm24OsY6A-SLxa2NzC08Lg")


