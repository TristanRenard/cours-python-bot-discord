import discord


async def create_poll(question, choix, channel):
    x = "\n"
    for index in range(len(choix)):
        x += f"{index}\U000020e3 : {choix[index]}\n"

    embed = discord.Embed(title="Sondage", description=(question + x), color=0xf7f7f7)
    message = await channel.send(embed=embed)

    for index in range(len(choix)):
        await message.add_reaction(f"{index}\U000020e3")
