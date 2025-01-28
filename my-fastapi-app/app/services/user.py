from sqlalchemy.orm import Session

from app.repositories.user import UserRepository
from app.schemas.user import User as UserSchema


class UserService:
    def __init__(self, db: Session):
        self.repository = UserRepository(db)

    def get_users(self) -> list[UserSchema]:
        users = self.repository.get_all()
        return [UserSchema.from_orm(user) for user in users]

    def get_user(self, user_id: int) -> UserSchema | None:
        user = self.repository.get_by_id(user_id)
        return UserSchema.from_orm(user) if user else None
