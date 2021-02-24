import requests
from datetime import datetime

# use the POST method to create a user

PIXELA_API_ENDPOINT = "https://pixe.la/v1/users"
USERNAME = "firstuser"
TOKEN = "TOKEN"
GRAPH_ID = "graph1"

pixela_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
user_creation_response = requests.post(url=PIXELA_API_ENDPOINT, json=pixela_params)
# print(response.text)

# create a graph
GRAPH_ENDPOINT = f"{PIXELA_API_ENDPOINT}/{USERNAME}/graphs"

graph_params = {
    "id": GRAPH_ID,
    "name": "Python Learning Tracker",
    "unit": "hours",
    "type": "int",
    "color": "sora"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

###################################### Already created the graph so commenting it out ###################

# graph_creation_response = requests.post(url=GRAPH_ENDPOINT, json=graph_params, headers=headers)
# print(graph_creation_response.text)

# yesterday = datetime(year=2021, month=2, day=22)
# yesterday = yesterday.strftime("%Y%m%d")
today = datetime.now()
# post to the habit graph
posting_params = {
    # use the strftime function to format the date in the way the API wants it
    "date": today.strftime("%Y%m%d"),
    "quantity": "3",
}
# print(posting_params["date"])
PIXEL_CREATION_ENDPOINT = f"{PIXELA_API_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}"
post_to_graph = requests.post(url=PIXEL_CREATION_ENDPOINT, json=posting_params, headers=headers)
# print(post_to_graph.text)


# update yesterday's pixel to 0 hours
# update_params = {
#     "quantity": "2"
# }
# update_pixel_endpoint = f"{PIXELA_API_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}/{yesterday}"
# update_pixel = requests.put(url=update_pixel_endpoint, json=update_params, headers=headers)

# delete yesterday's pixel
# delete_pixel_endpoint = f"{PIXELA_API_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}/{yesterday}"
# delete_pixel = requests.delete(url=delete_pixel_endpoint, headers=headers)
# print(delete_pixel.text)
