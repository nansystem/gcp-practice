# gcp-practice

``` sh
# remix、fastapiの起動
docker-compose build --no-cache
docker-compose up
docker-compose down
```

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

## DB
``` sh
docker-compose exec db mysql -u user -p
```

## インフラ

``` sh
# 変数
PROJECT=$(gcloud config get-value project)
LOCATION=asia-northeast1
NETWORK=my-vpc
SUBNET=my-subnet
REPO=my-repo  # Artifact Registory リポジトリの名前
RUN_SA=run-frontend  # Cloud Run（フロントエンド）に紐付けるサービスアカウントの名前

# VPCの作成
gcloud compute networks create ${NETWORK} \
    --project=${PROJECT} \
    --subnet-mode=custom

# サブネットの作成
gcloud compute networks subnets create ${SUBNET} \
    --project=${PROJECT} \
    --network=${NETWORK} \
    --range=192.168.101.0/24 \
    --region=${LOCATION} \
    --enable-private-ip-google-access


# Artifact Registory リポジトリの作成(gcloud run deployの場合は自動で作成される)
gcloud artifacts repositories create ${REPO} \
    --repository-format=docker \
    --project=${PROJECT} \
    --location=${LOCATION}

# cloud run バックエンドのデプロイ(1分) (公開して確認する用)
cd my-fastapi-app
gcloud run deploy run-backend \
    --source . \
    --region ${LOCATION} \
    --platform managed \
    --allow-unauthenticated \
    --timeout 300s

# cloud run バックエンドのデプロイ(1分) (VPC内のみアクセス可能+認証が必要な状態デプロイ→フロントエンドのサービスアカウント（run-frontend）にバックエンドのrun.invoker権限を付与する必要)
gcloud run deploy run-backend \
    --source . \
    --region ${LOCATION} \
    --platform managed \
    --ingress internal \
    --timeout 300s

# バックエンドのbackend.yamlによる Cloud Run サービスのデプロイ(未検証)
cd manifests
gcloud run services replace backend.yaml \
    --project=${PROJECT} \
    --region=${LOCATION}

# バックエンドの Cloud Run サービスの削除
gcloud run services delete run-backend \
    --region ${LOCATION} \
    --platform managed \
    --quiet

# デプロイの確認
gcloud run services describe run-backend \
  --region ${LOCATION} \
  --format="table[box](status.conditions[].type:label=CONDITION, status.conditions[].status:label=STATUS)"

# エンドポイントの確認
BACKEND_INTERNAL_IP=$(gcloud run services describe run-backend \
  --region asia-northeast1 \
  --format 'value(status.address.url)')
echo ${BACKEND_INTERNAL_IP}


# バックエンドの Cloud Run にアクセスするための権限を付与するためのサービスアカウントを作成
gcloud iam service-accounts create ${RUN_SA} --project=${PROJECT}

# 作成したサービスアカウントに、バックエンドの Cloud Run サービスを呼び出すための Cloud Run 起動元（roles/run.invoker） 権限を付与
gcloud run services add-iam-policy-binding run-backend \
    --role="roles/run.invoker" \
    --member="serviceAccount:${RUN_SA}@${PROJECT}.iam.gserviceaccount.com" \
    --project=${PROJECT} \
    --region=${LOCATION}


# フロントエンドサーバーのデプロイ
# Direct VPC Egressを有効化
# --vpc-ingress all: Cloud Run がインターネットからのトラフィックを受信できるようにする。
# --vpc-egress all-traffic: Cloud Run から送信される全てのトラフィックを VPC 経由で送信する。
cd my-remix-app
gcloud run deploy run-frontend \
  --source . \
  --region ${LOCATION} \
  --ingress all \
  --vpc-egress all-traffic \
  --network ${NETWORK} \
  --subnet ${SUBNET} \
  --set-env-vars "BACKEND_URL=${BACKEND_INTERNAL_IP}" \
  --service-account=${RUN_SA}@${PROJECT}.iam.gserviceaccount.com \
  --allow-unauthenticated \
  --port 3000
```
