from fastapi import FastAPI, status

app = FastAPI()


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.get("/calculate")
async def calculate_upgrade(a: int = 1, b: int = 1):
    """A simple endpoint to calculate the sum of two numbers."""
    return {"result": a + b}


@app.get("/greet/{name}")
async def not_green_anymore(name: str):
    return {"message": "It's NOT hello!"}


@app.get("/asd")
async def asd():
    return {"message": "This is a test endpoint."}


@app.get("/teapot", status_code=status.HTTP_418_IM_A_TEAPOT)
async def teapot(name: str):
    return {"message": "I'm a teapot, I cannot brew coffee!"}
