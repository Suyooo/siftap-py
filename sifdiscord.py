import discord, siftap, time

accepting = True
last = 0
delay = 0.005

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        global accepting, last, delay
        if message.channel and message.channel.id == 208004429826228224:
            if message.author.id == 81125477607014400:
                if message.content == "on": accepting = True
                elif message.content == "off": accepting = False
            if accepting:
                if len(message.content) > 2 or len(message.content) == 0: return
                if len(message.content) > 1 and not message.content[0] == message.content[1]: return
                o = ord(message.content[0]) - ord("0")
                if o < 1 or o > 9: return
                
                if time.time() - last < delay: return
                last = time.time()
                if len(message.content) == 1: siftap.tap(o)
                else: siftap.hold(o)

intents = discord.Intents(messages=True, guilds=True)

client = MyClient(intents=intents)
client.run('cool bot token')
