from fastapi import FastAPI, HTTPException

app = FastAPI(title="CI/CD Demo App")

items = {
    1: {"name": "Laptop", "price": 800},
    2: {"name": "Mouse", "price": 20},
    3: {"name": "Keyboard", "price": 45},
}


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/")
def root():
    return {"message": "Welcome To the CI/CD Demo App"}


@app.get("/items/{item_id}")
def get_item(item_id: int):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    return items[item_id]