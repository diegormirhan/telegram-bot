"""
from bs4 import BeautifulSoup
import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/58.0.3029.110 Safari/537.3'}


def cidade(city):
    city = city.replace(" ", "+")
    res = requests.get(
        f'https://www.google.com/search?q={city}&oq={city}&aqs=chrome.0.35i39l2j0l4j46j69i60.6128j1j7'
        f'&sourceid=chrome&ie=UTF-8',
        headers=headers)
    soup = BeautifulSoup(res.text, 'html.parser')

    location = soup.select('#wob_loc')[0].getText().strip()
    climate = soup.select('#wob_tm')[0].getText().strip()
    time = soup.select('#wob_dts')[0].getText().strip()
    precipitation = soup.select('#wob_pp')[0].getText().strip()
    humidity = soup.select('#wob_hm')[0].getText().strip()
    info = soup.select('#wob_dc')[0].getText().strip()

    return f'Localização: {location} \n' \
           f'Clima: {climate + "ºC"} - {info} \n' \
           f'Data: {time} \n' \
           f'Precipatação: {precipitation} \n' \
           f'Humidade: {humidity} \n' \
"""
# importing requests and json
import requests
import json

BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
API_KEY = "6ea3659178e682c04bfd3d1db3c6a362"


def cidades(cidade):
    # upadting the URL
    url = BASE_URL + "q=" + cidade + "&appid=" + API_KEY
    # HTTP request
    response = requests.get(url)
    # checking the status code of the request
    if response.status_code == 200:
        # getting data in the json format
        data = response.json()
        # getting the main dict block
        main = data['main']
        # getting temperature
        temp = main['temp']
        temperature = int(temp)
        # getting the humidity
        humidity = main['humidity']
        # getting the pressure
        pressure = main['pressure']
        # weather report
        report = data['weather']
        return f"{temperature - 279}"
    else:
        # showing the error message
        return "Error in the HTTP request"


print(cidades('Ubatuba'))