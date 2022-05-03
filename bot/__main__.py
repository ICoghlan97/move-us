import discord
from discord.ext import tasks
from dotenv import load_dotenv
import os

load_dotenv()
client = discord.Client()

CHANNEL_ID = 318103513047760899
HYDRATE_TIME_MINS = 20


@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))
    hydrate_alert.start()


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("$hello"):
        await message.channel.send("Hello!")


@tasks.loop(minutes=HYDRATE_TIME_MINS)
async def hydrate_alert():
    channel = client.get_channel(CHANNEL_ID)
    await channel.send("Hydrate, Bozo 💦")


client.run(os.getenv("TOKEN"))
