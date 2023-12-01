import discord


async def danger(message: discord.Message):
    with open("logs/moderation/ban_words.txt", "r") as f:
        dico = {}
        lines = f.readlines()
        for line in lines:
            author = line.split(' : ')[0]
            if author in dico:
                dico[author] += 1
            else:
                dico[author] = 1

    ranking = []
    for author, ct in dico.items():
        ranking.append((author, ct))

    ranking.sort(key=lambda x: x[1], reverse=True)

    ranked = ''
    for i in ranking[:10]:
        ranked += f"{i[0]} : {i[1]}\n"

    embed = discord.Embed(title="Classement des plus gros danger du serveur"
                          , description=ranked
                          , color=0xff2600)

    await message.channel.send(embed=embed)
