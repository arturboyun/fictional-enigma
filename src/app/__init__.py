from typing import Annotated

from fastapi import Body, FastAPI, status

app = FastAPI()


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.post("/login")
async def login(
    username: Annotated[str, Body()],
    password: Annotated[str, Body()],
    metadata: Annotated[dict | None, Body()] = None,
) -> dict:
    print(f"Received login request for username: {username}, with metadata: {metadata}")
    return {"username": username, "success": True, "metadata": metadata}


@app.post("/register")
async def register(
    username: Annotated[str, Body()],
    password: Annotated[str, Body()],
) -> dict:
    return {"username": username, "success": True}

@app.post("/b1")
async def b1(
    data: Annotated[dict, Body()]
) -> dict:
    print(f"Received data: {data}")
    return {"success": True, "received_data": data}