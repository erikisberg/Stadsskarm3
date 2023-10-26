from flask import Flask, jsonify, request
import requests
from bs4 import BeautifulSoup
from flask_cors import CORS

app = Flask(__name__)
CORS(app, origins=["https://www.gofantastic.org"])

BASE_URL = "https://www.matochmat.se/lunch/ostersund/"

def scrape_site():
    response = requests.get(BASE_URL)
    soup = BeautifulSoup(response.content, 'html.parser')

    restaurants_data = []

    restaurants = soup.find_all("div", class_="lunchMenuListItem")

    for restaurant in restaurants:
        restaurant_name = restaurant.find("h2").text.strip()
        dishes = restaurant.find_all("div", class_="dish")

        for dish in dishes:
    dish_name = dish.find("span", class_="dish__name").text.strip()

    # Check if the dish has a description
    dish_description_element = dish.find("span", class_="dish__bottomRow")
    if dish_description_element:
        dish_description = dish_description_element.text.strip()
    else:
        dish_description = ""

    dish_data = {
        "Restaurant": restaurant_name,
        "Dish": dish_name,
        "Description": dish_description
    }
    restaurants_data.append(dish_data)


    return restaurants_data

@app.route('/get_lunch_data', methods=['GET'])
def get_lunch_data_endpoint():
    data = scrape_site()
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)


