import discord
from utils import getservinfo,salutation,sondage

intents = discord.Intents.default()
intents.message_content = True
intents.members = True  # Activer les événements liés aux membres

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

    channel = client.get_channel(1179712383476842508)

    question = "Quel est votre choix ?"
    choix = ["Option 1", "Option 2"]
    await sondage.create_poll(question, choix, channel)


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$get-info'):
        await getservinfo.get_server_info(message)
    elif message.content.startswith('get-sondage'):
        content = message.content.split(' / ')
        question = content[1]
        choix = content[2::]
        await sondage.create_poll(question,choix, message.channel)



@client.event
async def on_member_join(member):
    await salutation.salutation(client,member)

client.run('MTE3OTcxMzQyNTE0OTAxODExMg.GNV-7P.kKgSUZKbGKsa9yoXZr8UOWjm15Wc8E27zt8ds0')
