from flask import Flask, redirect, render_template
from config import *
from flask_login import (
    LoginManager,
    current_user,
    login_required,
    login_user,
    logout_user,
)


class WebUI:
    def __init__(self, name, host='0.0.0.0', port='8080'):
        self.app = Flask(name)
        self.host = host
        self.port = port
        self.app.config["TEMPLATES_AUTO_RELOAD"] = True
    
        @self.app.route('/')
        def __index():
            return self.index()

        @self.app.route('/api/login', methods=['POST'])
        def __login_api():
            return self.login_api()
        
        @self.app.route('/api/login')
        def __login():
            return self.login()
    
    def index(self):
        return render_template("login.html")

    def login_api(self):
        pass

    
    def run(self):
        self.app.run(host=self.host, port=self.port)

if __name__ == "__main__":
    web = WebUI(__name__, host=FLASK_HOST, port=FLASK_PORT)
    web.run()
