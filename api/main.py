from fastapi import FastAPI
from typing import Union
from fastapi import FastAPI, Query, Response
from app.models.qrcode import Qrcode
from app.models.spreadsheet import Spreadsheet

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/attend_employees/{employee_code}")
# post/emplyee_code -> 200 出席 or 400 error 出席済みの参加者です
def check_attendance(employee_code):
    sp = Spreadsheet()
    if sp.is_present(int(employee_code)):
        return Response(content="出席済みの参加者です", media_type="text", status_code=400)
    else:
        sp.attend(int(employee_code))
        return Response(content="出席", media_type="text", status_code=200)


# get/employee_code -> qrcode.png
@app.get("/employees/{employee_code}")
def read_qrcode(employee_code: int):
    qrcode = Qrcode.create(employee_code)
    qrcode_png = Qrcode.convert_png(qrcode, file=None)
    return Response(qrcode_png, media_type="image/png")
