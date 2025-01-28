from sqlalchemy import Column, Integer, String

from app.db.base_class import Base


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    email = Column(String(255))
    name = Column(String(255))

    def __repr__(self):
        return f"User(id={self.id}, email={self.email}, name={self.name})"
