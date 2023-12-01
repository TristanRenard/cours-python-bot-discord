from flask import Flask
from utils import getlogct

app = Flask(__name__)


@app.route("/")
def index():
    html = ("<head>  <meta charset='UTF-8'>  <meta name='viewport' content='width=device-width, initial-scale=1.0'>  "
            "<script src='https://cdn.tailwindcss.com'></script></head>")
    body = "<body class='bg-slate-900 text-sky-100'>"
    nav = ("<nav class='flex justify-center mb-12'><a href='/' class='mr-5'>Messages</a><a href='/ban' "
           "class='mr-5'>Ban</a><a href='/banwords' class='mr-5'>Banwords</a><a href='/clear' "
           "class='mr-5'>Clear</a><a href='/info' class='mr-5'>Info</a><a href='/sondage' class='mr-5'>Sondage</a><a "
           "href='/convert' class='mr-5'>Convert</a><a href='/chifumi' class='mr-5'>Chifumi</a></nav>")
    thead = "<thead class='border-b-4 border-indigo-500'><tr><th class='pb-5'>Author</th><th>Message</th></tr></thead>"
    tbody = "<tbody>" + str(getlogct.getlogcontent("messages.txt")) + "</tbody>"
    body+= nav
    body += "<h1 class='text-xl text-center mb-12'>Logs</h1><table class='w-full'>" + thead + tbody + "</table>"
    body += "</body>"
    html += body

    return html


@app.route("/ban")
def ban():
    html = ("<head>  <meta charset='UTF-8'>  <meta name='viewport' content='width=device-width, initial-scale=1.0'>  "
            "<script src='https://cdn.tailwindcss.com'></script></head>")
    body = "<body class='bg-slate-900 text-sky-100'>"
    nav = ("<nav class='flex justify-center mb-12'><a href='/' class='mr-5'>Messages</a><a href='/ban' "
           "class='mr-5'>Ban</a><a href='/banwords' class='mr-5'>Banwords</a><a href='/clear' "
           "class='mr-5'>Clear</a><a href='/info' class='mr-5'>Info</a><a href='/sondage' class='mr-5'>Sondage</a><a "
           "href='/convert' class='mr-5'>Convert</a><a href='/chifumi' class='mr-5'>Chifumi</a></nav>")
    thead = "<thead class='border-b-4 border-indigo-500'><tr><th class='pb-5'>Author</th><th>Message</th></tr></thead>"
    tbody = "<tbody>" + str(getlogct.getlogcontent("moderation/ban.txt")) + "</tbody>"
    body += nav
    body += "<h1 class='text-xl text-center mb-12'>Ban</h1>"
    body += "<table class='w-full'>" + thead + tbody + "</table>"
    body += "</body>"
    html += body

    return html


@app.route("/banwords")
def banwords():
    html = ("<head>  <meta charset='UTF-8'>  <meta name='viewport' content='width=device-width, initial-scale=1.0'>  "
            "<script src='https://cdn.tailwindcss.com'></script></head>")
    body = "<body class='bg-slate-900 text-sky-100'>"
    nav = ("<nav class='flex justify-center mb-12'><a href='/' class='mr-5'>Messages</a><a href='/ban' "
           "class='mr-5'>Ban</a><a href='/banwords' class='mr-5'>Banwords</a><a href='/clear' "
           "class='mr-5'>Clear</a><a href='/info' class='mr-5'>Info</a><a href='/sondage' class='mr-5'>Sondage</a><a "
           "href='/convert' class='mr-5'>Convert</a><a href='/chifumi' class='mr-5'>Chifumi</a></nav>")
    thead = "<thead class='border-b-4 border-indigo-500'><tr><th class='pb-5'>Author</th><th>Message</th></tr></thead>"
    tbody = "<tbody>" + str(getlogct.getlogcontent("moderation/ban_words.txt")) + "</tbody>"
    body += nav
    body += "<h1 class='text-xl text-center mb-12'>Banwords</h1>"
    body += "<table class='w-full'>" + thead + tbody + "</table>"
    body += "</body>"
    html += body

    return html


@app.route("/clear")
def clear():
    html = ("<head>  <meta charset='UTF-8'>  <meta name='viewport' content='width=device-width, initial-scale=1.0'>  "
            "<script src='https://cdn.tailwindcss.com'></script></head>")
    body = "<body class='bg-slate-900 text-sky-100'>"
    nav = ("<nav class='flex justify-center mb-12'><a href='/' class='mr-5'>Messages</a><a href='/ban' "
           "class='mr-5'>Ban</a><a href='/banwords' class='mr-5'>Banwords</a><a href='/clear' "
           "class='mr-5'>Clear</a><a href='/info' class='mr-5'>Info</a><a href='/sondage' class='mr-5'>Sondage</a><a "
           "href='/convert' class='mr-5'>Convert</a><a href='/chifumi' class='mr-5'>Chifumi</a></nav>")
    thead = "<thead class='border-b-4 border-indigo-500'><tr><th class='pb-5'>Author</th><th>Message</th></tr></thead>"
    tbody = "<tbody>" + str(getlogct.getlogcontent("moderation/clear.txt")) + "</tbody>"
    body += nav
    body += "<h1 class='text-xl text-center mb-12'>Clear</h1>"
    body += "<table class='w-full'>" + thead + tbody + "</table>"
    body += "</body>"
    html += body

    return html


