import requests

def send_request(url, data=None, headers=None):
    try:
        if data:
            response = requests.post(url, data=data, headers=headers)
        else:
            response = requests.get(url, headers=headers)
        return response
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        return None

def print_response(response):
    if response:
        print(f"Status Code: {response.status_code}")
        print("Response Body:\n", response.text)
    else:
        print("No response received.")
