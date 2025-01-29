# fastapiアプリ

``` sh
# データベースのテーブルを作成
PYTHONPATH=$PYTHONPATH:. poetry run python scripts/init_db.py
PYTHONPATH=$PYTHONPATH:. poetry run python scripts/seed_db.py
```

``` sh
# 起動
poetry run uvicorn app.main:app --reload
```

``` sh
# dockerで起動
docker build -t fastapi-app .
docker run --rm -p 8080:8080 fastapi-app
```

``` sh
# スキーマを出力
PYTHONPATH=$PYTHONPATH:. poetry run python scripts/export_schema.py
```
