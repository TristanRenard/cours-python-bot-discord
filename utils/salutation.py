async def salutation(client, member):
    channel = client.get_channel(1179728507828445265)

    if channel is not None:
        await channel.send(f'Bienvenue {member.mention} sur le serveur!')
