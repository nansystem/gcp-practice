import sqlalchemy
from pydantic_settings import BaseSettings


class LocalDBConfig(BaseSettings):
    """ローカル開発用DB設定"""

    DB_HOST: str = "localhost"
    DB_PORT: int = 3306
    DB_USER: str = "user"
    DB_PASSWORD: str = ""
    DB_NAME: str = "mydb"

    @property
    def SQLALCHEMY_DATABASE_URI(self) -> str:
        return f"mysql+pymysql://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

    @property
    def engine(self):
        return sqlalchemy.create_engine(
            self.SQLALCHEMY_DATABASE_URI,
            pool_size=5,
            max_overflow=2,
            pool_timeout=30,
            pool_recycle=1800,
        )

    class Config:
        env_prefix = "DB_"
