import discord
#from discord.ext import commands
import random
from datetime import datetime, time, timedelta
import asyncio
from PIL import Image, ImageDraw, ImageFont

WHEN = time(20, 37, 10)
channel_id = 1054022219099021332

def daj_cytat(lines):
    o = 0
    while o < 1:
        o = 1
        n = random.randrange(1, len(lines))
        k = 0

        # while k<15:

        for k in range(len(wyj)):
            s = wyj[k]
            # k = k + 1
            if n == s:
                o = 0
    x = lines[n]
    w = 'nie ma'
    if n >= kasztan1:
        w = '~Kasztan'
        if n >= szycha1:
            w = '~Szycha'
            if n >= tomek1:
                w = '~Tomek'
                if n >= mati1:
                    w = '~KeroY'
                    if n >= filip1:
                        w = '~Cerber'
                        if n >= vexors1:
                            w = '~Vexors'
                            if n >= patryk1:
                                w = '~Imraael'
                                if n >= magda1:
                                    w = '~Magda'
                                    if n >= oski1:
                                        w = '~Oski'
                                        if n >= janek1:
                                            w = '~Janek'
                                            if n >= marcin1:
                                                w = '~Marcin'
                                                if n >= rafu1:
                                                    w = '~Rafu'
                                                    if n >= wyko1:
                                                        w = '~Wyko'
                                                        if n >= bartek1:
                                                            w = '~Bartek'
                                                            if n >= randomy1:
                                                                w = '~Randomy'
    return w,x

def cycat(text,w):

    font = ImageFont.truetype('arial.ttf', 37)
    image = Image.open('cytat.jpg')
    draw = ImageDraw.Draw(image)
    line_width = 800  # Maximum width of a line in pixels
    lines = []
    for line in text.split('\n'):
        line_words = line.split(' ')
        i = 0
        while i < len(line_words):
            # Try adding words to the line until it is full
            line_text = line_words[i]
            i += 1
            while i < len(line_words) and draw.textsize(line_text + ' ' + line_words[i], font=font)[0] < line_width:
                line_text += ' ' + line_words[i]
                i += 1
            lines.append(line_text)
            #print(line_text)
        # Calculate the position of the first line of text
        text_width, text_height = draw.textsize(lines[0], font=font)
        x = (image.width - text_width) / 2
        y = (image.height - text_height * len(lines)) / 2

        # Draw each line of text on the image
        for line in lines:
            draw.text((x, y), line, font=font, fill=(255, 0, 0))
            y += text_height
        font = ImageFont.truetype('arial.ttf', 45)
        draw.text((1100, 700), w, font=font, fill=(255, 0, 0))
        # Save the modified image to a different file
        image.save('cytat_p.jpg')
        return 0

def hujowy_kometarz(kometarze):
    n = random.randrange(1, len(kometarze))
    v = kometarze[n]
    return v

def logi(log):
    with open('logi.txt', 'a', encoding='utf8', errors='ignore') as h:
        h.write("\n")
        h.write(log)
    h.close()

with open('readme.txt', 'r', encoding='utf8', errors='ignore') as h:
    lines = h.readlines()
h.close()
with open('kometarze.txt', 'r', encoding='utf8', errors='ignore') as g:
    kometarze = g.readlines()
g.close()

kasztan1=0
wyj=[]

