from fastapi import FastAPI, Body

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI app!"}

@app.post("/items/")
def create_item(item: dict = Body(...)):
    # The request body is directly handled as a dictionary
    name = item.get("name")
    description = item.get("description")
    return {"item_name": name, "item_description": description}
