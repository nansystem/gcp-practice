from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.schemas.user import User
from app.services.user import UserService

router = APIRouter()


@router.get("/users/", response_model=list[User])
def read_users(db: Session = Depends(get_db)):
    service = UserService(db)
    return service.get_users()


@router.get("/users/{user_id}", response_model=User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    service = UserService(db)
    user = service.get_user(user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user
