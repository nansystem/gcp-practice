from datetime import datetime

import strawberry


@strawberry.type
class User:
    id: int
    name: str
    email: str
    created_at: datetime


@strawberry.type
class Query:
    @strawberry.field
    def users(self) -> list[User]:
        # ダミーデータを返す
        return [
            User(
                id=1,
                name="Test User 1",
                email="test1@example.com",
                created_at=datetime.now(),
            ),
            User(
                id=2,
                name="Test User 2",
                email="test2@example.com",
                created_at=datetime.now(),
            ),
        ]

    @strawberry.field
    def user(self, id: int) -> User | None:
        # IDに基づいてユーザーを返す
        return User(
            id=id,
            name=f"User {id}",
            email=f"user{id}@example.com",
            created_at=datetime.now(),
        )


@strawberry.type
class Mutation:
    @strawberry.mutation
    def create_user(self, name: str, email: str) -> User:
        # 新規ユーザー作成（ダミー）
        return User(id=3, name=name, email=email, created_at=datetime.now())

    @strawberry.mutation
    def update_user(self, id: int, name: str, email: str) -> User:
        # ユーザー更新（ダミー）
        return User(id=id, name=name, email=email, created_at=datetime.now())

    @strawberry.mutation
    def delete_user(self, id: int) -> bool:
        # ユーザー削除（ダミー）
        return True


schema = strawberry.Schema(query=Query, mutation=Mutation)
