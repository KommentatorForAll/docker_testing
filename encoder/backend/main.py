import urllib.parse

import mysql.connector
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import RedirectResponse, JSONResponse

import encoder
import statistics
from encoder import get_all_encoder_names, EncodingBody

db = mysql.connector.connect(
    host="db",
    user="py",
    password="py",
    database="encoder"
)
db_cursor = db.cursor()

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


@app.get("/statistics")
async def get_statistics():
    return statistics.get_statistics(db_cursor)


@app.post("/encoders/encode")
async def encode(encoding_body: EncodingBody):
    encoding_body.message = urllib.parse.unquote(encoding_body.message.replace("+", " "))
    try:
        ret_val = encoder.encode(encoding_body)
        db_cursor.execute(
            "INSERT INTO calls values (%(type)s, %(message)s, 1) ON DUPLICATE KEY UPDATE amount = amount + 1;",
            {
                "type": encoding_body.type,
                "message": encoding_body.message[:255]
            }
        )
        return ret_val
    except KeyError:
        db_cursor.execute(
            "INSERT INTO error values ('%(type)s', %(message)s, 1) ON DUPLICATE KEY UPDATE amount = amount + 1;",
            {
                "type": encoding_body.type,
                "message": encoding_body.message[:255]
            }
        )
        return JSONResponse(status_code=402, content={"message": "Payment required to use (implement) this encoder"})
    except Exception as e:
        print(e)
        return JSONResponse(status_code=400, content={"message": "an unknown error occurred"})
    finally:
        db.commit()


@app.post("/encoders/encode_url/{enc_type}/{message}")
async def encode_path(enc_type: str, message: str):
    enc_type = urllib.parse.unquote(enc_type)
    body = EncodingBody(type=enc_type, message=message)
    response = await encode(body)
    return response
