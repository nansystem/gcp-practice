from app.db.base_class import Base
from app.db.session import engine

def init_db() -> None:
    try:
        print("登録されているモデル:")
        for table in Base.metadata.tables.keys():
            print(f"- {table}")
            
        Base.metadata.create_all(bind=engine)
        print("テーブルの作成に成功しました")
    except Exception as e:
        print(f"テーブル作成エラー: {e}")
        raise

if __name__ == "__main__":
    from app.db.session import engine

    try:
        with engine.connect() as conn:
            print("データベースへの接続に成功しました")
    except Exception as e:
        print(f"接続エラー: {e}")

    init_db()
    print("データベースのテーブルが初期化されました。")