import requests

def make_api_request(method, url, data=None):
    try:
        if method.upper() == 'GET':
            response = requests.get(url)
        elif method.upper() == 'POST':
            response = requests.post(url, json=data)  # Sending data as JSON
        elif method.upper() == 'PUT':
            response = requests.put(url, json=data)  # Sending data as JSON
        elif method.upper() == 'DELETE':
            response = requests.delete(url)
        else:
            raise ValueError("Invalid HTTP method. Please use GET, POST, PUT, or DELETE.")

        
        response.raise_for_status()  
        
        
        return response.json() 
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None

if __name__ == "__main__":
    
    method = input("Enter HTTP method (GET, POST, PUT, DELETE): ")
    url = input("Enter the URL: ")
    
    if method.upper() in ['POST', 'PUT']:
        data = input("Enter JSON data (or leave blank): ")
        if data:
            data = eval(data)  
        else:
            data = None
    else:
        data = None

    
    result = make_api_request(method, url, data)

    print("Response from the API:")
    print(result)
