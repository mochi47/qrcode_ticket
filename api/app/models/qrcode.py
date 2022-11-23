import pyqrcode

URL_CLIENT = "https://localhost:3000/"


class Qrcode:
    def create(str: employee_code) -> str:
        qrcode = pyqrcode.create(
            URL_CLIENT + employee_code, error="Q", version=14
        )  # 400文字のAlphanumetricまでいける
        qrcode_text = qrcode.text()
        return qrcode_text
