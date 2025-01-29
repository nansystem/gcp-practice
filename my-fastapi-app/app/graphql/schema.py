from datetime import datetime

import strawberry

USERS = [
    {
        "id": 1,
        "name": "Test User 1",
        "email": "test1@example.com",
        "created_at": datetime.now(),
    },
    {
        "id": 2,
        "name": "Test User 2",
        "email": "test2@example.com",
        "created_at": datetime.now(),
    },
]


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
        return [User(**user) for user in USERS]

    @strawberry.field
    def user(self, id: int) -> User | None:
        user = next((user for user in USERS if user["id"] == id), None)
        return User(**user) if user else None


@strawberry.type
class Mutation:
    @strawberry.mutation
    def create_user(self, name: str, email: str) -> User:
        new_id = max(user["id"] for user in USERS) + 1

        new_user = {
            "id": new_id,
            "name": name,
            "email": email,
            "created_at": datetime.now(),
        }

        USERS.append(new_user)
        return User(**new_user)

    @strawberry.mutation
    def update_user(self, id: int, name: str, email: str) -> User | None:
        user_index = next(
            (index for index, user in enumerate(USERS) if user["id"] == id), None
        )

        if user_index is None:
            return None

        USERS[user_index].update({"name": name, "email": email})

        return User(**USERS[user_index])

    @strawberry.mutation
    def delete_user(self, id: int) -> bool:
        user_index = next(
            (index for index, user in enumerate(USERS) if user["id"] == id), None
        )

        if user_index is None:
            return False

        USERS.pop(user_index)
        return True


schema = strawberry.Schema(query=Query, mutation=Mutation)
