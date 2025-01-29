import sqlalchemy
from fastapi import FastAPI

from app.api.v1 import users
from app.core.config.cloud_settings import CloudSQLConfig

config = CloudSQLConfig()
engine = config.engine

try:
    with engine.connect() as conn:
        result = conn.execute(sqlalchemy.text("SELECT 1"))
        print("★Connection successful! Result:", result.scalar())
except Exception as e:
    print("★Connection failed:", e)
finally:
    engine.dispose()


app = FastAPI()

app.include_router(users.router, prefix="/api/v1")
