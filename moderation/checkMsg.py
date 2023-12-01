async def check_msg(message, ban_words):
    for word in ban_words:
        if word in message.content:
            await message.delete()
            await message.channel.send(f"{message.author.mention} tu n'as pas le droit d'envoyer ce message ici !")
            with open("logs/moderation/ban_words.txt", "a") as f:
                f.write(f"{message.author} : {message.content}\n")
            return
