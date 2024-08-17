class DatabasSettings:
    DEBUG: bool = True

    TELEGRAM_BOT_TOKEN = ""

    DATABASE_HOST: str = "localhost"
    DATABASE_DB: str = "sqlite3.db"

    @property
    def db_url(self) -> str:
        return "sqlite:///../" + self.DATABASE_DB


settings = DatabasSettings()
