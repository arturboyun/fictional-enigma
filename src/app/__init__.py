from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.get("/calculate")
async def read_root(a: int, b: int):
    return {"result": a + b}


def main() -> None:
    print("Hello from app!")
