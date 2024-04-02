# Import FastAPI
from fastapi import FastAPI
from pydantic import BaseModel

# Create an instance of the FastAPI class
app = FastAPI()

class NameItem(BaseModel):
    name: str

# Define a route
@app.get("/")
async def read_root():
    return {"Hello": "World"}

# Define the POST method
@app.post("/testing")
async def testing(item: NameItem):
    return {"Hello": item.name}

# Define the POST method
@app.post("/testing101")
async def testing(item: NameItem):
    return {"Hello": item.name}