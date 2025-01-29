import os
from contextlib import contextmanager
from pathlib import Path

import pymysql
import sqlalchemy
from dotenv import load_dotenv
from google.cloud.sql.connector import Connector, IPTypes

env_path = Path.cwd() / ".env"
load_dotenv(env_path)


def connect_with_connector() -> sqlalchemy.engine.base.Engine:
    instance_connection_name = os.environ[
        "GCLOUD_INSTANCE_CONNECTION_NAME"
    ]  # e.g. 'project:region:instance'
    db_user = os.environ["GCLOUD_DB_USER"]  # e.g. 'my-db-user'
    db_pass = os.environ["GCLOUD_DB_PASSWORD"]  # e.g. 'my-db-password'
    db_name = os.environ["GCLOUD_DB_NAME"]  # e.g. 'mydb'

    ip_type = IPTypes.PRIVATE if os.environ.get("PRIVATE_IP") else IPTypes.PUBLIC

    connector = Connector(ip_type)

    def getconn() -> pymysql.connections.Connection:
        conn: pymysql.connections.Connection = connector.connect(
            instance_connection_name,
            "pymysql",
            user=db_user,
            password=db_pass,
            db=db_name,
        )
        return conn

    pool = sqlalchemy.create_engine(
        "mysql+pymysql://",
        creator=getconn,
    )
    return pool


@contextmanager
def get_db():
    engine = connect_with_connector()
    try:
        with engine.connect() as connection:
            yield connection
    finally:
        engine.dispose()


def get_users():
    with get_db() as db:
        result = db.execute(sqlalchemy.text("SELECT * FROM users"))
        return [
            {
                "id": row[0],
                "name": row[1],
                "email": row[2],
            }
            for row in result
        ]


if __name__ == "__main__":
    print(os.environ.get("PRIVATE_IP"))
    users = get_users()
    print(users)
