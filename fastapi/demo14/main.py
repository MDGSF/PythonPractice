from typing import Annotated

from fastapi import FastAPI, Header

app = FastAPI()


@app.get("/items/")
async def read_items(user_agent: Annotated[str | None, Header()] = None):
    return {"User-Agent": user_agent}


@app.get("/items2/")
async def read_items2(
    strange_header: Annotated[str | None, Header(convert_underscores=False)] = None,
):
    return {"strange_header": strange_header}


@app.get("/items3/")
async def read_items3(x_token: Annotated[list[str] | None, Header()] = None):
    return {"X-Token values": x_token}
