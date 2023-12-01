from random import randint


async def chifumi(message, client):
    ppc = ["pierre", "papier", "ciseaux"]
    bot = ppc[randint(0, 2)]
    await message.channel.send("Pierre, papier, ciseaux !")
    msg = await client.wait_for('message', check=lambda m: m.author == message.author)
    player = msg.content
    if player == bot:
        await message.channel.send("Egalité !")
    elif player == "pierre":
        if bot == "ciseaux":
            await message.channel.send("Tu as gagné !")
        else:
            await message.channel.send("Tu as perdu !")
    elif player == "papier":
        if bot == "pierre":
            await message.channel.send("Tu as gagné !")
        else:
            await message.channel.send("Tu as perdu !")
    elif player == "ciseaux":
        if bot == "papier":
            await message.channel.send("Tu as gagné !")
        else:
            await message.channel.send("Tu as perdu !")
    else:
        await message.channel.send("Ce mot n'est pas valide !")
