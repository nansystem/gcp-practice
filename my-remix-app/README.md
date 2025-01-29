## remixアプリ
``` sh
# remixアプリを起動
cd my-remix-app
npm run dev -- --port 3000
```

``` sh
# dockerで起動
docker build -t remix-app .
docker run -p 3000:3000 remix-app

# 停止
docker ps
docker stop [コンテナID]
# すべてのコンテナを停止
docker stop $(docker ps -q)
```
