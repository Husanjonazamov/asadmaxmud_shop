import requests
from utils.env import BASE_URL

def createUser(user):
    url = f"{BASE_URL}/users/"
    response = requests.post(url, json=user)
    print(response.status_code)
    if response.status_code == 201:  
        data = response.json()
        return data
    else:
        print(response.status_code)


def getUser(user_id):
    url = f"{BASE_URL}/users/{user_id}/"
    response = requests.get(url)  
    
    if response.status_code == 200: 
        data = response.json()
        return data
    else:
        print(response.status_code)
