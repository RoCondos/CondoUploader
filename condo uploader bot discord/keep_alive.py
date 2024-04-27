from flask import Flask
from threading import Thread

app = Flask('condo-alive')

@app.route('/')
def main():
    return "BOT > I am alive!"

def run():
    app.run(host="0.0.0.0", port=8080)

def keep_alive():
    server = Thread(target=run)
    server.start()
