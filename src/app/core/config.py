class DatabasSettings:
    DEBUG: bool = True

    TELEGRAM_BOT_TOKEN = "788371865:AAH_kdWRUdELq2BNYLPkSGbUBMiLaU6h5I0"

    DATABASE_HOST: str = "localhost"
    DATABASE_DB: str = "sqlite3.db"

    @property
    def db_url(self) -> str:
        return "sqlite:///../" + self.DATABASE_DB


settings = DatabasSettings()
