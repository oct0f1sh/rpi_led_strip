from flask import Flask
import threading

class ServerThread(threading.Thread):
    threading.Thread.__init__(self)
    
    self.app = Flask(__name__)

    def run(ip):
        self.app.run(ip)

thread = ServerThread()
thread.run()

@thread.app.route('/nice')
def thing():
    return 'nice'
