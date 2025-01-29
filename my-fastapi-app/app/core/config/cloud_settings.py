import sqlalchemy
from google.cloud.sql.connector import Connector, IPTypes
from pydantic_settings import BaseSettings


class CloudSQLConfig(BaseSettings):
    """Google Cloud SQL固有の設定"""

    INSTANCE_CONNECTION_NAME: str
    DB_USER: str
    DB_PASSWORD: str
    DB_NAME: str

    class Config:
        env_file = ".env"
        extra = "ignore"
        env_prefix = "GCLOUD_"
        case_sensitive = True

    @property
    def engine(self):
        connector = Connector(ip_type=IPTypes.PRIVATE)

        def get_connection():
            return connector.connect(
                self.INSTANCE_CONNECTION_NAME,
                "pymysql",
                user=self.DB_USER,
                password=self.DB_PASSWORD,
                db=self.DB_NAME,
            )

        return sqlalchemy.create_engine(
            "mysql+pymysql://",
            creator=get_connection,
            pool_size=5,
            max_overflow=2,
            pool_timeout=30,
            pool_recycle=1800,
        )
