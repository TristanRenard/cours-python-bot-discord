def getlogcontent(file):
    with open("/Users/tristan/Desktop/Dev/python/bot-discord/cours-python-bot-discord/logs/"+file, "r") as f:
        lines = f.readlines()
        tb = ""
        for line in lines:
            tb += (f"<tr class=' border-b border-slate-800'><td class='py-5 text-center'>{line.split(' : ')[0]}</td><td class='py-5 "
                   f"text-center'>{line.split(' : ')[1]}</td></tr>")
        return tb
