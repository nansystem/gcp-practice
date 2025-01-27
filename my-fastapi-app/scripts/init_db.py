from sqlalchemy import create_engine
import sys
import os

# プロジェクトルートをPYTHONPATHに追加
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.core.config import settings
from app.db.base import Base

def init_db() -> None:
    engine = create_engine(settings.DATABASE_URL)
    Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    init_db()
    print("データベーステーブルが作成されました") 