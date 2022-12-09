import pyqrcode
from io import BytesIO

URL_CLIENT = "http://127.0.0.1:8000/employees/"


class Qrcode:
    def create(employee_code) -> str:
        qrcode = pyqrcode.create(
            URL_CLIENT + str(employee_code), error="Q", version=14
        )  # 400文字のAlphanumetricまでいける
        return qrcode

    def convert_png(qrcode, file=None):
        if file is None:
            buffer = BytesIO()
            qrcode.png(buffer)
            return buffer.getvalue()
        else:
            return qrcode.png(file, scale=4)


if __name__ == "__main__":
    URL_CLIENT = "https://google.com"
    employee_code = ""
    qrcode = Qrcode.create(employee_code)
    print(Qrcode.convert_png(qrcode, "code.png"))
