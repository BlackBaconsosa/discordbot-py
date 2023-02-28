from cmath import log
from distutils.sysconfig import PREFIX
import discord
from dotenv import load_dotenv
import os
load_dotenv()

PREFIX = os.environ['PREFIX']
TOKEN = os.environ['TOKEN']

client = discord.Client()

@client.event
async def on_ready():
    print(f'Logged in as {client.user}.')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == f'{PREFIX}call':
        await message.channel.send("callback!")

    if message.content.startswith(f'{PREFIX}처리'):
        await message.channel.send('처리가 완료되었습니다! 문화상품권 지급은 몆시간, 길면 몆일 후에 지급될수 있으니 양해부탁드립니다...! (DM으로 전송됩니다!')
        
    if message.content.startswith(f'{PREFIX}랜덤숫자뽑기'):
        await message.channel.send(str(random.randrange(1,100)))


try:
    client.run(TOKEN)
except discord.errors.LoginFailure as e:
    print("Improper token has been passed.")
