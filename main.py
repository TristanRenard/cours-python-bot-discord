import discord
from utils import getservinfo, salutation, sondage, chifumi, converter
from moderation import checkMsg, clear, ban, danger

prefix = '$'

intents = discord.Intents.default()
intents.message_content = True
intents.members = True  # Activer les événements liés aux membres

client = discord.Client(intents=intents)

ban_words = ["TS", "typescript", "TypeScript", " ts ", "typescript", ]


@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')


@client.event
async def on_message(message: discord.Message):
    with open("logs/messages.txt", "a") as f:
        f.write(f"{message.author} : {message.content}\n")
    await checkMsg.check_msg(message, ban_words)
    if message.author == client.user:
        return
    if message.content.startswith(prefix + 'get-info'):
        await getservinfo.get_server_info(message)
        with open("logs/commands/info.txt", "a") as f:
            f.write(f"{message.author} : {message.content}\n")
    elif message.content.startswith(prefix + 'convert'):
        ct = message.content.split(" ")
        await converter.convert(message.channel, ct[1])
        with open("logs/commands/convert.txt", "a") as f:
            f.write(f"{message.author} : convert -> {ct[1]}\n")
    elif message.content.startswith(prefix + 'create-sondage'):
        content = message.content.split(' / ')
        question = content[1]
        choix = content[2:12]
        await sondage.create_poll(question, choix, message.channel)
        with open("logs/commands/sondage.txt", "a") as f:
            f.write(f"{message.author} : {message.content}\n")

    elif message.content.startswith(prefix + 'clear'):
        content = message.content.split(' ')
        try:
            await clear.clear(message.channel, message.author.roles[1], int(content[1]))
        except IndexError:
            await clear.clear(message.channel, message.author.roles[1])
        with open("logs/moderation/clear.txt", "a") as f:
            f.write(f"{message.author} : {message.content}\n")
    elif message.content.startswith(prefix + 'ban'):
        content = message.content.split(' ')
        try:
            try:
                await ban.ban(message, message.mentions[0], reason=content[2])
            except:
                await ban.ban(message, message.mentions[0])
        except IndexError:
            await message.channel.send("Vous devez mentionner un utilisateur !")
        with open("logs/moderation/ban.txt", "a") as f:
            f.write(f"{message.author} : {message.content}\n")
    elif message.content.startswith(prefix + 'chifumi'):
        await chifumi.chifumi(message, client)
        with open("logs/commands/chifumi.txt", "a") as f:
            f.write(f"{message.author} : {message.content}\n")
    elif message.content.startswith(prefix + 'danger'):
        await danger.danger(message)
    elif message.content.startswith(prefix + 'logs-file'):
        await message.channel.send(file=discord.File('logs/messages.txt'))
    elif message.content.startswith(prefix + 'logs'):
        embed = discord.Embed(title="Logs", description="Voici les logs", url="http://127.0.0.1:5000/", color=0xf7f7f7)
        await message.channel.send(embed=embed)


@client.event
async def on_member_join(member):
    await salutation.salutation(client, member)


def run_discord():
    client.run('MTE3OTcyOTQwNzEyNDk2NzU0NA.Gz2fFe.DeqOYSdpftrRlGOMFOycy6RMPuJi8tX0d47RE4')


run_discord()
