from typing import List

from fastapi import FastAPI, UploadFile, HTTPException
from starlette.middleware.cors import CORSMiddleware
from starlette.responses import Response, JSONResponse

from database import database
from models import sales_table
from utils import extract_sales_data_from_text_array

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*']
)


@app.post("/upload_file/")
async def upload_file(files: List[UploadFile]):
    message = 'Successfully created!'

    for file in files:
        if not file.filename.endswith(".txt"):
            raise HTTPException(status_code=400, detail="Only .txt files are allowed")

        contents = await file.read()
        lines = contents.decode().splitlines()

        if len(lines) == 0:
            raise HTTPException(status_code=400, detail="The file is empty")

        sales_data = extract_sales_data_from_text_array(lines)

        for data in sales_data['results']:
            query = sales_table.insert().values(**data)
            await database.execute(query)

        for index, exception in enumerate(sales_data['exceptions']):
            if index == 0:
                message = message + " But we had some exceptions:\n"

            message = message + exception + "\n"

    return JSONResponse({"detail": message}, status_code=201)
