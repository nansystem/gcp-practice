from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter

from app.api.v1 import users
from app.graphql.schema import schema

# debug: Cloud SQLへの接続確認
# from app.core.config.cloud_settings import CloudSQLConfig

# config = CloudSQLConfig()
# engine = config.engine

# try:
#     with engine.connect() as conn:
#         result = conn.execute(sqlalchemy.text("SELECT 1"))
#         print("★Connection successful! Result:", result.scalar())
# except Exception as e:
#     print("★Connection failed:", e)
# finally:
#     engine.dispose()


app = FastAPI()

app.include_router(users.router, prefix="/api/v1")

graphql_app = GraphQLRouter(schema)
app.include_router(graphql_app, prefix="/api/graphql")
