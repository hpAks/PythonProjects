import datetime

import requests

pixela_endpoint = "https://pixe.la/v1/users"
create_graph_endpoint = pixela_endpoint + "/testing1123/graphs"
add_pixela_endpoint = create_graph_endpoint +"/grap1"

user_params= {
    "token":"ajhy234hnkkgh5063nkkmm",
    "username":"testing1123",
    "agreeTermsOfService":"yes",
    "notMinor":"yes",
}
#response = requests.post(url=pixela_endpoint,json=user_params)
#print(response.json())


graph_params = {
    "id":"grap1",
    "name":"Meditation Graph",
    "unit":"Minutes",
    "type": "float",
    "color":"kuro",
}
headers = {
    "X-USER-TOKEN":"ajhy234hnkkgh5063nkkmm"
}
#graph_response = requests.post(url=create_graph_endpoint,json=graph_params, headers=headers)
#print(graph_response.json())

body = {
    "date":datetime.date.today().strftime("%Y%m%d"),
    "quantity":"60",
}

#add_pixel_response = requests.post(url=add_pixela_endpoint,json=body, headers=headers)
#print(add_pixel_response.json())

update_pixel_quantity = {
    "quantity":"120"
}
update_pixel_url = add_pixela_endpoint+"/"+ datetime.date.today().strftime("%Y%m%d")
update_pixel = requests.put(url=update_pixel_url,headers=headers,json=update_pixel_quantity)
print(update_pixel.json())
