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
        attendance = self.sheet.col_values(1)
        return attendance

    def test(self):
        return self.sheet.get_all_records()


if __name__ == "__main__":
    sp = Spreadsheet()
    print(sp.test())
