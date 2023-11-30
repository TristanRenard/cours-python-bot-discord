import discord
from utils import getservinfo,salutation

intents = discord.Intents.default()
intents.message_content = True
intents.members = True  # Activer les événements liés aux membres

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

server-info
    if message.content.startswith('$get-info'):
        await getservinfo.get_server_info(message)

@client.event
async def on_member_join(member):
    await salutation.salutation(client,member)

client.run('MTE3OTcxMzQyNTE0OTAxODExMg.GNV-7P.kKgSUZKbGKsa9yoXZr8UOWjm15Wc8E27zt8ds0')
