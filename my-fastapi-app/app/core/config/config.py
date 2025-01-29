from .base_settings import BaseConfig
from .cloud_settings import CloudSQLConfig
from .local_settings import LocalDBConfig


class Settings(BaseConfig):
    """アプリケーション全体の設定クラス"""

    # データベース設定
    DB: LocalDBConfig | CloudSQLConfig | None = None

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._configure_database()

    def _configure_database(self):
        """環境に応じてデータベース設定を選択"""
        if self.ENVIRONMENT == "local":
            self.DB = LocalDBConfig()
        else:
            self.DB = CloudSQLConfig()

    @property
    def database_engine(self):
        if not self.DB:
            raise ValueError("Database configuration not initialized")
        return self.DB.engine if hasattr(self.DB, "engine") else None


def get_settings() -> Settings:
    return Settings()


settings = get_settings()
print("★settings:", settings)
