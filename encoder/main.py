from fastapi import FastAPI
from starlette.responses import RedirectResponse, JSONResponse

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
    try:
        return encoder.encode(encoding_body)
    except KeyError:
        return JSONResponse(status_code=402, content="Payment required to use (implement) this encoder")
