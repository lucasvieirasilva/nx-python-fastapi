from fastapi import FastAPI
from lib1.hello import hello

app = FastAPI()


@app.get("/")
async def root():
    return {"message": hello()}
