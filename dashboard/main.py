from flask import Flask
from utils import getlogct

app = Flask(__name__)


@app.route("/")
def test():
    html = ("<head>  <meta charset='UTF-8'>  <meta name='viewport' content='width=device-width, initial-scale=1.0'>  "
            "<script src='https://cdn.tailwindcss.com'></script></head>")
    body = "<body class='bg-slate-900 text-sky-100'><h1 class='text-xl text-center mb-12'>Logs</h1>"
    thead = "<thead class='border-b-4 border-indigo-500'><tr><th class='pb-5'>Author</th><th>Message</th></tr></thead>"
    tbody = "<tbody>" + str(getlogct.getlogcontent("messages.txt")) + "</tbody>"
    body += "<table class='w-full'>" + thead + tbody + "</table>"
    body += "</body>"
    html += body

    return html
