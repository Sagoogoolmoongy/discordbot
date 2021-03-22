import discord
import os

client = discord.Client()


@client.event
async def on_ready():
    print(client.user.id)
    print("디스코드 봇 실행 성공!")
    game = discord.Game("사구굴뭉이 봇")
    await client.change_presence(status=discord.Status.online, activity=game)



@client.event
async def on_message(message):
    if message.content.startswith("!안녕"):
        await message.channel.send("안녕하세요 사구굴뭉이 봇입니다")


acces_token = os.environ["BOT_TOKEN"]
client.run("acces_token")

