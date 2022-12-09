from fastapi import FastAPI
from typing import Union
from fastapi import FastAPI, Query, Response
from app.models.qrcode import Qrcode

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/employees/{employee_code}")
# post/emplyee_code -> 200 出席 or 400 error 出席済みの参加者です
def check_attendance(employee_code):
    # TODO　if has_attended: raise Error400 "出席済みの参加者です"
    pass


# get/employee_code -> qrcode.png
@app.get("/employees/{employee_code}")
def read_qrcode(employee_code: int):
    qrcode = Qrcode.create(employee_code)
    qrcode_png = Qrcode.convert_png(qrcode, file=None)
    return Response(qrcode_png, media_type="image/png")
