from fastapi import FastAPI, UploadFile, File
from media_service.utils import upload_file_to_s3

app = FastAPI()

@app.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    file_url = await upload_file_to_s3(file)
    return {"file_url": file_url}