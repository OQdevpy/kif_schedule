import sqlite3


class Database:
    def __init__(self, path_to_db="main.db"):
        self.path_to_db = path_to_db

    @property
    def connection(self):
        return sqlite3.connect(self.path_to_db)

    def execute(self, sql: str, parameters: tuple = None, fetchone=False, fetchall=False, commit=False):
        if not parameters:
            parameters = ()
        connection = self.connection
        # connection.set_trace_callback(logger)
        cursor = connection.cursor()
        data = None
        cursor.execute(sql, parameters)

        if commit:
            connection.commit()
        if fetchall:
            data = cursor.fetchall()
        if fetchone:
            data = cursor.fetchone()
        connection.close()
        return data

    def create_table_users(self):
        sql = """
        CREATE TABLE BotUsers(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            telegram_id integer NOT NULL,
            tg_name varchar(255),
            full_name varchar(255) NOT NULL,
            phone_number varchar(255),
            user_name varchar(255),
            unvon varchar(255),
            language varchar(2) DEFAULT 'uz',
            join_date varchar(60),
            UNIQUE(telegram_id)
            );
"""
        self.execute(sql, commit=True)

    @staticmethod
    def format_args(sql, parameters: dict):
        sql += " AND ".join([
            f"{item} = ?" for item in parameters
        ])
        return sql, tuple(parameters.values())

    def add_bot_user(self, telegram_id: int, full_name: str, user_name: str = None):
        sql = """
        INSERT INTO BotUsers(telegram_id, full_name, user_name, join_date) VALUES(?, ?, ?, datetime('now'))
        """
        self.execute(sql, parameters=(telegram_id, full_name, user_name), commit=True)


    def select_user(self, **kwargs):
        sql = f"SELECT * FROM BotUsers WHERE "
        sql, parameters = self.format_args(sql, kwargs)
        return self.execute(sql, parameters=parameters, fetchone=True)
    
    def update_user_data(self, telegram_id, full_name, user_name, phone_num, unvon):
        sql = f"""
        UPDATE BotUsers SET full_name = ?, user_name = ?, phone_number = ?, unvon = ? WHERE telegram_id = ?
        """
        self.execute(sql, parameters=(full_name, user_name, phone_num, unvon, telegram_id), commit=True)
    def update_user_language(self, telegram_id, language):
        sql = f"""
        UPDATE BotUsers SET language = ? WHERE telegram_id = ?
        """
        self.execute(sql, parameters=(language, telegram_id), commit=True)
    def update_tg_name(self, telegram_id, tg_name):
        sql = f"""
        UPDATE BotUsers SET tg_name = ? WHERE telegram_id = ?
        """
        self.execute(sql, parameters=(tg_name, telegram_id), commit=True)
    def select_all_users(self):
        sql = f"""
        SELECT * FROM BotUsers
        """
        return self.execute(sql, fetchall=True)
    
    
    def drop_message(self):
        self.execute("DROP TABLE Messages", commit=True)
