async def clear(channel, role, amount=-1):
    if role.id != 1179714180174069785:
        await channel.send("Vous n'avez pas la permission de faire ça !")
        return
    if amount == -1:
        await channel.purge(limit=None)
    else:
        await channel.purge(limit=amount+1)
    return
