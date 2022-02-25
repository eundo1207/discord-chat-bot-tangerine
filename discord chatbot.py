import asyncio, discord
client = discord.Client()
from discord.ext import commands
client = commands.Bot(command_prefix="!")


@client.event
async def on_ready():
    print(client.user.id)
    print("성공적으로 봇이 구동되었습니다!")
    game = discord.Game("신나린을 사랑")
    await client.change_presence(status=discord.Status.online, activity=game)




@client.event
async def on_message(message):
    if message.content.startswith("!안녕"):
       await message.channel.send("안녕하세요!")

    if message.content.startswith("!바보"):
       await message.channel.send("응 아니야")

    if message.content.startswith("!사랑해"):
       await message.channel.send("저도요!")

    if message.content.startswith("!좋아해"):
       await message.channel.send("저도요!")

    if message.content.startswith("!노래"):
        await message.channel.send("노래 재생은 할 수 없어요!")

    if message.content.startswith("!싫어"):
        await message.channel.send("나도 너 싫어")

    if message.content.startswith("!개똥 멍청이"):
        await message.channel.send("점심쨩")

    if message.content.startswith("!결혼하자"):
        await message.channel.send("부케는 누가 받을까?")

    if message.content.startswith("!귤 까"):
        await message.channel.send("싫어")

    if message.content.startswith("!주사위"):
        await message.channel.send("그 기능은 아직 구동되지 않이요!")

    if message.content.startswith("!도박"):
        await message.channel.send("도박 중독 치료 센터는 1336")

    if message.content.startswith("!학원"):
        await message.channel.send("풉 ㅋ 가다가 넘어져라 깔깔깔")

    if message.content.startswith("!여자친구"):
        await message.channel.send("넌 없잖앙 ㅋ")

    if message.content.startswith("!여친"):
        await message.channel.send("넌 없잖앙 ㅋ")

    if message.content.startswith("!남자친구"):
        await message.channel.send("넌 없잖앙 ㅋ")

    if message.content.startswith("!남친"):
        await message.channel.send("넌 없잖앙 ㅋ")

    if message.content.startswith("!친구"):
        await message.channel.send("넌 없잖앙 ㅋㅋㅋㅋㅋㅋ")

    if message.content.startswith("!유선월"):
        await message.channel.send("!내가 사랑하는 주인님")

    if message.content.startswith("!허브"):
        await message.channel.send("부마들 괴롭히는 나쁜 악당")

    if message.content.startswith("!공부"):
        await message.channel.send("그게 뭐죠? 먹는 건가요?")



client.run("OTQ2MzM2Nzg5NzA5MzI4NDA1.YhdO0A.2rdALTE_dkOu_q-emiDMwOUD0f8")