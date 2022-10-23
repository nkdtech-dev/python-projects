import requests
from datetime import datetime

# ------------------------------editable parameter-------------------------------#
GENDER = "male"
WEIGHT_KG = "58kg"
HEIGHT_CM = "1.67cm"
AGE = 20
# ---------------------------------------strings --------------------------------#
spreadsheet_api = "https://api.sheety.co/6e7fcee8d722ea977fcdd89370bae85c/pythonProjectWorksheet/sheet1"
nutritionix_api_key = "9b4d8a7117b634ec8bff54da70e8c755"
nutritionix_api_ID = "7b73b458"
nutritionix_exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

# --------------------------------------nutritionix header-------------------------------------#
headers = {
    "x-app-id": nutritionix_api_ID,
    "x-app-key": nutritionix_api_key,
    "x-remote-user-id": "0"
}
# ------------------------------------------------nutritionix  queries----------------------------------#
queries = {
    "query": input("tell me which exercise you did today"),
    # "gender": GENDER,
    # "weight_kg": WEIGHT_KG,
    # "height_cm": HEIGHT_CM,
    # "age": AGE

}

response = requests.post(nutritionix_exercise_endpoint, json=queries, headers=headers)
response.raise_for_status()
data = response.json()
# ------------------------------------sheet query--------------------------------#
TOKEN = "Bearer KFUFUYFOHPIGILFGPIOHOFGIFIU"
bearer_headers = {
    "Authorization": TOKEN
}
for item in data['exercises']:
    body = {
        "sheet1": {
            "date": datetime.today().strftime("%d/%m/%Y"),
            "time": datetime.now().strftime("%H:%M:%S"),
            "exercise": item["name"].title(),
            "duration": item["duration_min"],
            "calories": item["nf_calories"]

        }
    }
    sheet_response = requests.post(spreadsheet_api, json=body, headers=bearer_headers)
    print(sheet_response.text)
