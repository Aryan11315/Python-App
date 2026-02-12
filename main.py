from fastapi import FastAPI
from pydantic import BaseModel
import os

app = FastAPI()

# Demo model
class User(BaseModel):
    name: str
    age: int

@app.get("/")
def read_root():
    return {"message": "FastAPI deployed successfully on Render 🚀"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}

@app.post("/user")
def create_user(user: User):
    return {
        "message": "User created successfully",
        "data": user
    }

# IMPORTANT FOR RENDER
if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 10000))
    uvicorn.run(app, host="0.0.0.0", port=port)
