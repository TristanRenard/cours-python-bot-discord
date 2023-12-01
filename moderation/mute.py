import discord


async def ban(message, member: discord.member , *, reason=None):
    if message.author.roles[1].id != 1179714180174069785:
        await message.channel.send("Vous n'avez pas la permission de faire ça !")
        return
    await member.timeout(reason=reason)
    await message.channel.send(f"{member.mention} a été mute !")
    return