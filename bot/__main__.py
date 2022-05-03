import discord
from discord.ext import tasks
from dotenv import load_dotenv
import os
import random

load_dotenv()
client = discord.Client()

CHANNEL_ID = 318103513047760899
HYDRATE_TIME_MINS = 20
EXERCISE = 0.5
PERFORM = ['10 Press-Ups' , '15 Sit-Ups' , '5 Burpees' , '20 Mountain Climbers' , '15 Squats' , '30 Second Plank' , '10 Squat Jumps' , '20 Lunges' , '15 Crunches' , '15 Dips' , '10 Leg Raises' , '30 Russian Twists' , '30 Second Side-Plank']
HYDRATE = ['Time To Hydrate' , 'Drink Some Water' , 'Quench That Thirst' , 'Flush Out That Liver' , 'Wet That Mouth' , 'Give That Throat Some Moisture' , 'Hit The Chug-Jug' , 'Gulp That Liquid' , 'Down That Pint' , 'Sip Some Juice']
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
    await channel.send(random.choice(HYDRATE) + ' 💦 ' + 'and do ' + random.choice(PERFORM) + ' 🏋️‍♀️')


client.run(os.getenv("TOKEN"))
