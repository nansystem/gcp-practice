from pathlib import Path

from sqlalchemy import text

from app.db.session import engine


def execute_sql_file(conn, file_path: Path) -> None:
    with open(file_path) as f:
        sql = f.read()
        conn.execute(text(sql))


def seed_db() -> None:
    try:
        sql_dir = Path(__file__).parent / "sql"

        with engine.begin() as conn:
            # SQLファイルを番号順に実行
            sql_files = sorted(sql_dir.glob("*.sql"))
            for sql_file in sql_files:
                print(f"Executing {sql_file.name}")
                execute_sql_file(conn, sql_file)

        print("初期データの作成に成功しました")
    except Exception as e:
        print(f"初期データ作成エラー: {e}")
        raise


def main():
    seed_db()


if __name__ == "__main__":
    main()
