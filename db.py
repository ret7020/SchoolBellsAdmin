import sqlite3
from werkzeug.security import check_password_hash, generate_password_hash

class DbManager:
    def __init__(self, path_to_db: str):
        self.connection = sqlite3.connect(path_to_db, check_same_thread=False)
        self.cursor = self.connection.cursor()
    
    def check_password(self, input_password: str) -> bool:
        real_pass_hash = self.cursor.execute(
            'SELECT `password` FROM `settings`').fetchone()[0]
        return check_password_hash(real_pass_hash, input_password)