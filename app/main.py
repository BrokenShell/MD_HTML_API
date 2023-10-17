import shutil
from tempfile import NamedTemporaryFile

from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse

from app.transform import md_file_to_html_file

VERSION = "0.0.1"
API = FastAPI(
    title='Markdown to HTML',
    version=VERSION,
    docs_url='/',
)
API.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)


@API.get("/version", tags=["General"])
async def version():
    """ Returns API Version """
    return VERSION


@API.post("/process", tags=["MD To HTML"])
async def process(file: UploadFile = File(...)):
    temp_file = NamedTemporaryFile(delete=False)
    with temp_file as buffer:
        shutil.copyfileobj(file.file, buffer)
    filename = file.filename.split(".")[0]
    html_file = filename + ".html"
    md_file_to_html_file(temp_file.name, html_file)
    return FileResponse(
        path=html_file,
        filename=html_file,
        media_type="application/octet-stream",
    )
