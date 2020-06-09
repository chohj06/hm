

import discord
import os


client = discord.Client()

@client.event
async def on_ready():
    print(client.user.id)
    print("ready")
    game = discord.Game("일")
    await client.change_presence(status=discord.Status.online, activity=game)


@client.event
async def on_message(message):
    if message.content.startswith("!구독"):
        await message.channel.send("https://www.youtube.com/channel/UCLCn7P6JHwacN7owSR_uS1g?sub_confirmation=1")


@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'안녕 {member.name}님, 구독 해주세요! https://www.youtube.com/channel/UCLCn7P6JHwacN7owSR_uS1g?sub_confirmation=1'
    )






access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