@app.route("/info")
def info():
    html = ("<head>  <meta charset='UTF-8'>  <meta name='viewport' content='width=device-width, initial-scale=1.0'>  "
            "<script src='https://cdn.tailwindcss.com'></script></head>")
    body = "<body class='bg-slate-900 text-sky-100'>"
    nav = ("<nav class='flex justify-center mb-12'><a href='/' class='mr-5'>Messages</a><a href='/ban' "
           "class='mr-5'>Ban</a><a href='/banwords' class='mr-5'>Banwords</a><a href='/clear' "
           "class='mr-5'>Clear</a><a href='/info' class='mr-5'>Info</a><a href='/sondage' class='mr-5'>Sondage</a><a "
           "href='/convert' class='mr-5'>Convert</a><a href='/chifumi' class='mr-5'>Chifumi</a></nav>")
    thead = "<thead class='border-b-4 border-indigo-500'><tr><th class='pb-5'>Author</th><th>Message</th></tr></thead>"
    tbody = "<tbody>" + str(getlogct.getlogcontent("commands/info.txt")) + "</tbody>"
    body += nav
    body += "<h1 class='text-xl text-center mb-12'>Info</h1>"
    body += "<table class='w-full'>" + thead + tbody + "</table>"
    body += "</body>"
    html += body

    return html


@app.route("/sondage")
def sondage():
    html = ("<head>  <meta charset='UTF-8'>  <meta name='viewport' content='width=device-width, initial-scale=1.0'>  "
            "<script src='https://cdn.tailwindcss.com'></script></head>")
    body = "<body class='bg-slate-900 text-sky-100'>"
    nav = ("<nav class='flex justify-center mb-12'><a href='/' class='mr-5'>Messages</a><a href='/ban' "
           "class='mr-5'>Ban</a><a href='/banwords' class='mr-5'>Banwords</a><a href='/clear' "
           "class='mr-5'>Clear</a><a href='/info' class='mr-5'>Info</a><a href='/sondage' class='mr-5'>Sondage</a><a "
           "href='/convert' class='mr-5'>Convert</a><a href='/chifumi' class='mr-5'>Chifumi</a></nav>")
    thead = "<thead class='border-b-4 border-indigo-500'><tr><th class='pb-5'>Author</th><th>Message</th></tr></thead>"
    tbody = "<tbody>" + str(getlogct.getlogcontent("commands/sondage.txt")) + "</tbody>"
    body += nav
    body += "<h1 class='text-xl text-center mb-12'>Sondage</h1>"
    body += "<table class='w-full'>" + thead + tbody + "</table>"
    body += "</body>"
    html += body

    return html


@app.route("/convert")
def convert():
    html = ("<head>  <meta charset='UTF-8'>  <meta name='viewport' content='width=device-width, initial-scale=1.0'>  "
            "<script src='https://cdn.tailwindcss.com'></script></head>")
    body = "<body class='bg-slate-900 text-sky-100'>"
    nav = ("<nav class='flex justify-center mb-12'><a href='/' class='mr-5'>Messages</a><a href='/ban' "
           "class='mr-5'>Ban</a><a href='/banwords' class='mr-5'>Banwords</a><a href='/clear' "
           "class='mr-5'>Clear</a><a href='/info' class='mr-5'>Info</a><a href='/sondage' class='mr-5'>Sondage</a><a "
           "href='/convert' class='mr-5'>Convert</a><a href='/chifumi' class='mr-5'>Chifumi</a></nav>")
    thead = "<thead class='border-b-4 border-indigo-500'><tr><th class='pb-5'>Author</th><th>Convert</th></tr></thead>"
    tbody = "<tbody>" + str(getlogct.getlogcontent("commands/convert.txt")) + "</tbody>"
    body += nav
    body += "<h1 class='text-xl text-center mb-12'>Convert</h1>"
    body += "<table class='w-full'>" + thead + tbody + "</table>"
    body += "</body>"
    html += body

    return html


@app.route("/chifumi")
def chifumi():
    html = ("<head>  <meta charset='UTF-8'>  <meta name='viewport' content='width=device-width, initial-scale=1.0'>  "
            "<script src='https://cdn.tailwindcss.com'></script></head>")
    body = "<body class='bg-slate-900 text-sky-100'>"
    nav = ("<nav class='flex justify-center mb-12'><a href='/' class='mr-5'>Messages</a><a href='/ban' "
           "class='mr-5'>Ban</a><a href='/banwords' class='mr-5'>Banwords</a><a href='/clear' "
           "class='mr-5'>Clear</a><a href='/info' class='mr-5'>Info</a><a href='/sondage' class='mr-5'>Sondage</a><a "
           "href='/convert' class='mr-5'>Convert</a><a href='/chifumi' class='mr-5'>Chifumi</a></nav>")
    thead = "<thead class='border-b-4 border-indigo-500'><tr><th class='pb-5'>Author</th><th>Message</th></tr></thead>"
    tbody = "<tbody>" + str(getlogct.getlogcontent("commands/chifumi.txt")) + "</tbody>"
    body += nav
    body += "<h1 class='text-xl text-center mb-12'>Chifumi</h1>"
    body += "<table class='w-full'>" + thead + tbody + "</table>"
    body += "</body>"
    html += body

    return html




