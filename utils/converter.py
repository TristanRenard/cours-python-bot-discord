import requests
import discord
import json


async def convert(channel, val=1):
    conv = ""
    req = json.loads(requests.get('https://cdn.taux.live/api/ecb.json').content)
    m = float(val) / req.get("rates").get('EUR')
    for k, v in req.get("rates").items():
        conv += (k + " -> " + str(round(v * m, 2)) + "\n")

    embed = discord.Embed(title=f"Convert {val}€",
                          description=conv,
                          color=0xff2600)
    await channel.send(embed=embed)
