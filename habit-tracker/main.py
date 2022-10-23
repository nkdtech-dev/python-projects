import requests
from datetime import datetime

user_name = "nkem"
password = "1twihsksgwiogieyfoisif"
pixela_endpoint = "https://pixe.la/v1/users"

user_parameters = {
    "token": password,
    "username": user_name,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}
today = datetime.now()
graph_id = "graph2"
#    -----------------------------creating a pixela acount-----------------------------------------------------------3
# response = requests.post(url=pixela_endpoint, json=user_parameters)
# print(response.text)

graph_parameters = {
    "id": graph_id,
    "name": "study graph",
    "unit": "km",
    "type": "float",
    "color": "sora"
}
headers = {
    "X-USER-TOKEN": password,
}
# ---------------------------------------------------creating a graph-------------------------------------------#
graphs_endpoint = f"{pixela_endpoint}/{user_name}/graphs"
response = requests.post(url=graphs_endpoint, json=graph_parameters, headers=headers)
print(response.text)

post_details = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "9.6",
}
# ---------------------------------------------------updating graph_______________________________________#
response = requests.post(url=f"{pixela_endpoint}/{user_name}/graphs/{graph_id}", json=post_details, headers=headers)
print(response.text)
data_to_update = {
    "id": graph_id,
    "name": "study graph",
    "unit": "km",
    "color": "ajisai"
}
new_pixel_data = {
    "quantity": "19"
}
put_endpoint = f"https://pixe.la/v1/users/{user_name}/graphs/{graph_id}/{today.strftime('%Y%m%d')}"
# ---------------------------------------updating graph data---------------------------------------------------#

# response = requests.put(url=put_endpoint, json=new_pixel_data, headers=headers)
# # print(response.text)

# -----------------------------------------------deleting graph data-------------------------------------------#
# response = requests.delete(url=put_endpoint, headers=headers)
# print(response.text)
