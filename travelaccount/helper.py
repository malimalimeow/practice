import requests 
def get_rate(base, currency): 
    url = f"https://open.er-api.com/v6/latest/{base}" 
    data = requests.get(url).json() 
    return data["rates"][currency] 

