from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello from FastAPI on Render!"}

@app.get("/ping")
def ping():
    return {"status": "Server is running!"}
