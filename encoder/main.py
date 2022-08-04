from fastapi import FastAPI
from starlette.responses import RedirectResponse

from encoder import get_all_encoder_names, EncodingBody
import encoder

app = FastAPI()


@app.get("/")
async def read_root():
    return RedirectResponse("/docs")


@app.get("/encoders/list")
async def get_encoder_list():
    return get_all_encoder_names()


@app.post("/encoders/encode")
async def encode(encoding_body: EncodingBody):
    return encoder.encode(encoding_body)
