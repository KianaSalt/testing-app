from flask import Flask, render_template, request, jsonify 
import requests
import os
import asyncio
import random
import json


app = Flask(__name__)

booked_services = []

tips_data = [
    {"text": "Pack light and smart.", "url": "https://www.travelandleisure.com/travel-tips/packing-tips/travel-editor-packing-tips?cjdata=MXxOfDB8WXww&cjevent=05b529406b5e11ee814640fc0a82b824&utm_source=CJ&utm_medium=affiliate"},
    {"text": "Learn a few local phrases.", "url": "https://blog.oncallinternational.com/before-you-travel-key-phrases-to-learn-in-the-local-language/"},
    {"text": "Respect local customs and traditions.", "url": "https://www.kayak.com.au/news/travel-etiquette-tips/#:~:text=7%20Travel%20Etiquette%20Advice%20To%20Better%20Respect%20Local,...%207%207.%20DO%20watch%20your%20dress%20code"},
    # Add more tips as needed
]
hotels_data = [
    {"name": "Hotel A", "location": "City A"},
    {"name": "Hotel B", "location": "City B"},
    {"name": "Hotel C", "location": "City C"},
    # Add more hotel data as needed
]

# Home route
@app.route("/")                   
def home():
    return render_template("index.html", travel_tips=tips_data)




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
    {"cityName": "Berlin", "countryName": "Germany"},
    {"cityName": "Atlanta", "countryName": "Georgia"},
    
    ] #{"cityName": "Bangkok", "countryName": "Thailand"}
   #querystring = {"cityName":"Berlin","countryName":"Germany"}
    #querystring2 = {"cityName":"Atlanta","countryName":"Georgia"}

    headers = {
    "X-RapidAPI-Key": "f483517b4amshef1d273499a38dep145e52jsn49c64fb576fb",
	"X-RapidAPI-Host": "best-booking-com-hotel.p.rapidapi.com"
    }
    all_data = []

    for querystring in querystrings:
        response = requests.get(url, headers=headers, params=querystring)

    #data = response.json()
        #if response.status_code != 200:
            #return f"Error: Received status code {response.status_code} from API."
        data = response.json()

        all_data.append(data)

    return render_template("suggestions.html", datum=all_data)  # Pass the city data to the template




#return render_template("end.html")

    

# About Route
@app.route("/about")
def about():
    return render_template("about.html")
#Book Now
@app.route("/book-now", methods=["GET", "POST"])
def book_now():
    if request.method == "POST":
        selected_service = request.form.get("service")
        # Handle the selected service (store it in a database, etc.)
        return render_template("booking_confirmation.html", service=selected_service)
    else:
        return render_template("book_now.html", services=available_services)



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
