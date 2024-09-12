import logging
from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from .database import database  # 相対インポート
from pydantic import BaseModel
from typing import List, Optional

# ロガーの設定
logger = logging.getLogger("uvicorn.error")
app = FastAPI()

# CORS設定
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # ここを特定のドメインに限定することも可能
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Item(BaseModel):
    id: int
    detail: str

@app.on_event("startup")
async def startup():
    try:
        await database.connect()
        logger.info("Database connected successfully")
    except Exception as e:
        logger.error(f"Database connection failed: {e}")

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()
    logger.info("Database disconnected")

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}", response_model=Item)
async def read_time(item_id: int):
    query = "SELECT * FROM item_test WHERE id = :item_id"
    item: Optional[dict] = await database.fetch_one(query=query, values={"item_id": item_id})
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return Item(**item)