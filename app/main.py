from fastapi import FastAPI
from app.views import router
from app.database import engine
from app.models import Base

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(router)
