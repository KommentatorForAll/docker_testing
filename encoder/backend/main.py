from fastapi import FastAPI
from starlette.responses import RedirectResponse, JSONResponse

from encoder import get_all_encoder_names, EncodingBody
import encoder
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(debug=True)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


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
        return JSONResponse(status_code=402, content={"message": "Payment required to use (implement) this encoder"})
    except Exception as e:
        return JSONResponse(status_code=400, content={"message": e})


@app.post("/encoders/encode_url/{enc_type}/{message}")
async def encode_path(enc_type: str, message: str):
    body = EncodingBody(type=enc_type, message=message)
    response = await encode(body)
    return response
