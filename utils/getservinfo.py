import discord


async def get_server_info(message):
    embed = discord.Embed(title="Serveur info",
                          description="Ce serveur est un serveur pour un exercice de python dans le cadre d'un cours. "
                                      "Voici quelques commandes : \n\n"
                                      " `$get-info`  -> affiche ce message",
                          color=0xffaca6
                          )

    await message.channel.send(embed=embed)
