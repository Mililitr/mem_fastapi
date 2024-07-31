from fastapi import FastAPI
from app.routers import memes
from app.database import engine, Base

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(memes.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Meme API"}