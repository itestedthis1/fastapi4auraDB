from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"code":418, "message": "I am not the teapot your looking for!"}