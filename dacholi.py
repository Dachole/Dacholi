import discord



client = discord.Client()


@client.event
async def on_ready():
    print(client.user.id)
    print("ready")
    game = discord.Game("당신과 즐겁게대화")
    await client.change_presence(status=discord.Status.online, activity=game)


@client.event
async def on_message(message):
    if message.content.startswith(",다쵸리메뉴얼"):
        await message.channel.send("명령어 앞에,를 붙여주세요\n대화\n안녕\n반가워\n뭐해?\n게임추천\n사랑해\n싫어해\n이름이뭐야?\n기여워\n애교부려봐\n다쵸리내거")
    if message.content.startswith("다쵸리메뉴얼"):
        await message.channel.send("명령어 앞에,를 붙여주세요\n대화\n안녕\n반가워\n뭐해?\n게임추천\n사랑해\n싫어해\n이름이뭐야?\n기여워\n애교부려봐\n다쵸리내거")
    if message.content.startswith(",안녕"):
        await message.channel.send("안녕하세요 다쵸리에요!")
    if message.content.startswith(",반가워"):
        await message.channel.send("반가워요 다쵸리에요!")
    if message.content.startswith(",뭐해?"):
        await message.channel.send("당신과 즐거운대화중!!!!")
    if message.content.startswith(",게임추천!"):
        await message.channel.send("마인크래프트!")
    if message.content.startswith(",사랑해"):
        await message.channel.send("저두요!")
    if message.content.startswith(",싫어해"):
        await message.channel.send("ㅠㅠ")
    if message.content.startswith(",이름이 뭐야?"):
        await message.channel.send("다쵸리에요!")
    if message.content.startswith(",이름이 뭐야"):
        await message.channel.send("다쵸리에요!")
    if message.content.startswith(",이름이뭐야"):
        await message.channel.send("다쵸리에요!")
    if message.content.startswith(",이름이뭐야?"):
        await message.channel.send("다쵸리에요!")
    if message.content.startswith(",취미는 뭐야?"):
        await message.channel.send("게임과 애니보는 것!")
    if message.content.startswith(",취미는 뭐야"):
        await message.channel.send("게임과 애니보는 것!")
    if message.content.startswith(",취미는뭐야?"):
        await message.channel.send("게임과 애니보는 것!")
    if message.content.startswith(",취미는뭐야"):
        await message.channel.send("게임과 애니보는 것!")
    if message.content.startswith(",기여워"):
        await message.channel.send("감사합니다!")
    if message.content.startswith(",애교부려봐"):
        await message.channel.send("다쵸리기여미")
    if message.content.startswith(",다쵸리는 내거"):
        await message.channel.send("데헷!")
    if message.content.startswith(",다쵸리 내거"):
        await message.channel.send("데헷!")
    if message.content.startswith(",다쵸리내거"):
        await message.channel.send("데헷!")
    if message.content.startswith(",디닥은 누구야?"):
        await message.channel.send("바보")
    if message.content.startswith(",나와 냥냥냥님은 누구야?"):
        await message.channel.send("바보")
    if message.content.startswith(",아레스는?"):
        await message.channel.send("정성.")



client.run("Njg0NjYwMDAzOTYxMDQ1MDAy.Xl-1UA.UCi_KRqh_qw7RR5IBMDt8RPYuGU")
