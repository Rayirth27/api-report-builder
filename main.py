import requests
import os
import csv
from dotenv import load_dotenv
from datetime import date

load_dotenv()

api = os.environ.get('nasa_api_key')

if not api:
    raise EnvironmentError("API KEY could not be found in .env")

today= date.today()

try:
    r = requests.get('https://api.nasa.gov/planetary/apod/',params = {'api_key':api, 'date':today}, timeout=5)

    data = r.json()

    with open('output_extracted_vertical.csv','w',encoding='utf-8',newline='') as out:
        writer = csv.writer(out)
        writer.writerow(['Field','Value'])
        writer.writerows(data.items())
    print("Output is extracted at the file -> output_extracted_vertical.csv")

except requests.exceptions.HTTPError as e:
    print(f'HTTPError as {e.response.status_code} - {e}')
except requests.exceptions.Timeout:
    print("Request Timeout Error")
except requests.exceptions.ConnectionError:
    print("Connection Failed")
except requests.exceptions.RequestException as e:
    print(f"Something went wrong: {e}")