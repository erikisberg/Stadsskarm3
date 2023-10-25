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

    restaurants = soup.find_all("div", class_="lunchrestaurant")

    for restaurant in restaurants:
        restaurant_name = restaurant.find("h2").text.strip()
        dishes = restaurant.find_all("div", class_="lunch")

        for dish in dishes:
            dish_data = {}
            dish_data["Restaurant"] = restaurant_name
            dish_data["Dish"] = dish.text.strip().replace("\n", " - ")
            restaurants_data.append(dish_data)

    return restaurants_data

@app.route('/get_lunch_data', methods=['GET'])
def get_lunch_data_endpoint():
    data = scrape_site()
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)


