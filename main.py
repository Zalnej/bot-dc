import discord
#from discord.ext import commands
import random
from datetime import datetime, time, timedelta
import asyncio

WHEN = time(20, 37, 10)
#WHEN = time(15, 22, 0)
channel_id = 1054022219099021332

with open('readme.txt', 'r', encoding='utf8', errors='ignore') as f:
    lines = f.readlines()
f.close()

class MyClient(discord.Client):
    async def on_ready(self):
       print(f'Logged on as {self.user}!')

    async def ping(ctx):
        print(len(lines))
    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')
        await client.wait_until_ready()
        if message.author == client.user:
            return

        if message.content=='start.to':
            print(len(lines))
            channel = client.get_channel(channel_id)  # Note: It's more efficient to do bot.get_guild(guild_id).get_channel(channel_id) as there's less looping involved, but just get_channel still works fine
            await channel.send("no to zaczynamy wymienianie")

            now = datetime.utcnow()
            if now.time() > WHEN:  # Make sure loop doesn't start after {WHEN} as then it will send immediately the first time as negative seconds will make the sleep yield instantly
                tomorrow = datetime.combine(now.date() + timedelta(days=1), time(0))
                seconds = (tomorrow - now).total_seconds()  # Seconds until tomorrow (midnight)
                print(seconds)
                await asyncio.sleep(seconds)  # Sleep until tomorrow and then the loop will start

            while True:
                now = datetime.utcnow()
                t=now.time()

                n=random.randrange(1, len(lines))
                #if now.time() > WHEN:
                x=lines[n]

                target_time = datetime.combine(now.date(), WHEN)
                seconds_until_target = (target_time - now).total_seconds()
                print(seconds_until_target)

                seconds_until_target=5

                await asyncio.sleep(seconds_until_target)

                print('A cytat na dziś to:\n'+x)
                v='A cytat na dziś to:\n'+x
                #await channel.send('Dziś jest:')
                #await channel.send(now.date())
                #await channel.send('A cytat na dziś to:')
                #await channel.send(x)
                await channel.send(v)

                tomorrow = datetime.combine(now.date() + timedelta(days=1), time(0))
                seconds = (tomorrow - now).total_seconds()
                print(seconds)

                seconds=5

                await asyncio.sleep(seconds)

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run('MTAzNzA2MzM2MTcxNzg3ODg1NA.G0VKb5.T731nxpQMVCtw2whan5qd0_N6j7pFY0h2s9-8I')


