from fastapi import FastAPI

app = FastAPI()

# Run firt endpoint
@app.get("/")
def read_root():
    return {"message": "Financial Budget API Running 🚀"}