import discord


async def get_server_info(message):
    embed = discord.Embed(title="Serveur info",
                          description="Ce serveur est un serveur pour un exercice de python dans le cadre d'un cours. "
                                      "Voici quelques commandes : \n\n\n \n"
                                      " `$get-info`  -> affiche ce message\n \n"
                                      " `$convert <valeur>` -> convertit la valeur en euros\n \n"
                                      " `$create-sondage <question> / <choix1> / <choix2> / ...9` -> crée un sondage\n \n"
                                      " `$chifumi <choix>` -> joue au chifumi\n \n"
                                      " `$danger` -> affiche les utilisateurs dangereux\n \n"
                                      " `$clear <nombre>` -> supprime le nombre de messages donné\n \n"
                                      "`$ban <utilisateur> <raison>` -> banni l'utilisateur donné avec la raison donnée\n \n"
                                      " `$logs` -> affiche les logs\n \n"
                                      " `$logs-file` -> envoie le fichier des logs\n \n",
                          color=0xffaca6
                          )

    await message.channel.send(embed=embed)
