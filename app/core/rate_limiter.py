from fastapi import FastAPI
from fastapi_limiter import FastAPILimiter
import redis.asyncio as redis
from app.core.config import settings

async def setup_rate_limiter(app: FastAPI):
    redis_instance = redis.from_url(settings.REDIS_URL, encoding="utf-8", decode_responses=True)
    await FastAPILimiter.init(redis_instance)