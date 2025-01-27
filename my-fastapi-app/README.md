# fastapiアプリ

``` sh
# 起動
cd my-fastapi-app
poetry run uvicorn main:app --reload
```

``` sh
# dockerで起動
docker build -t fastapi-app .
docker run --rm -p 8080:8080 fastapi-app
```
