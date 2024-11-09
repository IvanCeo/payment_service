from dynaconf import Dynaconf
from pydantic import BaseModel


class DBConfig(BaseModel):
    db_name: str
    db_user: str
    db_password: str
    db_host: str
    db_port: str
    
    @property
    def db_url(self):
        return f'postgresql+asyncpg://{self.db_user}:{self.db_password}@{self.db_host}:{self.db_port}/{self.db_name}'

class APPConfig(BaseModel):
    app_port: int
    app_version: str
    app_name: str
    app_host: str
    app_mount: str


class Settings(BaseModel):
    app: APPConfig
    db: DBConfig

dyna_settings = Dynaconf(
    settings_file=['settings.toml'],

)

settings = Settings(app=dyna_settings['app_settings'], db=dyna_settings['db_settings'])
print(settings.app.app_port)