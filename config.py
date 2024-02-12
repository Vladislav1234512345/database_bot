
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        case_sensitive=True,
    )
    bot_token: str

class DatabaseSettings(BaseSettings):
    model_config = SettingsConfigDict(
        case_sensitive=True,
    )
    username: str
    password: str
    localhost: str
    database: str

class User:
    def __init__(self):
        self.login: str = ""
        self.password: str = ""
        self.user_id: str = ""
    def login(self):
        return self.login
    def login(self, login):
        self.login = login
    def password(self):
        return self.password
    def password(self, password):
        self.password = password
    def user_id(self):
        return self.user_id
    def user_id(self, user_id):
        self.user_id = user_id
    def empty(self):
        self.login = ""
        self.password = ""

class Access:
    def __init__(self):
        self.register = False
        self.login = False
    def register(self):
        return self.register
    def register(self, value):
        self.register = value



database_settings = DatabaseSettings()

settings = Settings()

user = User()

access = Access()
