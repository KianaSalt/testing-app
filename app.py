from flask import Flask, render_template, request, jsonify 
import requests
import os
import asyncio
import random
import json


app = Flask(__name__)

# Home route
@app.route("/")                   
def home():
    return render_template("home.html")

# Booking route
@app.route("/booking")                   
def booking():
    # Perform API request (if needed)
    # ...
    available_services = ["Service A", "Service B", "Service C", "Service D", "Service E"]  # List of available services
    return render_template("booking.html", services=available_services)


# Suggestions route
@app.route("/suggestions")                   
def end():
    url = "https://best-booking-com-hotel.p.rapidapi.com/booking/best-accommodation"

   # List of query strings
    querystrings = [
    {"cityName": "Bangkok", "countryName": "Thailand"},
    {"cityName": "Punta Cana", "countryName": "Dominican Republic"},
    ]
    headers = {
    "X-RapidAPI-Key": "4894c3a1bcmshd133c8566ef57e7p1c5692jsn39cf5eb18188",
	"X-RapidAPI-Host": "best-booking-com-hotel.p.rapidapi.com"
    }
    all_data = []

    for querystring in querystrings:
        response = requests.get(url, headers=headers, params=querystring)

        data = response.json()

        all_data.append(data)

    return render_template("suggestions.html", datum=all_data)  # Pass the city data to the template


# Get hotels route (if needed)
@app.route("/get_hotels")                   
def get_hotels():
    url = "https://apidojo-booking-v1.p.rapidapi.com/currency/get-exchange-rates?rapidapi-key=ff511b0e11msh532c009df749b7fp1c32f0jsncc64d31ee82a"
    querystring = {"cityName": "Berlin", "countryName": "Germany"}

    headers = {
         "X-RapidAPI-Key": "ff511b0e11msh532c009df749b7fp1c32f0jsncc64d31ee82a",
         "X-RapidAPI-Host": "apidojo-booking-v1.p.rapidapi.com"
    }

    try:
        response = requests.get(url, headers=headers, params=querystring)
        response.raise_for_status()  # Raise an HTTPError for bad requests (4xx and 5xx status codes)
        hotels_data = response.json().get("data", [])
        return render_template("hotels.html", hotels=hotels_data)
    except requests.exceptions.HTTPError as errh:
        return f"HTTP Error: {errh}"
    except requests.exceptions.ConnectionError as errc:
        return f"Error Connecting: {errc}"
    except requests.exceptions.Timeout as errt:
        return f"Timeout Error: {errt}"
    except requests.exceptions.RequestException as err:
        return f"Something went wrong: {err}"

if __name__ == "__main__":
    app.run(debug=True)