for i in range(len(lines)):
    #print(lines[i])
    #l=lines[i]
    #m=to_string(l)
    if lines[i]=='szycha\n':
        kasztan2=i-1
        szycha1=i+1
        wyj.append(i)
    if lines[i] == 'tomek\n':
        szycha2=i-1
        tomek1=i+1
        wyj.append(i)
    if lines[i] == 'mati\n':
        tomek2=i-1
        mati1=i+1
        wyj.append(i)
    if lines[i] == 'filip\n':
        mati2=i-1
        filip1=i+1
        wyj.append(i)
    if lines[i] == 'vexors\n':
        filip2=i-1
        vexors1=i+1
        wyj.append(i)
    if lines[i] == 'patryk\n':
        vexors2=i-1
        patryk1=i+1
        wyj.append(i)
    if lines[i] == 'magda\n':
        patryk2=i-1
        magda1=i+1
        wyj.append(i)
    if lines[i] == 'oski\n':
        magda2=i-1
        oski1=i+1
        wyj.append(i)
    if lines[i] == 'janek\n':
        oski2=i-1
        janek1=i+1
        wyj.append(i)
    if lines[i] == 'marcin\n':
        janek2 = i - 1
        marcin1 = i + 1
        wyj.append(i)
    if lines[i] == 'rafu\n':
        marcin2=i-1
        rafu1=i+1
        wyj.append(i)
    if lines[i] == 'wyko\n':
        rafu2=i-1
        wyko1=i+1
        wyj.append(i)
    if lines[i] == 'bartek\n':
        wyko2=i-1
        bartek1=i+1
        wyj.append(i)
    if lines[i] == 'randomy\n':
        bartek2=i-1
        randomy1=i+1
        wyj.append(i)
    if lines[i] == 'koniec\n':
        randomy2=i-1
        wyj.append(i)

class MyClient(discord.Client):
    async def on_ready(self):
       print(f'Logged on as {self.user}!')

    async def ping(ctx):
        print('piszę sobie cos')
    async def on_message(self, message):
        #print(f'Message from {message.author}: {message.content}')
        log=f'{message.author}: {message.content}'
        logi(log)
        now = datetime.utcnow()
        #print(f'Message from {message.author}: {message.content}')
        #print(now)
        await client.wait_until_ready()
        if message.author == client.user:
            return
        if  client.user in message.mentions:
            # The bot was mentioned in the message
            #print('zostałem spingowany')
            kto_napisal, tekst = daj_cytat(lines)
            cycat(tekst, kto_napisal)
            await message.channel.send(file=discord.File('cytat_p.jpg'))

        if message.content=='start.to1': #and message.author=='Zalnej#2706':
            print(len(lines))
            g=message.author
            #print(g)
            print('weszłem')

            channel = client.get_channel(channel_id)  # Note: It's more efficient to do bot.get_guild(guild_id).get_channel(channel_id) as there's less looping involved, but just get_channel still works fine
            #await channel.send("no to zaczynamy wymienianie")

            now = datetime.utcnow()
            print(now)
            if now.time() > WHEN:  # Make sure loop doesn't start after {WHEN} as then it will send immediately the first time as negative seconds will make the sleep yield instantly
                tomorrow = datetime.combine(now.date() + timedelta(days=1), time(0))
                seconds = (tomorrow - now).total_seconds()  # Seconds until tomorrow (midnight)
                print(seconds)
                await asyncio.sleep(seconds)  # Sleep until tomorrow and then the loop will start

            while True:
                now = datetime.utcnow()
                t=now.time()



                #if now.time() > WHEN:
                kto_napisal,tekst=daj_cytat(lines)

                target_time = datetime.combine(now.date(), WHEN)
                seconds_until_target = (target_time - now).total_seconds()


                #seconds_until_target=5
                print(seconds_until_target)

                await asyncio.sleep(seconds_until_target)

                #print('A cytat na dziś to:\n'+x)
                #v='A cytat na dziś to:\n'+x
                #await channel.send('Dziś jest:')
                #await channel.send(now.date())
                await channel.send('A cytat na dziś to:')
                #await channel.send(x)
                cycat(tekst,kto_napisal)
                #await channel.send(v)

                await channel.send(file=discord.File('cytat_p.jpg'))

                kom=hujowy_kometarz(kometarze)
                await channel.send(kom)
                #await channel.send(w)
                tomorrow = datetime.combine(now.date() + timedelta(days=1), time(0))
                seconds = (tomorrow - now).total_seconds()


                #seconds=5
                print(seconds)

                await asyncio.sleep(seconds)

intents = discord.Intents.default()
intents.message_content = True
with open('token1.txt', 'r', encoding='utf8', errors='ignore') as f:
    xd = f.readlines()

f.close()
client = MyClient(intents=intents)
client.run(xd[0])


