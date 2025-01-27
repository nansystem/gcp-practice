from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from config.settings import settings
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins,
    allow_credentials=True,
    allow_methods=settings.cors_methods,
    allow_headers=settings.cors_headers,
)

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

@app.get("/api/hello")
async def read_root():
    return {"message": "Hello from FastAPI!"} 