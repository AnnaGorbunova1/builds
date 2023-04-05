from fastapi import FastAPI
from pydantic import BaseModel
import tasks


class BuildName(BaseModel):
    build: str


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/get_tasks")
async def get_tasks(param: BuildName):
    result = await tasks.get_tasks_for_build(param.build)
    return result


