import requests
from dotenv import load_dotenv
import os
import json
load_dotenv()
API_KEY = os.getenv('API_KEY')



def fetch_data(animal_name):
    """
    Fetching data as json from api ninjas and converting to list

    Parameter: animal_name as string

    Returns: a list of animals, each animal is a dictionary:
    {
    'name': ...,
    'taxonomy': {
      ...
    },
    'locations': [
      ...
    ],
    'characteristics': {
      ...
    }
    },
    
    """
    try:
        api_url = f'https://api.api-ninjas.com/v1/animals?name={animal_name}'
        response = requests.get(api_url, headers={'X-Api-Key': API_KEY})
        print(response)
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error during request: {e}")
       
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")

    return None