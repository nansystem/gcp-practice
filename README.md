# gcp-practice

## remixアプリ
``` sh
# remixアプリを起動
cd my-remix-app
npm run dev -- --port 3000
```

``` sh
# dockerで起動
docker build -t my-remix-app .
docker run -p 8080:3000 my-remix-app

# 特定のコンテナを停止
docker ps
docker stop [コンテナID]
# すべてのコンテナを停止
docker stop $(docker ps -q)
```

``` sh
# gcloud認証
gcloud auth login
# デプロイ
gcloud run deploy remix-service \
  --source . \
  --region asia-northeast1 \
  --platform managed \
  --allow-unauthenticated \
  --min-instances 0

# 削除
gcloud run services delete remix-service --region asia-northeast1
```

## fastapiアプリ
``` sh
# 起動
cd my-fastapi-app
poetry run uvicorn main:app --reload
```