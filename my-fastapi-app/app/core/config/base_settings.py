from pydantic_settings import BaseSettings


class BaseConfig(BaseSettings):
    """全環境共通の基本設定"""

    ENVIRONMENT: str = "local"

    class Config:
        env_file = ".env"  # ローカル開発時のみ使用
        extra = "ignore"
