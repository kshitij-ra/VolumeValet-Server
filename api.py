from flask import Flask
from vol_fns import *
from threading import Thread
from werkzeug.serving import make_server

class ServerThread(Thread):
    def __init__(self, app):
        Thread.__init__(self)
        self.server = make_server('0.0.0.0', 5000, app)
        self.ctx = app.app_context()
        self.ctx.push()

    def run(self):
        self.server.serve_forever()

    def shutdown(self):
        self.server.shutdown()

def start_server():
    global server

    app = Flask(__name__)

    @app.route('/volGet',methods = ['GET'])
    def getVol():
        return str(volget())
    @app.route('/volSet/<int:vol>')
    def setVol(vol):
        volset(vol)
        return "Success"
    @app.route('/volMute/<int:s>')
    def muteVol(s):
        volmute(s)
        return "Success"
    @app.route('/getMute')
    def getMute():
        return str(getmute())
    @app.route('/next')
    def goNext():
        return str(nexttrack())
    @app.route('/prev')
    def goPrev():
        return str(prevtrack())
    @app.route('/pp')
    def pp():
        return str(playpause())
    server = ServerThread(app)
    server.daemon=True
    server.start()

def stop_server():
    global server
    server.shutdown()