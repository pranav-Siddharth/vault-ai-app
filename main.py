from fastapi import FastAPI, UploadFile
import os

app = FastAPI()

@app.get("/")
def home():
    return {"message": "AI Engine Online - Ready for DigitalOcean"}

@app.post("/upload")
async def upload_file(file: UploadFile):
    return {"filename": file.filename, "status": "Uploaded Successfully"}
