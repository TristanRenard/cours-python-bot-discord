import discord
from utils import getservinfo

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return


    if message.content.startswith('$get-info'):
        await getservinfo.get_server_info(message)


client.run('MTE3OTcyOTQwNzEyNDk2NzU0NA.GoxJm-.Y6RdN07PPr6WJIg2mUE5UrP5RucA2egm4sI5F8')
