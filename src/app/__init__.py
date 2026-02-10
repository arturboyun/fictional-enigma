from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.get("/calculate")
async def calculate_upgrade(a: int = 1, b: int = 1):
    """A simple endpoint to demonstrate calculation."""
    return {"result": a + b}


@app.get("/greet/{name}")
async def greet(name: str):
    return {"message": f"Hello, {name}!"}


def main() -> None:
    print("Hello from app!")
