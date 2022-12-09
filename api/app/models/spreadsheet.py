import gspread
from oauth2client.service_account import ServiceAccountCredentials


class Spreadsheet:
    def __init__(self):
        scope = [
            "https://spreadsheets.google.com/feeds",
            "https://www.googleapis.com/auth/drive",
        ]
        creds = ServiceAccountCredentials.from_json_keyfile_name(
            "client_secret.json", scope
        )
        client = gspread.authorize(creds)
        self.sheet = client.open_by_key(
            "1Dq9PKsj2UJusT-Bv06M0PELOjaPeE2Iym-qd-8fukb4"
        ).sheet1

    def is_present(self, employee_code: int):
        attendance = self.sheet.cell(int(employee_code) + 1, 3).value
        return attendance == "出席済み"

    def attend(self, employee_code: int):
        self.sheet.update_cell(int(employee_code) + 1, 3, "出席済み")

    def test(self):
        return self.sheet.get_all_records()


if __name__ == "__main__":
    sp = Spreadsheet()
    sp.attend(5)
    print(sp.is_present(5))
    print(sp.test())
