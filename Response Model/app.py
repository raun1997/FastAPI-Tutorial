from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Product(BaseModel):
    id: int
    name: str
    price: float | None
    quantity: int

@app.post("/products/")
def create_product(prod: Product)->Product:
    return prod

@app.get("/products/")
def read_products() -> list[Product]:
    return [
        Product(id=1, name="Boat Headphone", price=4999, quantity=5),
    ]
