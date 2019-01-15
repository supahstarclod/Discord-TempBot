import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
from datetime import datetime, date, time

Client = discord.Client()
client = commands.Bot(command_prefix = "^")

@client.event
async def on_ready():
    print("Bot is ready!")

@client.event
async def on_message(message):
    if message.content == "^ping":
        await client.send_message(message.channel, "Pong!")

###########################################################

@client.event
async def on_message(message):
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

    general_channel = get_channel(client.get_all_channels(), 'bot-test')
    gambling = get_channel(client.get_all_channels(), 'gambling')
    screencaps = get_channel(client.get_all_channels(), 'screencaps')
    
    if message.content.startswith('!stat'):
        array = message.content.split(" ")
        mesg = await client.send_message(general_channel, 'Calculating...')
        m = 1
        d = 1
        if m >= 3 and m < 11: #DST on
            aH = 6
            bH = 7
        else: #DST off
            aH = 7
            bH = 8
        flagS = False
        flagE = False
        print(datetime.utcnow())
        while m <= (12):
            while d <= int(arr[1][m - 1]):
            #while d < (3):
                ymdA = datetime(2017, m, d, aH, 59, 59)
                if flagS == True:
                    aH -= 1
                    flagS = False
                if m == 3 and d >= 8 and d <= 14 and ymdA.isoweekday() == 7:
                    bH -= 1
                    flagS = True
                    print('on')
                if flagE == True:
                    aH += 1
                    flagE = False
                if m == 11 and d >= 1 and d <= 7 and ymdA.isoweekday() == 7:
                    bH += 1
                    flagE = True
                    print('off')
                #print(ymdA)
                if d + 1 > int(arr[1][m - 1]):
                    ymdB = datetime(2017, m + 1, 1, bH, 0, 0)
                    #print(ymdB)
                else:
                    ymdB = datetime(2017, m, d + 1, bH, 0, 0)
                    #print(ymdB)
                counter = 0
                async for msg in client.logs_from(gambling, limit=30686, before=ymdB, after=ymdA, reverse=True):
                    #if msg.author.id == "172002275412279296": #tatsu
                    if msg.author.id == "206881350513459210": #clod
                        counter += 1
                print('{}/{} {}'.format(str(m), str(d), str(counter)))
                d += 1
            m += 1
            d = 1

        await client.edit_message(mesg, '{} has {} messages in #{}.'.format(message.author, str(counter), gambling))
        
        
client.run("NTE2NDc2MzAxMjcyNjc4NDI0.Dt0OSA.YyuxgPfNDMZ74krs7EllFp7AZsY")


