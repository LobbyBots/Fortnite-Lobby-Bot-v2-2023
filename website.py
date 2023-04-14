from flask import Flask, redirect
from replit import web
import logging
logging.getLogger('werkzeug').setLevel(logging.ERROR)

app = Flask(__name__)

@app.route('/')
def home():
    return redirect("https://lobbybots.ga/commands", code=302)

print('\033[36m' + "Add the link thats at the top of the Client Commands window to https://uptimerobot.com/ to keep your bot online 24/7!" + '\033[0m')

if __name__ == '__main__':
    web.run(app)
