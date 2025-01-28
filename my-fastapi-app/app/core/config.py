from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    ENVIRONMENT: str = "development"
    DB_HOST: str = "localhost"
    DB_PORT: str = "5432"
    DB_USER: str = "user"
    DB_PASSWORD: str = ""
    DB_NAME: str = "mydb"
    INSTANCE_CONNECTION_NAME: str = ""

    @property
    def DATABASE_URL(self) -> str:
        if self.ENVIRONMENT == "production":
            return f"mysql+pymysql://{self.DB_USER}:{self.DB_PASSWORD}@/{self.DB_NAME}?unix_socket=/cloudsql/{self.INSTANCE_CONNECTION_NAME}"
        return f"mysql+pymysql://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

    class Config:
        env_file = ".env"
        case_sensitive = True
        extra = "ignore"


def get_settings() -> Settings:
    return Settings()


settings = get_settings()

print(settings.DATABASE_URL)
