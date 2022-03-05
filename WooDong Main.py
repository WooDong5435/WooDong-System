import numbers
from re import purge
import discord
import datetime
import pytz
import asyncio
## ─────────────────────────────────────────────────────────────────────────────────────────────────── ↑ 위 모듈

client = discord.Client()
token = "OTQwNTYyMTE2OTUwMjQ5NTMz.YgJMuw.40Ck0ulBw0CJUjjr92dblD1x5cY"
## ─────────────────────────────────────────────────────────────────────────────────────────────────── ↑ 위 토큰 로그인

@client.event
async def on_ready():
## ─────────────────────────────────────────────────────────────────────────────────────────────────── ↑ 위 준비단계 1

    print(client.user.name)
    print('시스템 정상적으로 구동되었습니다.')
    game = discord.Game("도움말 >시스템 설명서")
    await client.change_presence(status=discord.Status.online, activity=game)
## ─────────────────────────────────────────────────────────────────────────────────────────────────── ↑ 위 준비단계 2

@client.event
async def on_message(message):
    if message.content == "어쩔티비":
        await message.channel.send("저쩔티비")
## ─────────────────────────────────────────────────────────────────────────────────────────────────── ↑ 위 응답메세지

    if message.content == "김우동":
        embed = discord.Embed(title="김우동 유튜브 채널", description="https://www.youtube.com/channel/UClkcb8Yy_NdIrnOZBaeE51A", color=0x00ff00)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/697495165023027202/948880177352552458/ee967737784984f3.png")
        embed.add_field(name="AURA SERVER", value="AURA VLOG VIDEO",inline=True)
        embed.set_footer(text="WooDong")
        await message.channel.send(embed=embed)
## ─────────────────────────────────────────────────────────────────────────────────────────────────── ↑ 위 김우동 유튜브 채널(임베드)

    if message.content.startswith(">청소"):
        number = int(message.content.split(" ")[1])
        await message.delete()
        await message.channel.purge(limit=number)
        await message.channel.send(f"{number}개의 메세지 삭제 완료!")
## ─────────────────────────────────────────────────────────────────────────────────────────────────── ↑ 위 디스코드 메세지 삭제

    ## if message.content.startswith(">추방"):
        ## member = message.guild.get_member(int(message.content.split(" ")[1]))
        ## await message.guild.kick(member, reason=' '.join(message.content.split(" ")[2:]))a

    if message.content == '>내정보':
        user = message.author
        date = datetime.datetime.utcfromtimestamp(((int(user.id) >> 22) + 1420070400000) / 1000)
        await message.channel.send(f"{message.author.mention}의 가입일 : {date.year}/{date.month}/{date.day}")
        await message.channel.send(f"{message.author.mention}의 이름 / 아이디 / 닉네임 : {user.name} / {user.id} / {user.display_name}")
        ## await message.channel.send(message.author.avater_url)
## ─────────────────────────────────────────────────────────────────────────────────────────────────── ↑ 위 디스코드 내정보

    if message.content == ">시스템 설명서":
        embed = discord.Embed(colour=discord.Colour.red(), title="김우동 시스템 설명서", descripttion="올바른 우동이 사용방법")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/697495165023027202/948880177352552458/ee967737784984f3.png")
    #error    # embed.set_image("https://cdn.discordapp.com/attachments/697495165023027202/948880177352552458/ee967737784984f3.png")
    #error    # embed.set_footer(text=message.author, icon_url=message.author.avater_url)
        embed.add_field(name="응답메세지", value="**```우동아 / 김우동```**", inline=True)
        embed.add_field(name="관리자", value="```>청소 / >추방```", inline=True)
        embed.add_field(name="유저", value="**```우동아 / 김우동 / >내정보```**", inline=True)
        embed.add_field(name="시스템", value="**```>시스템 설명서```**", inline=True)
        await message.channel.send(embed=embed)
## ─────────────────────────────────────────────────────────────────────────────────────────────────── ↑ 위 김우동 시스템 설명서













































client.run(token)
