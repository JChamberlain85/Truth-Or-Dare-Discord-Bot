import discord
import random
import time
import private.py #All Private information stored here

client = discord.Client(intents=discord.Intents.default())


# Startup Information and Bot Status
@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game('*help'))
    
    print("Connected to bot: {}".format(client.user.name))
    print("Bot ID: {}".format(client.user.id))
    print("Servers: " + str(len(client.guilds)))


#Commands
@client.event
async def on_message(message):

    if message.author == client.user:
        return

    if message.content.startswith("*help"):
        embedVar = discord.Embed(title="Commands", description="Below is a list of bot commands", color=0xEEBC1D)
        embedVar.add_field(name="`*ping`", value="Tells you bot latency in milliseconds (bigger is better they say)", inline=False)
        embedVar.add_field(name="`*truth`", value="Asks a question you must answer... you know... truthfully", inline=False)
        embedVar.add_field(name="`*dare`", value="Challenges you to do something stupid", inline=False)
        embedVar.add_field(name="`*invite`", value="Sends an invite link so you can add me to your server! You can also click the giant button in my profile", inline=False)
        embedVar.add_field(name="`*server`", inline=False)
        embedVar.set_author(name=message.author.display_name, icon_url=message.author.avatar_url)
        embedVar.set_thumbnail(url="https://st3.depositphotos.com/27847728/34696/v/450/depositphotos_346961774-stock-illustration-initial-letter-logo-design-vector.jpg")
        await message.channel.send(embed=embedVar)
    
    if message.content.startswith("*truth"):
        Rtruth = random.choice(truth)
        await message.channel.send(Rtruth)

    if message.content.startswith("*dare"):
        Rdare = random.choice(dare)
        await message.channel.send(Rdare)

    if message.content.startswith("*ping"):
        before = time.monotonic()
        ping = (time.monotonic() - before) * 1000
        await message.channel.send(f"Pong! {round(client.latency * 1000)}ms")

    if message.content.startswith("*invite"):
        await message.channel.send("https://discord.com/api/oauth2/authorize?client_id=1001282224999628891&permissions=412317240384&scope=bot")

    if message.content.startswith("*server"):
        await message.channel.send(SERVER)
        
        

client.run(TOKEN)
