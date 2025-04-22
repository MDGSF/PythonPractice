from typing import Annotated
from pydantic import BaseModel, Field
from fastapi import FastAPI, Body

app = FastAPI()


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "name": "Foo",
                    "description": "A very nice Item",
                    "price": 35.4,
                    "tax": 3.2,
                }
            ]
        }
    }


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    results = {"item_id": item_id, "item": item}
    return results


class Item2(BaseModel):
    name: str = Field(examples=["Foo"])
    description: str | None = Field(default=None, examples=["A very nice Item"])
    price: float = Field(examples=[35.4])
    tax: float | None = Field(default=None, examples=[3.2])


@app.put("/items2/{item_id}")
async def update_item2(item_id: int, item: Item2):
    results = {"item_id": item_id, "item": item}
    return results


class Item3(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


@app.put("/items3/{item_id}")
async def update_item3(
    item_id: int,
    item: Annotated[
        Item3,
        Body(
            examples=[
                {
                    "name": "Foo",
                    "description": "A very nice Item",
                    "price": 35.4,
                    "tax": 3.2,
                }
            ],
        ),
    ],
):
    results = {"item_id": item_id, "item": item}
    return results
