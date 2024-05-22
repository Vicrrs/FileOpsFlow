#!/usr/bin/env python
# -*- coding: utf-8 -*-

from fastapi import FastAPI, File, UploadFile
from fastapi.responses import FileResponse
import os

app = FastAPI()


@app.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    file_location = f"/code/uploads/{file.filename}"
    with open(file_location, "wb+") as file_object:
        file_object.write(await file.read())
    return {"info": f"file '{file.filename}' saved at '{file_location}'"}


@app.get("/download/{file_name}")
async def download_file(file_name: str):
    file_location = f"/code/uploads/{file_name}"
    if os.path.exists(file_location):
        return FileResponse(path=file_location, filename=file_name)
    return {"error": "File not found"}

