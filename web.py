from flask import Flask, redirect, render_template, jsonify, request
from config import *
from models import LoginnedUserModel
from db import DbManager
from flask_login import (
    LoginManager,
    current_user,
    login_required,
    login_user,
    logout_user,
)


class WebUI:
    def __init__(self, name, db_manager, host='0.0.0.0', port='8080'):
        self.app = Flask(name)
        self.host = host
        self.port = port
        self.app.config["TEMPLATES_AUTO_RELOAD"] = True
        self.db_manager = db_manager
        self.login_manager = LoginManager(self.app)
        self.app.config['SECRET_KEY'] = SECRET_KEY

        # UI

        @self.app.route('/')
        def __index():
            return self.index()

        @self.app.route('/login')
        def __login():
            return self.login()

        # API

        @self.app.route('/api/login', methods=['POST'])
        def __login_api():
            return self.login_api()

        @self.app.route('/api/logout')
        def __logout():
            return self.logout()


        # utility
        @self.login_manager.user_loader
        def load_user(user_id: str):
            return LoginnedUserModel.get(user_id)

        
    
    def index(self):
        if not current_user.is_authenticated:
            return redirect("/login")
        else:
            all_machines = self.db_manager.get_machines()
            return render_template("index.html", all_machines=all_machines)
        
    def login(self):
        if not current_user.is_authenticated:
            return render_template("login.html")
        else:
            return redirect("/")

    def logout(self):
        logout_user()
        return redirect('/login')


    def login_api(self):
        correct = self.db_manager.check_password(request.form.get('password'))
        if correct:
            login_user(LoginnedUserModel(1))
        return jsonify({"status": correct})

    
    def run(self):
        self.app.run(host=self.host, port=self.port)

if __name__ == "__main__":
    db_manager = DbManager("./data/db.sqlite")
    web = WebUI(__name__, db_manager, host=FLASK_HOST, port=FLASK_PORT)
    web.run()
